from datetime import datetime
from flask import Flask, render_template, request
from api.api import api

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html',
                           calltime=f"{datetime.utcnow()}")

@app.route('/api', defaults={'path': ''})
@app.route('/api/<path:path>', methods=['GET'])
def getApi(path):
    global api
    return api.get(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)