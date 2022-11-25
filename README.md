## Quick start
### 1) Run docker
```docker run -p 8091:8091 -it azshoo/alaska:1.0```
### 2) Install project requirements
```pip install -r requirements.txt```

List of requirements:
```
allure-pytest==2.12.0
allure-python-commons==2.12.0
attrs==22.1.0
certifi==2022.9.24
charset-normalizer==2.1.1
colorama==0.4.6
exceptiongroup==1.0.4
idna==3.4
importlib-metadata==5.0.0
importlib-resources==5.10.0
iniconfig==1.1.1
jsonschema==4.17.0
packaging==21.3
pkgutil-resolve-name==1.3.10
pluggy==1.0.0
pyparsing==3.0.9
pyrsistent==0.19.2
pytest==7.2.0
requests==2.28.1
six==1.16.0
tomli==2.0.1
typing-extensions==4.4.0
urllib3==1.26.12
zipp==3.10.0
```

## Test-Cases
* [MS Word document](https://github.com/EPoleshchuk/bear_test_task/blob/master/TestCases.docx)
* [PDF document](https://github.com/EPoleshchuk/bear_test_task/blob/master/TestCases.pdf)

## Run tests
To run test execute command: ```pytest --alluredir {allure_dir}```  
To generate allure report execute command: ```allure serve {allure_dir}```
