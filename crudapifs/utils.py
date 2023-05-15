import requests


def get_posts():
    # url = 'http://localhost:3000/posts'
    url = 'http://192.168.0.3:7303/web/services/TAB_ListGastos/TAB_ListGastos'
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('No hay data')
        return None
