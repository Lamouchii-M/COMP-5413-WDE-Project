import glob
import os.path
from collections import OrderedDict
from pygments.lexers import PythonLexer
import xmltodict
import javalang
import ast
import pygments
from pygments.lexers import JavaLexer
from pygments.token import Token
import json
from datasets import DATASET


class BugReport:
    
    __slots__ = ['summary', 'description', 'fixed_files',
                 'pos_tagged_summary', 'pos_tagged_description', 'stack_traces']
    
    def __init__(self, summary, description, fixed_files):
        self.summary = summary
        self.description = description
        self.fixed_files = fixed_files
        self.pos_tagged_summary = None
        self.pos_tagged_description = None
        self.stack_traces = None


class SourceFile:
    
    __slots__ = ['all_content', 'comments', 'class_names', 'attributes',
                 'method_names', 'variables', 'file_name', 'pos_tagged_comments',
                 'exact_file_name', 'package_name']
    
    def __init__(self, all_content, comments, class_names, attributes,
                 method_names, variables, file_name, package_name):
        self.all_content = all_content
        self.comments = comments
        self.class_names = class_names
        self.attributes = attributes
        self.method_names = method_names
        self.variables = variables
        self.file_name = file_name
        self.exact_file_name = file_name[0]
        self.package_name = package_name
        self.pos_tagged_comments = None


class Parser:
    
    __slots__ = ['name', 'src', 'bug_repo']
    
    def __init__(self, project):
        self.name = project.name
        self.src = project.src
        self.bug_repo = project.bug_repo
        
    
    def report_parser(self):
      with open(self.bug_repo) as json_file: 
        data = json.load(json_file) 
  
      bug_reports = OrderedDict()
      count=0
      fixedFilesArray=[]
      for i in data["closed_issues"]:
        fixedFilesArray.clear()  
        for items in data["closed_issues"][i].get("files_changed"):
          if items != []:
            fixedFilesArray.append(os.path.normpath(items[1]))
        selected_files = list(filter(lambda x: x.endswith('.py'), fixedFilesArray))
        if selected_files:       
          bug_reports[count] = BugReport(
                 data["closed_issues"][i].get("issue_summary"),
                 data["closed_issues"][i].get("issue_description") 
                     if data["closed_issues"][i].get("issue_description") else '',
                 selected_files[:]
             )
             
          count+=1
             
      print('Total bug reports:'+str(count))        
      return bug_reports          
  

    def src_parser(self):
        src_addresses = glob.glob(str(self.src) + '/**/*.py', recursive=True)
        
        python_lexer = PythonLexer()
        
        src_files = OrderedDict()
        for src_file in src_addresses:         
            
            with open(src_file,encoding = "ISO-8859-1") as file:
                src = file.read()

            comments = ''
            class_names = []
            attributes = []
            method_names = []
            variables = []
            module = ast.parse(src)

            try:
               for node in ast.walk(module):
                  if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    variables.append(node.id)
                  elif isinstance(node, ast.Attribute):                
                    attributes.append(node.attr)
                  elif isinstance(node, ast.FunctionDef):
                    method_names.append(node.name)
                  elif isinstance(node, ast.ClassDef):
                    class_names.append(node.name)
            except:
                pass
                                
            lexed_src = pygments.lex(src, python_lexer)
            ind = True
            for i, token in enumerate(lexed_src):
                if token[0] in Token.Comment:
                    if ind and i == 0 and token[0] is Token.Comment.Multiline:
                        src = src[src.index(token[1]) + len(token[1]):]
                        continue
                    comments += token[1]
                
                      
            package_name = None           
                         
            
            src_id=src_file
                                        
            src_id=src_id.replace(str(DATASET.src)+'/','')
            
            s1= SourceFile(
                    src, comments, class_names, attributes,
                    method_names, variables,
                    [os.path.basename(src_file).split('.')[0]],
                    package_name
                )
                
            src_files[src_id] =s1;    
                        
        return src_files
