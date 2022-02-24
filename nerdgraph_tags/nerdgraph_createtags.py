import requests
import json
from license import user_key

def nerdgraph_createtags(key):
  # GraphQL query to NerdGraph
  query = """
  mutation {
    taggingAddTagsToEntity(
        guid: "XXX",
        tags: [
          	{ key: "env", values: ["prod"]}, 
          	{ key: "cloud", values: ["AWS", "ap-southeast"]},
            { key: "team", values: ["web", "content", "frontend"]}
        		]) {
            errors {
                message
            }
        }
  }"""

  # NerdGraph endpoint 
  endpoint = "https://api.newrelic.com/graphql"
  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})
  
  if response.status_code == 200: 
    # convert a JSON into an equivalent python dictionary
    dict_response = json.loads(response.content)
    print(dict_response)

    # optional - serialize object as a JSON formatted stream 
    # json_response = json.dumps(response.json(), indent=2)
    # print(json_response)
  else:
    # raise an exepction with a HTTP response code, if there is an error
    raise Exception(f'Nerdgraph query failed with a {response.status_code}.')

nerdgraph_createtags(user_key)