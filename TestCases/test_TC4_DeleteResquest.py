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
    obj = ExcelOperations.excelUtility('/home/deadpool/PycharmProjects/ApiTesting/TestData/testData.xlsx', 'delete')

def test_deleteRequest(beforeTest):
    col = obj.get_col_count()
    row = obj.get_row_count()

    for i in range(2, row+1):               #exclude header
        resourceID = obj.getResourceID(i)
        request_URL= URL + str(resourceID)
        # reqHeaders = {'Authorization': 'Bearer ----delete should be authorized and hence here should be your token',
        #            'Content-Type': '*/*'}
        # response = requests.delete(url= URL, headers= reqHeaders)
        # above snippet to be used in case we need to pass headers to request
        response = requests.delete(request_URL)
        print(response)
        assert response.status_code == 204

# Test data contains negative resource ids as well. But since the api doesnt give any validation error, test passed.