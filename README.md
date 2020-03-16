# CSC-394-Data-Science-Jobs

Web Application that analyzes Data Science Positions

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Must have an AWS DynamoDB set up (Free Tier works great!)

Things you need to install the software and how to install them:

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
			- Or through SSH (easier in my opinion) git@github.com:Mason-gtScofield/CSC-394-Data-Science-Jobs.git
			- See for collaborators 1.a for more help
		4. Leave default directory or add custom path
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

Within the PyCharm Terminal, remain in the repo root directory:
Set environment variables to reflect your AWS Private and public keys
Match DB region to yours in webApp/webScraper/DataBase/__init__.py

```
set AWS_PUB=<yourpublickey>
set AWS_PRIV=<yourprivatekey>
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```
*The FLASK_ENV variable is used for debugging the app*

Or input them manually in PyCharm (Works Best):
1. Navigate and open run.py in the editor:
2. In the top right drop down ensure the script path is set to run.py
3. Within the drop down navigate to Edit Configurations -> Environment -> Environment Variables
4. Click the '$' icon
5. In the pop up window click the '+' sign in the upper right section to add the variables
    -Both AWS_PUB and AWS_PRIV
    -Must be set as typed above see use case in webApp/webScraper/DataBase/__init__.py
    -Ensure region properly reflects your DB region
6. Click OK, then click Apply
7. Close the window and run the app by clicking the Green 'Play' button next to the 'RUN' drop down


If successful it should output the following:

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

If an error occurs on output be sure you have remained in the root directory (ie clonedRepo/) when setting the flask app variable and when running locally.

On your preferred browser view the web app locally: 

```
http://127.0.0.1:5000/
```

You can deploy directly to a Heroku Server by creating a Free Tier account and linking your cloned repository
*You must set up environment variables within the Settings to set up your Public and Local keys*
