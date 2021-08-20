from flask import Flask
from os import environ

from dotenv import load_dotenv
from requests import get

load_dotenv()

app = Flask(__name__)

@app.route("/", defaults={"path": "client/build/index.html"})
@app.route("/client/build/<path:path>")
def getApp(path):
    if environ.get('HOT_RELOAD'):
        print('http://localhost:3000/client/build/' + path)
        return proxy('http://localhost:3000/client/build/' + path)
    return app.send_static_file(path)

def proxy(url):
    response = get(url)
    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    headers = {
        name: value
        for name, value in response.raw.headers.items()
        if name.lower() not in excluded_headers
    }
    return (response.content, response.status_code, headers)
if __name__ == '__main__':
    app.run()