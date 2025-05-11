import requests

from models import User



class UserService:
    def __init__(self, url:str='https://jsonplaceholder.typicode.com/users', user_id: int = 1):
        self.url: str = url
        self.user: User = None
        self.user_id:int = user_id 




        self.get_user(user_id)
    

    def get_user (self, user_id: int):
        response = requests.get(f'{self.url}/{user_id}')
        if response.status_code == 200:
            data = response.json()
            if 'name'in data and 'username' in data and 'email' in data:
                self.user = User(name=data['name'], username=data['username'], email=data['email'])
        else:
            self.user = None




