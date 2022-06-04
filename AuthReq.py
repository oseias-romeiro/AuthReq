import requests
from bs4 import BeautifulSoup

class AuthReq:
    def __init__(self):
        self.sess : requests.Session = requests.session()

    def sessGet(self, url:str) -> requests.Response:
        return self.sess.get(url)

    def sessPost(self, url:str, data: dict) -> requests.Response:
        return self.sess.post(url, data=data)
        
    def login(self, login: str, loginPost: str, payload: dict):
        tokenName: str = list(payload.keys())[0]

        content = self.sessGet(login).content
        soup = BeautifulSoup(content, 'html.parser')

        token = soup.find('input', {'name': tokenName})['value']

        payload[tokenName] = token

        return self.sessPost(loginPost, data=payload)

    def logout(self) -> None:
        self.sess.close()
