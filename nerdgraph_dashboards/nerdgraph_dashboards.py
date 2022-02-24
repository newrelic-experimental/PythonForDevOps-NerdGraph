import requests
import json
from license import user_key

def nerdgraph_dashboards(key):
  # GraphQL query to NerdGraph
  query = """mutation { dashboardCreateSnapshotUrl(guid: "XXX") }"""
  
  # NerdGraph endpoint
  endpoint = "https://api.newrelic.com/graphql"
  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    # convert a JSON into an equivalent python dictionary
    json_dictionary = json.loads(response.content)
    print(json_dictionary)

    # only interested with the dashboard url
    url_pdf = json_dictionary["data"]["dashboardCreateSnapshotUrl"]
    print(url_pdf)

    # replace PDF with PNG, and get the link to download the file
    url_png = url_pdf[:-3] + "PNG"
    print(url_png)

    # rename the downloaded file, and save it in the working directory
    dashboard_response = requests.get(url_png, stream=True)
    open('dashboard_example.png', 'wb').write(dashboard_response.content)

    # optional - serialize object as a JSON formatted stream
    # json_response = json.dumps(response.json()["data"]["dashboardCreateSnapshotUrl"], indent=2)
    # print(json_response)

  else:
      # raise an error with a HTTP response code
      raise Exception(f'Nerdgraph query failed with a {response.status_code}.')

nerdgraph_dashboards(user_key)