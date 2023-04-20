# importing the requests library
import requests

# api-endpoint
URL = "https://api.clo.ru/v1/{}"
URL2 = "https://api.clo.ru/v1/{}/{}"
# HEADERS = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'}

def get_project(token):
    # defining a dict of headers to be sent to the API
    url=URL.format('projects')
    headers=    {'Content-Type': 'application/json',
                 'Authorization': 'Bearer {}'.format(token)
                  }
    # sending get request and saving the response as response object
    r = requests.get(url = url, headers = headers)
    #if r.s
    if r.status==200:
        project_id=r.json()['results'][0]['id']
    else:
        project_id=-1
    return project_id

def get_images(token,project_id):
    headers=    {'Content-Type': 'application/json',
                 'Authorization': 'Bearer {}'.format(token)
                  }
    url = URL2.format(project_id,"images")

    # defining a dict of headers to be sent to the API
    headers=HEADERS.format(token)

    # sending get request and saving the response as response object
    r = requests.get(url = url, headers = headers)
    return r.json()
