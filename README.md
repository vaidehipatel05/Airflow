# Airflow
Testing how Airflow works

Used New York Times API of top stories
https://developer.nytimes.com/docs/top-stories-product/1/overview

Created DAG to run the code everyday to fetch NYT Top Stories.


This Python script performs an ETL (Extract, Transform, Load) process using the New York Times (NYT) API and stores data in CSV.

1. Imported Libraries:
   - `requests`: Used for making HTTP requests to the NYT API.
   - `pandas`: Used for data manipulation and creating a DataFrame.
   - `datetime`: Used for handling dates.

2. Function Definition:
   - `run_nyt_etl()`: This function makes a request to the NYT API for the top science stories. It then processes the JSON response, extracts relevant information for each article, creates a list of refined articles, converts it into a Pandas DataFrame, saves the DataFrame to a CSV file, and prints the DataFrame.

3. NYT API Request:
   - The script constructs the NYT API request URL with the provided API key and queries for top science stories.
   - It uses the `requests.get` method to make the API request.

4. Data Processing:
   - If the API request is successful (status code 200), the JSON response is processed.
   - The script extracts relevant information for each article (title, abstract, URL, published date) and creates a list of refined articles.

The API URL is set to query the top science stories.





How to run-
Open terminal, go to folder with code files and run below command,

docker-compose up

(Make sure Postgres is running).

Once it completes, open browser and go to localhost:8080 and you will get the DAG UI.
Select the DAG and hit Start.
