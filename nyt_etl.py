import requests
import pandas as pd
from datetime import datetime
#import s3fs 
import boto3
from botocore.exceptions import NoCredentialsError
from io import StringIO 

def run_nyt_etl():

    # Replace 'your_api_key' with your actual New York Times API key
    api_key = ''
    api_url = 'https://api.nytimes.com/svc/topstories/v2/science.json'

    params = {
        'api-key': api_key,
    }
    # Make the API request
    response = requests.get(api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        if data.get('status') == 'OK':

            results = (data)
            articles = results.get('results', [])

            list_of_articles = []
            for article in articles:
                refined_article = {
                    #'section': article.get("section", ""),
                    'title': article.get("title", ""),
                    'abstract': article.get("abstract", ""),
                    'url': article.get("url", ""),
                    'published_date': article.get("published_date", "")
                    #'image_url': article.get("multimedia", [{}])[0].get("url", ""),  # Assuming there may be multiple multimedia entries
                }
                list_of_articles.append(refined_article)

            # Convert the list of articles to a DataFrame
            df = pd.DataFrame(list_of_articles)

            # Save DataFrame to CSV in-memory
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            
            # Upload CSV buffer to AWS S3
            upload_to_s3(csv_buffer.getvalue(), 'airflow-nyt', 'refined_articles.csv')

        else:
            print(f"API returned an error: {data.get('status')}")

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")


def upload_to_s3(csv_data, bucket_name='airflow-nyt', object_name='refined_articles.csv'):

    s3 = boto3.client('s3')

    try:
        s3.put_object(Body=csv_data, Bucket=bucket_name, Key=object_name)
        print(f"CSV data uploaded to {bucket_name}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available or incorrect")
