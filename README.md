# Testing Web Template PY

This project contains a template for mobile test automation.

## Project technologies

The project is developed with the **Python** programming language and the **Selenium** mobile automation framework.

- Python 3.11.6

- Selenium 2.1.3

- PIP 23.3.1

The following are the dependencies of the project:

| Dependency | Version |
|--|--|
| Allure Behave | 2.13.2 |
| Allure Python Commons | 2.13.2 |
| Behave | 1.2.6 |
| Selenium | 4.15.2 |

## Project structure

```
testing-web-template
│ behave.ini
│ run.sh
│ requirements.txt  
└─features
| | _*.feature
| | environment.py
| └─pages
| | | base_page.py
| | | home_page.py
| | | login_page.py
| | | users_page.py
| └─steps
|   | base_steps.py
|   | click_steps.py
|   | compound_steps.py
|   | validation_steps.py
└─utils
| | mobile_capabilities.py

```

## Setting up the project before execution

The **mobile_capabilities.py** file located in the **/utils** path must be modified, adding the capabilities for each device used for testing.

```
ios-simulator: {
  "platformName": "iOS",
  "platformVersion": "16.1",
  "automationName": "XCUITest",
  "deviceName": "iPhone 14"
}

ios-real: {
  "platformName": "iOS",
  "platformVersion": "15.4",
  "automationName": "XCUITest",
  "deviceName": "iPhone XS Max",
  "udid": "XXXXXXXX-XXXXXXXXXXXXXXXX",
  "xcodeOrgId": "XXXXXXXXXX",
  "xcodeSigningId": "iPhone Developer"
}

android-simulator: {
  "platformName": "Android",
  "appium:avd": "Android_8",
  "automationName": "UiAutomator2",
  "appium:deviceName": "Android_8"
}

android-real: {
  "platformName": "Android",
  "automationName": "UiAutomator2",
  "appium:deviceName": "XXXXXXXXX"
}
```

## Executing the project

The project is executed by running the **run.sh** file in Terminal.

`> /run.sh`

Or by running the following command in Terminal

`behave -f allure -o ./reports/report/ ./features/`

## Generating report

By default, the allure report folder will be generated in the ```ROOT_DIR/reports/report``` path.

If you want to change the report path, modify the ```./reports/report``` line in the ```run.sh``` file or the ```behave command```.
