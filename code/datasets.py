from collections import namedtuple
from pathlib import Path

# Dataset root directory
_DATASET_ROOT = Path('/content/drive/MyDrive/MehdiLamouchi_SE_Project/data')

Dataset = namedtuple('Dataset', ['name', 'root', 'src', 'bug_repo'])

certbot=Dataset(
  'certbot-master',
  _DATASET_ROOT / 'certbot-master',
  _DATASET_ROOT /'certbot-master/certbot-master',
  _DATASET_ROOT /'certbot-master/certbot.json'
)

compose=Dataset(
  'compose-master',
  _DATASET_ROOT / 'compose-master',
  _DATASET_ROOT /'compose-master/compose-master',
  _DATASET_ROOT /'compose-master/compose.json'
)

django=Dataset(
  'django-rest-framework-master',
  _DATASET_ROOT / 'django-rest-framework-master',
  _DATASET_ROOT /'django-rest-framework-master/django-rest-framework-master',
  _DATASET_ROOT /'django-rest-framework-master/django_rest_framework.json'
)

keras=Dataset(
  'keras-master',
  _DATASET_ROOT / 'keras-master',
  _DATASET_ROOT /'keras-master/keras-master',
  _DATASET_ROOT /'keras-master/keras.json'
)

requests=Dataset(
  'requests-master',
  _DATASET_ROOT / 'requests-master',
  _DATASET_ROOT /'requests-master/requests-master',
  _DATASET_ROOT /'requests-master/requests.json'
)
scikit=Dataset(
  'scikit-learn-master',
  _DATASET_ROOT / 'scikit-learn-master',
  _DATASET_ROOT /'scikit-learn-master/scikit-learn-master',
  _DATASET_ROOT /'scikit-learn-master/scikit-learn.json'
)
scrapy=Dataset(
  'scrapy-master',
  _DATASET_ROOT / 'scrapy-master',
  _DATASET_ROOT /'scrapy-master/scrapy-master',
  _DATASET_ROOT /'scrapy-master/scrapy.json'
)
spaCy=Dataset(
  'spaCy-master',
  _DATASET_ROOT / 'spaCy-master',
  _DATASET_ROOT /'spaCy-master/spaCy-master',
  _DATASET_ROOT /'spaCy-master/spaCy.json'
)

tornado=Dataset(
  'tornado-master',
  _DATASET_ROOT / 'tornado-master',
  _DATASET_ROOT /'tornado-master/tornado-master',
  _DATASET_ROOT /'tornado-master/tornado.json'
)
### change this name to change the dataset
DATASET = tornado