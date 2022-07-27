import requests




#res = requests.get("http://127.0.0.1:3000/api/courses/2")

res = requests.post("http://127.0.0.1:3000/api/courses/2", json={"login": "test_login2", "password": 'test_password2'})
#print(res.json())
print(res.json())
