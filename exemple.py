from AuthReq import AuthReq

ar = AuthReq()

login = 'https://exemple.com'
loginPost = 'https://exemple.com/login'
payload = {'token': None, 'username': 'admin', 'password': 'admin'}

res = ar.login(login, loginPost, payload)

print(res.status_code)

print(ar.sessGet('https://google.com').status_code)
print(ar.sess.get('https://google.com').status_code)
