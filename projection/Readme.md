# Description

Dedicated challenge to automate tests for projection.

## Technical data

* __Operating system__: Mac OS
* __Text Editor__: Microsoft Visual Studio Code
* __Design Pattern__: Pytest

## Requirements

* [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
* Libraries
  * pipenv
  * selenium
  * pytest
  * allure-pytest
  * pytest-dependency

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the [pipenv](https://pipenv.pypa.io/en/latest/) module.

```bash
pip install pipenv
pipenv install
```

Allure will be needed for pipenv to run. For mac environments please run:

```bash
brew install allure
```

For other OS please follow the documentation of [allure](https://docs.qameta.io/allure/).

Once the module is installed, proceed to execute the command ```pipenv install``` in a cmd within the project path. This will create the virtual environment and install the other necessary modules on which the project is built.

To create the virtual env, run:

```bash
pipenv shell
```

To run the test, for example:

```bash
pipenv run python3 -m pytest {path of the test}
```

To run only the tests in caden link:

```bash
pipenv run python3 -m pytest Caden/tests/Caden-Link
```

To run the regression:

```bash
pipenv run pytest --alluredir={path of reports folder inside target folder}
```

To execute the report:

```bash
pipenv run allure serve {path of reports folder inside target folder}
```