# # Selenium Pytest Framework
#
# This is an automation testing framework developed using:
#
# - Selenium WebDriver
# - Pytest
# - Python
#
# ## Project Structure
#
# - tests → Test cases
# - pages → Page Object Model files
# - utils → Utility files
# - reports → HTML reports
# - screenshots → Failure screenshots
# - test_data → Test data files
#
# ## Website Used
#
# https://www.saucedemo.com/
#
# ## Features
#
# - Page Object Model (POM)
# - Pytest Fixtures
# - HTML Reports
# - Reusable Code Structure
#
# ## Run Tests
#
# pytest
#
# ## Generate Report
#
# pytest --html=reports/report.html
#
# [pytest]
#
# addopts = -v -s --html=./reports/report.html
#
# python_files = test_*.py
#
# python_classes = Test*
#
# python_functions = test_*
#
# markers =
#     smoke: smoke test cases
#     regression: regression test cases
#     sanity: sanity test cases