from . import test_TC1_GetRequest
from . import test_TC2_PostRequest
from . import test_TC3_PutRequest
from . import test_TC4_DeleteResquest

import requests
import json
import jsonschema
from jsonschema import Draft7Validator
import jsonpath
from Library import ExcelOperations
import pytest