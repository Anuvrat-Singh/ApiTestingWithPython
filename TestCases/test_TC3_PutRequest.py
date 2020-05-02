    # Rest api testing. verify response headers, status, and schema
import pytest
import requests
import json
import jsonschema
from jsonschema import Draft7Validator
import jsonpath
from Library import ExcelOperations

baseURL = "https://reqres.in/"
postRequest_URI = "api/users/2"
URL = baseURL + postRequest_URI

@pytest.fixture()
def beforeTest():
    global inputFile
    global obj
    global f
    inputFile = open('/home/deadpool/PycharmProjects/ApiTesting/inputJsons/updateResource.json', 'r')
    obj = ExcelOperations.excelUtility('/home/deadpool/PycharmProjects/ApiTesting/TestData/testData.xlsx', 'update')
    f = open('/home/deadpool/PycharmProjects/ApiTesting/Schemas/updateRequestJsonSchema.json', 'r')


def test_putRequest_Positive(beforeTest):
    input_json = json.loads(inputFile.read())

    col = obj.get_col_count()
    row = obj.get_row_count()
    keyList = obj.get_keyNames()

    schemaSkeleton = f.read()
    jsonSchemaSkeleton = json.loads(schemaSkeleton)

    for i in range(2, row+1):               #exclude header
        request_json= obj.update_json_with_data(i, input_json, keyList)
        response = requests.put(URL, request_json)
        print(response)

        assert response.status_code == 200
        print(response.content)
        contentType = response.headers.get('Content-Type')

        assert contentType == 'application/json; charset=utf-8'
        response_json = json.loads(response.text)
        updatedAt = response_json['updatedAt']         #jsonpath returns list
        print(updatedAt)
        #--------------- Schema Validation -----------------
        validator = Draft7Validator(schema=jsonSchemaSkeleton)
        errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)

        if len(errors) == 0:
            print("No Validation Error")
        else:
            print("Validation error occured: ")
            for error in errors:
                print(error.message)

def test_putRequest_Negative(beforeTest):
    input_json = json.loads(inputFile.read())

    col = obj.get_col_count()
    row = obj.get_row_count()
    keyList = obj.get_keyNames()

    schemaSkeleton = f.read()
    jsonSchemaSkeleton = json.loads(schemaSkeleton)

    for i in range(2, row+1):               #exclude header
        request_json= obj.update_json_with_data(i, input_json, keyList)
        response = requests.put(URL, request_json)
        print(response)

        assert response.status_code != 2000
        print(response.content)
        contentType = response.headers.get('Content-Type')

        assert contentType == 'application/json; charset=utf-8'
        response_json = json.loads(response.text)
        updatedAt = response_json['updatedAt']
        print(updatedAt)
        #--------------- Schema Validation -----------------
        validator = Draft7Validator(schema=jsonSchemaSkeleton)
        errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)

        if len(errors) == 0:
            print("No Validation Error")
        else:
            print("Validation error occured: ")
            for error in errors:
                print(error.message)
