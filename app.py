import os
import time

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from azure.storage.blob import BlobServiceClient

from datetime import datetime

app = Flask(__name__)

storage_account_key = "oGGBil47vhK+ElVNNQIWnXYcQ1LloABCXZNSJe1sYOfaN0UuJVDQFEt9m1N+GnHEAB5J2Dp61bhQ+AStI4ncDg=="
storage_account_name = "hackxstorage"
connection_string = "DefaultEndpointsProtocol=https;AccountName=hackxstorage;AccountKey=oGGBil47vhK+ElVNNQIWnXYcQ1LloABCXZNSJe1sYOfaN0UuJVDQFEt9m1N+GnHEAB5J2Dp61bhQ+AStI4ncDg==;EndpointSuffix=core.windows.net"
container_name = "pictures"

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/upload', methods=['POST'])

def uploadToBlobStorage():
   file = request.files['myFile']
   uniqueFileName = datetime.now().strftime("%H:%M:%S") + file.filename
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container = container_name, blob = uniqueFileName)
   with file.stream as data:
    blob_client.upload_blob(data = data)

    time.sleep(1.5)

   return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)
