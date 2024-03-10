import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

# def login(username, password):
#     response = requests.post(data['website1', username, password])
#     if response.status_code == 200:
#         return response.json()['token']
#         # print(response.json()['token'])
#
# def get_post(token):
#     response = requests.get(data['website2'], headers={'X-Auth-Token': token}, params={"owner": "notMe"})
#     if response.status_code == 200:
#         return response.json()

####################################################################
def login():
    response = requests.post(data['website1'], data={'username': data['username'], 'password': data['password']})
    if response.status_code == 200:
        return response.json()['token']

def get_post(token):
    response = requests.get(data['website2'], headers={'X-Auth-Token': token}, params={"owner": "notMe"})
    if response.status_code == 200:
        return response.json()
####################################################################
def get_title(inform):
    inform = get_post(login())['data'][1]['title']
    return inform

def post_post(token):
    response = requests.get(data['website2'], headers={'X-Auth-Token': token},
                            params={"owner": "Me", 'title': 'my_new_post', 'description': 'test_text', 'content': 'some_text'})
    if response.status_code == 200:
        return response.json()

def check_title(info):
    inform = post_post(login())['data'][1]['title']
    return info


if __name__ == '__main__':
    print(get_post(login()))
    print(post_post(login()))

