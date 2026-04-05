Testing RESTful APIs in Python with requests and pytest
==================
This project contains automated checks for a User Management API. It validates core CRUD operations (Create, Read, Update, Delete) and authentication flows (Login, Access Token retrieval). The tests are written in Python using pytest, [requests](https://requests.readthedocs.io/en/latest/), library, and rely on fixtures to manage test data and API interactions.

Features
==================
* User Creation: Ensures new users can be registered successfully.
* Login & Authentication: Validates that users can log in and receive an access token. 
* Get User by ID: Confirms that user details can be retrieved with proper authorization. 
* Full Update: Tests updating user details and verifies persistence. 
* Delete User: Ensures users can be removed from the system. 
* Reusable Fixtures: Provides payloads, created users, and login credentials for consistent test setup.

Setting up your system
==================
1) Make sure you have a working Python 3 installation. Get it from [here](https://www.python.org/downloads/) if you haven't got that already.
2) Download and unzip or clone this project
3) From the project root, run `pip install -r requirements.txt` to install the necessary dependencies
4) Run the tests with `pytest -v` 

What API is used for this project
---
Special thanks to my friend Ahmad Waqar for developing this dummy [CRUD API](https://demo.ahmadwaqar.dev/docs), for learning purposes. Please ensure the API is running and that your machine has permission to access it before use.


Comments? Saying thanks?
---
Feel free to file an issue here or send me an email at kingsleyedemudoh@yahoo.com.

---
