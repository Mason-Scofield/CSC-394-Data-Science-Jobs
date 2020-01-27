# CSC-394-Data-Science-Jobs

Web Application that analyzes Data Sience Positions

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

PyCharm for Intuitive Project management:
```
PyCharm 2019.3.1 (Community Edition)
```

### Installing

In PyCharm:
1. Create New Project: 
	**Assure the Project is running Python 3.6**
	1. Clone Repository:
		1. Navigate to VCS -> Get from Version Control
		2. Assure Version Control is Git
		3. In URL enter: https://github.com/Mason-Scofield/CSC-394-Data-Science-Jobs.git
			- Or through SSH (easier in my opinion) git@github.com:Mason-Scofield/CSC-394-Data-Science-Jobs.git
			- See for collaborators 1.a for more help
		4. Leave deafult directory or add custom path
		5. Click clone

Installing all libraries:
```
pip install -r requirements.txt
```


### For Collaborators:

Assure you are signed in to GitHub:
1. Navigate to File -> Settings -> GitHub
***Assure you have yet generated an SSH key before proceeding***
	1. On a web browser access your GitHub account:
		1. Navigate to Profile -> Settings -> SSH anf GPG Keys and generate new SSH Key
2. Click the plus button on the right and enter credentials

### Run Web App Locally

Within the PyCharm Terminal navigate to the webApp directory:

```
cd webApp
flask FLASK_APP = run.py
flask run
```

If successuful it should output the following:

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

If an error occurs on output be sure you have navigated to the correct directory (ie rootRepo/webApp) when setting the flask app variable and when running locally.

On your prefered browser view the web app locally: 
```
http://127.0.0.1:5000/
```