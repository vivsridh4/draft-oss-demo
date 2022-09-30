from flask import Flask
import tweepy
from decouple import config
import requests

app = Flask(__name__)

#update
@app.route('/')
def hello_world():
    
    import requests
    response = requests.get("https://vicky007.azurewebsites.net/api/vicky?name=Draft v2 on K8s demo")
    print(response) 
    return "Samosa at #OSI2022\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)