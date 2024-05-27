# Programmadi.exe - gen_ai_querybot

## Problem Statement:
Develop a query bot capable of interpreting user queries and utilizing Dataportal knowledge to generate SQL queries.


## Approach:
<img width="723" alt="image" src="https://media.git.target.com/user/20727/files/7af0ebca-e1bc-4669-aac6-d402f5c1e6b5">


### Data processing:
 - Processing all the certified and active tables with it's attributes and descriptions as a dictionary with asset/table name as keys and description as values
 - Saved data to ./data/tablename_vs_data.pkl
 - Using mixtral-8x7b-instruct-v0.1 model to summarize tables and their attribute descriptions and creating dictionary with asset/table name as key and concise description as value
 - Saved data to ./data/mixtral_summarized_descriptions.pkl
 
### Create Embedding:
- Generating the Embedding for all the assets/tables and their concise decriptions using Sentence bert framework
- Saved embeddings at ./data/description_embeddings.pkl
 
### Process the content:
- Given the user query getting the top 10 tables based cosine similarity of embeddings
- Using the comple decriptions of these top 10 tables as context 
- Pass this processed context along with user query

### Get response through Thinktank api:
- Using mixtral-8x7b-instruct-v0.1 model for api calls
- Passing the processed content and the user query to get response

### Validation:
- Extracting SQL query from the response.
- Validating the query by running it on hive using subprocess.
- If query fails sending the error message back to api
