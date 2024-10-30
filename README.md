# Python-testing-framework

### To install pytest, playwright, httpx, and more in your virtual environment, you can use the following commands:

**Run the following command to create a virtual environment:**
```Bash
python -m venv python-testing-framework
```

**Activate the Virtual Environment:**
```Bash
python-testing-framework\Scripts\activate
```

**Install Packages:**
```Bash
pip install pytest playwright httpx python-dotenv aiofiles pytest-html jsonschema pytest-asyncio
```

**Install playwright Browsers:**
```Bash
playwright install
```

**Export the installed packages to a requirements.txt file:**
```Bash
pip freeze > requirements.txt
```

**Done? -> Deactivate the Virtual Environment:**
```Bash
deactivate
```

**Install packages from requirements.txt:**
```Bash
pip install -r requirements.txt
```

**To list all virtual environments created using venv or other tools like virtualenv, you can use:**
```Bash
dir /s /b activate
```

# API Testing:

### Setup:
To ensure that your imports work correctly with pytest, you typically need to follow these steps:

1. **Ensure `__init__.py` files are present**: Make sure that each directory in your package has an `__init__.py` file.<br> 
This file can be empty but is necessary for Python to recognize the directory as a package.

    Your directory structure should look like this:
    ```Bash
    python-testing-framework/
    ├── pytest.ini
    ├── tests/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   │
    │   │   ├── core/
    │   │   │   ├── __init__.py
    │   │   │   └── apis_info.py
    │   │   │
    │   │   ├── module_a/
    │   │   │   ├── __init__.py
    │   │   │   ├── conftest.py
    │   │   │   │
    │   │   │   ├── setup/
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── cognito_token.py
    │   │   │   │
    │   │   │   ├── tests/
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── test_get_user.py
    ```
2. **Use relative imports**: to reference modules within the same package.<br> For example, in `test_get_user.py`, you should use:
    ```Python
    from ...core.apis_info import ApiAbbreviation, apiUrls
    ```

3. **Set the `PYTHONPATH` environment variable**: to the root directory of your project to ensure Python can find the modules correctly.<br> This step is necessary if you are running the tests from a different directory.
    ```Bash
    set PYTHONPATH=C:\xxx\xxx\python-testing-framework
    ```

4. **Run pytest from the root directory**: of your project to ensure it can find all the necessary modules and packages.
    ```Bash
    pytest -s tests/api/module_a/tests/test_get_user.py --html=report.html
    ```

---

### Global fixtures:
In pytest, you can create global fixtures by defining them in a file called `conftest.py`.<br>
This file should be located in your project's root directory or in any directory containing tests.<br>
Pytest will automatically discover `conftest.py` files and the fixtures defined in them,<br> 
and these fixtures will be available to all tests in your project/folder.

---

### Hooks:
Are special functions that pytest will automatically call at certain points during the testing process.<br><br>
`def pytest_sessionstart(session):`<br>
This function is a pytest hook that is automatically called once before any tests or test cases are run.

`def pytest_sessionfinish(session, exitstatus):`<br> 
This function is another pytest hook that is automatically called once after all tests and test cases have finished running.<br>
This might be done to clean up after the tests, or to ensure that the token isn't accidentally used outside of the testing session.

The `session` parameter in both `pytest_sessionstart` and `pytest_sessionfinish`<br>
is a Session object that contains information about the testing session, such as the tests that are being run and their status.<br>
The `exitstatus` parameter in `pytest_sessionfinish` is the exit status of the testing session,<br> 
which can be used to determine if the tests passed or failed.

---

### HTML reports:
For generating HTML reports in pytest, the most commonly recommended tool is pytest-html.<br> 
It is a plugin for pytest that generates a detailed HTML report for test sessions.<br> 
This report includes the summary of the test outcomes, categorization of tests (passed, failed, skipped, etc.),<br> 
and can also include additional information like logs, links, and screenshots if configured.

Run pytest with HTML report option: When running pytest, add the `--html` flag followed by the name of the report file you wish to generate.<br> 
This command will execute your tests and generate an HTML report named `report.html` in your current directory.

```Bash
pytest --html=report.html
```

1. **Custom Report Title**: to set a custom title for the HTML report.

```Bash
pytest --html=report.html --html-report-title="My Test Report"
```

2. **Include Environment Section**: To include an environment section in the report, you can use the --metadata option to add each key-value pair.

