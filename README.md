# risksek
assignment

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]

<!-- ABOUT THE PROJECT -->
## About The Project
To get the github organization
### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [pytest](https://docs.pytest.org/en/6.2.x/warnings.html)
* [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html)

### project structure
- Db schema is available in database folder
- Swagger is availabe in static folder
- Unit test written in tests package
- .env file need to create for environment variable.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* python
  ```sh
   https://www.python.org/downloads/release/python-365/
  ```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rajeevhcu/risksek
   ```
2. Create Virtual environment
   ```sh
   virtualenv -p python3 venv
   ```
   
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
3. Install required packages
    ```sh
   pip3 install -r requirements.txt
   ```
   
  
5. Create .env
   ```sh
    MYSQL_USER_ID = <user_id>
    MYSQL_PASSWORD = <password>
    MYSQL_HOST = <host>
    MYSQL_DATABASE = <db_name>
   ```
  
6. To run locally
   ```sh
    python3 wsgi.py
   ```
7. To run unittest
    ```
       pytest
    ```
8. To generate code coverage report
    ```
       coverage run -m pytest 
    ```
9. To show coverage report in terminal
    ```
       coverage report -m
    ```
