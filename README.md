# EBI02150 – Technical task

## Running the project locally with docker

- Clone the project to your local machine or download the zip file: ```git clone https://github.com/lightcodes845/legendary-octo-doodle.git```
- Navigate to the project directory: ```cd legendary-octo-doodle```
- If you have docker run the following command
```docker-compose up```
- The command above will:
  - create a mysql database container
  - create a database table
  - run database migrations
  - seed the database with the sql file
  - run the tests
  - run the python application
- Ensure that you allow docker to build the images, create and start all containers before your proceed to the next step. You should see some text similar to the text block below to know the server is up and running.
```
genes_test-web-1      | Starting server
genes_test-web-1      | [] [22] [INFO] Starting gunicorn 21.2.0
genes_test-web-1      | [] [22] [INFO] Listening at: http://0.0.0.0:8000 (22)
genes_test-web-1      | [] [22] [INFO] Using worker: sync
genes_test-web-1      | [] [23] [INFO] Booting worker with pid: 23
```
- Test the api endpoint using the following links:
  - [http://127.0.0.1:8000/api/genequery/?gene_symbol=JAG1](http://127.0.0.1:8000/api/genequery/?gene_symbol=JAG1)
  - [http://127.0.0.1:8000/api/genequery/?gene_symbol=ACE2](http://127.0.0.1:8000/api/genequery/?gene_symbol=ACE2)
- When done testing, to remove all data, containers, volumes, images created by the docker command use the following command:
```docker-compose down -v --rmi all```
- That's it. Thank you!

##If you do not have docker use the following steps below you do not need to have mysql db installed as I have created and seeded a database on AWS for the test.

## Running the project locally without docker

- Clone the project to your local machine or download the zip file.
- Navigate to the project directory: ```cd legendary-octo-doodle```
- Install virtualenv
```pip install virtualenv```
- Create a virtual environment
```virtualenv appenv```
- Specify which python to be used incase you have python2 and python3
```virtualenv -p /usr/bin/python3 appenv```
- Activate the virtual environment
```source appenv/bin/activate```
- Install dependencies of the application
```pip install -r requirements.txt```
- Run the tests using the following command
```pytest```
- Run the server with the following command:
```gunicorn genes_test.wsgi:application --bind 0.0.0.0:8000```
- You should see something like the below.
```
genes_test-web-1      | Starting server
genes_test-web-1      | [] [22] [INFO] Starting gunicorn 21.2.0
genes_test-web-1      | [] [22] [INFO] Listening at: http://0.0.0.0:8000 (22)
genes_test-web-1      | [] [22] [INFO] Using worker: sync
genes_test-web-1      | [] [23] [INFO] Booting worker with pid: 23
```
- Test the api endpoint using the following links:
  - [http://127.0.0.1:8000/api/genequery/?gene_symbol=JAG1](http://127.0.0.1:8000/api/genequery/?gene_symbol=JAG1)
  - [http://127.0.0.1:8000/api/genequery/?gene_symbol=ACE2](http://127.0.0.1:8000/api/genequery/?gene_symbol=ACE2)
- To deactivate the virtual environment use ```deactivate```
- That's it. Thank you!
