import os
from license import user_key

def nerdgraph_curl(key):
  # GraphQL query to NerdGraph
  query = """{"query": "{ requestContext { userId } }"}"""

  # NerdGraph endpoint
  endpoint = "https://api.newrelic.com/graphql"
  content_type = "Content-Type: application/json"

  # curl request to NerdGraph
  return os.system(f'curl -X POST {endpoint} -H \'{content_type}\' -H \'API-Key: {key}\' -d \'{query}\'')

nerdgraph_curl(user_key)