#!/usr/bin/env python
import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure Database URI: 
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=databasehackx.database.windows.net;DATABASE=pythonSQL;UID=CloudSAc66b69ee;PWD=KriksisPuksis123!")

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
db = SQLAlchemy(app)