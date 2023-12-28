# Python API Automation Framework

Hybrid Custom Framework to test REST APIs

### Tech Stack
1. Python 3.10
2. Request - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest-HTML 
5. Test DATA - CSV, Excel, JSON
6. Parallel Execution - x distribute

 
### How to install the packages
````pip install requests pytest pytest-html faker allure-pytest jsonschema

### To freeze your package version
````pip freeze > requirements.txt

### To install the freeze version
````pip install -r requirements.txt

### To run test cases parellel
````pip install pytest-xdist
samples
````pytest -n auto filepath leads to .py file
````pytest -n auto .\tests\parallel\test_parallel_testCases.py

### To work with Excel file
````pip install openpyxl

### To work with Json Schema
``pip install jsonschema``

