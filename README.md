# Airflow
Testing how Airflow works

Used New York Times API of top stories
https://developer.nytimes.com/docs/top-stories-product/1/overview

Created DAG to run the code everyday to fetch NYT Top Stories.

How to run-
Open terminal, go to folder with code files and run below command,

docker-compose up

(Make sure Postgres is running).

Once it completes, open browser and go to localhost:8080 and you will get the DAG UI.
Select the DAG and hit Start.
