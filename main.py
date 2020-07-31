from flask import json
from flask import request
from flask import Flask

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'hello'

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        print (json.dumps(request.json))
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)