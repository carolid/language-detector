import requests

r = requests.post("http://localhost:3000/post", data={'languageString': 'bonjour'})
print(r.text)