```Bash
pytest --html=report.html --metadata Browser Firefox --metadata Environment Test
```

You can put many pytest configuration options, including those for pytest-html, into a configuration file so you don't need to enter them every time you run a script.<br>
The most commonly used configuration file for pytest is `pytest.ini`

```Python
[pytest]
addopts =
    --html=report.html
    --metadata Browser Chrome
    --metadata Environment Test
```
<img src="readme_images/report1.html.png"  width="300"/>

(Environment can also be set inside the `conftest.py` file comming from the `.env` file)<br><br>
This configuration will automatically apply the specified options every time you run pytest, generating an HTML report titled "report.html" with the additional metadata and custom CSS specified.

For options that cannot be directly included in the configuration file, like adding extra links or assets through markers or modifying the pytest metadata within a test, you'll need to handle those within your test files or through custom plugins or hooks.

Remember to place the `pytest.ini` file at the root of your project or in a location where pytest can automatically detect it.

#### HTML report configuration for this framework:

`pytest.ini`<br>
Specifies the HTML report output file:
```Python
[pytest]

...

addopts =
    --html=report.html
```

`conftest.py`<br>
Imports the custom HTML summary function:
(You do not need to call it directly; pytest will call it as part of its hook system.)
```Python
from ..core.html_summary import pytest_html_results_summary
```


`html_summary.py`<br>
Contains the custom HTML summary function for the pytest-html plugin.<br> This function adds environment information to the HTML report in a styled table format.
```Python
import os

def pytest_html_results_summary(prefix, summary, postfix):
    environment = os.getenv("ENVIRONMENT")
    
    # Create a table with environment information using raw HTML and CSS
    table_html = """
    <style>
        .summary-table {{
            width: 20%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 11px;
            text-align: left;
        }}
        .summary-table th, .summary-table td {{
            padding: 12px 15px;
            border: 1px solid #ddd;
        }}
        .summary-table th {{
            background-color: #f2f2f2;
        }}
    </style>
    <table class="summary-table">
        <tr>
            <th>Key</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Environment</td>
            <td>{}</td>
        </tr>
    </table>
    """.format(environment)
    
    # Add custom content to prefix
    prefix.extend(["Test Execution Summary"])
    
    # Add the table to the summary
    summary.extend([table_html])
    
    # Add custom content to postfix
    postfix.extend(["End of Summary"])
```
<img src="readme_images/report2.html.png"  width="300"/>

---

### Logging 

The logging configuration is set up using a JSON file and a setup script.<br>
This configuration ensures that logs are written to both the console and a file, and are also captured for inclusion in the HTML report.<br>

`logging_config.json`
```Python
{
    "version": 1,
    "disable_existing_loggers": true,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "standard",
            "filename": "api_logging.log",
            "mode": "a",
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["console", "file"]
        }
    }
}
```
`loggingSetup.py`
```Python
import logging
import logging.config
import json
import os

def setup_logging():
    #Setup logging configuration
    path = os.path.join(os.path.dirname(__file__), 'logging_config.json')
    
    with open(path, 'r') as f:
        config = json.load(f) # Load the logging configuration from the JSON file
    
    # Dynamically set the absolute path for the .log file
    log_file_path = os.path.join(os.path.dirname(__file__), 'api_logging.log')
    
    # Clear the log file before adding new logs
    with open(log_file_path, 'w'):
        pass
    
    config['handlers']['file']['filename'] = log_file_path
    
    # Configure logging using the dictionary loaded from the JSON file
    logging.config.dictConfig(config) 
```

`conftest.py`<br>
In the **tests/api/module_a** directory contains fixtures and hooks for the test session.<br>
It includes environment variable loading, asynchronous setup and teardown, logging setup, and custom HTML summary configuration.

```Python
from ..core.loggingSetup import setup_logging 

# Setup logging configuration
setup_logging()

...

```

`html_summary.py`<br>
In the **tests/api/core** directory contains the custom HTML summary function for the pytest-html plugin.<br>
This function captures log output and adds it to the HTML report.

```Python
...

def pytest_html_results_table_row(report, cells):
    if report.when == 'call':
        # Add captured log output to the HTML report
        log_output = "\n".join(report.caplog)
        cells.append(html.div(log_output, class_='log'))

...
```

`test_get_user.py`<br>
The test uses the logger to log messages, which are captured by the caplog fixture and included in the HTML report.
```Python
import logging

# Configure the logger
logger = logging.getLogger(__name__)

...
```


