# Rest api testing. verify response headers, status, and schema
import pytest
import requests
import json
import jsonschema
from jsonschema import Draft7Validator
import jsonpath

from Library import ExcelOperations

baseURL = "https://reqres.in/"
postRequest_URI = "api/users/"

URL = baseURL + postRequest_URI


@pytest.fixture()
def beforeTest():
    global obj
    global f
    obj = ExcelOperations.excelUtility('/home/deadpool/PycharmProjects/ApiTesting/TestData/testData.xlsx', 'get')
    f = open("/home/deadpool/PycharmProjects/ApiTesting/Schemas/getRequestJsonSchema.json", "r")           #open file in read mode


def test_getRequest(beforeTest):
    col = obj.get_col_count()
    row = obj.get_row_count()

    SchemaSkeleton = f.read()                           #reads file in string format
    jsonSchemaSkeleton = json.loads(SchemaSkeleton)

    for i in range(2, row+1):               #exclude header
        resourceID = obj.getResourceID(i)
        request_URL= URL + str(resourceID)

        response = requests.get(URL)
        if (response.status_code == 404):
            print("Resource you are trying to fetch does not exist")
            continue
        else:
#           convert response into json
            json_response = json.loads(response.text)
            contentType = response.headers.get('Content-Type')
            assert contentType == 'application/json; charset=utf-8'

            #--------------- Schema Validation ------------------
            validator = Draft7Validator(schema=jsonSchemaSkeleton)
            # validator.validate(json_response)                         # breaks only for failures

            errors = sorted(validator.iter_errors(json_response), key=lambda e: e.path)

            if len(errors) == 0:
                print("No Validation Error")
            else:
                print("Validation error occured: ")
                for error in errors:
                    print(error.message)
