# ApiTestingWithPython

### **Setup:**

Install pip to get the required packages mentioned below. The link provided gives the required steps to download/install pip https://packaging.python.org/installing/

Install python on windows: https://www.python.org/downloads/windows/

**Personal System config:**
OS: Ubuntu 18.04  
Python 3.7  
IDE: Pycharm  
Unit testing framework: Pytest  
Reporting: Allure  
SCM: Git

**Libraries Used**
requests==2.23.0  
jsonschema==3.2.0  
allure-pytest==2.8.13  
openpyxl==3.0.3  
psycopg2==2.8.4  
pytest==5.4.1  
xlrd==1.2.0

Save all the libraries in a requirements.txt and use pip3 install -r requirements.txt (Python 3).  Install allure-cli. Download last version of allure-cli. Allure-cli requires java.
Allure-cli doesn't require installation, just unpack and add to your path and use it.

Once the system is set, to run the test cases with allure reports:
1. Open terminal/cmd/ide and make sure the path is set to /ApiTesting/Reports/mainHTMLReport [Where human readable HTML report will be generated].
2. Run command -> "pytest --alluredir Reports/jsonReport/ TestCases/". This will execute all the test cases file present in the TestCases directory.
3. In the jsonReport folder, multiple files will be generated in .json and .txt format.
4. Run command -> "run command: allure generate /ApiTesting/Reports/jsonReport" [path to json reports].
5. In the mainHTMLReport, a directory "allure-report" should be present.
6. Open index.html in browser.

**Note:** Some how the unit testing framework 'pytest' used in this project is not supporting the use of relative path. 
Anyone forking or branching this repo should provide the absolute path of any resource (such as excel file) used in the test cases.
Did some exploration over the same but did not understand the issue. As soon as a solution is found, it will be shared.

Currently using pycharm ide to run the test cases. Any python supporting IDE has to be installed and the code has to be cloned into it in order to run/edit the test cases manually.  
