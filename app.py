"""Cloud Foundry test"""
from flask import Flask, send_from_directory, request
import os
import redis

app = Flask(__name__)
r_client = redis.Redis(host = 'local', port = 6357, db = 0)
#port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def hello_world():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'index.html')
    #return 'Hello World! I am running on port ' + str(port)

@app.route('/static/<path:folder>/<path:path>')
def send_static_file(folder, path):
    """ Static files """
    return send_from_directory(app.config['UPLOAD_FOLDER'], folder+'/'+path)

@app.route("/config/add", methods=['POST'])
def add_conf():
    pass

@app.route("/config/list", methods=['POST'])
def add_conf():
    pass

@app.route("/config/del", methods=['POST'])
def add_conf():
    pass

@app.route("/score/add/<username>/<target>", methods=['POST'])
def add_score(username, target):
    print username
    aa =  request.get_json()
    for a in aa:
        r_client.set('score:'+username+':'+ target + a.name, a.score)
    return 200


@app.route("/score/list/<username>", methods=['POST'])
def add_conf():
    pass

@app.route("/score/show/<username>/<targetname>", methods=['POST'])
def add_conf():
    pass

@app.route("/score/delete/<username>/<targetname>", methods=['POST'])
def add_conf():
    pass

if __name__ == '__main__':
    #app.config['UPLOAD_FOLDER'] = '/home/vcap/app/ui/'
    app.config['UPLOAD_FOLDER'] = '/root/share/myproject/ui/'
    app.run(host='0.0.0.0', port=8000)