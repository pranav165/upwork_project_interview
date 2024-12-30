# upwork_project_interview

This is a Selenium Page Object Modal framework for automating web application.
The framework also supports multiple browser / performance metrics when enabeled from settings.py

How to run

1) Create a virtual enviornment using python -m pip install virtualenv
2) Activate the virtual env
3) Install dependencies - pip install -r requirements.txt
4) Run the test script using python main.py
5) Enter the browser choice 1-Chrome , 2-Firefox
6) Logs will be printed on console for debugging

When PEROFRMANCE=True  - Performance metrics will also be logged in the console logs

Following Test Scenario is automated for demo purpose

"""
Sample Test Scenario

1) Navigate to - http://cloudtwo.cloud-vms.com/customer/alerts
2) Login with Valid Credentials
3) Navigate to Alerts
4) Filter table by site name - Toronto
5) Click on Review
6) Validate GPT response status is True
"""


This will further be enhanced and converted to a Pytest test along with HTML Reporting.
