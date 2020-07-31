from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        print (json.dumps(request.json))
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)