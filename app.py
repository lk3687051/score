#encoding=utf-8
"""Cloud Foundry test"""
from flask import Flask, send_from_directory, request
import os
import redis
import json
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
def conf_add():
    pass

@app.route("/config/list", methods=['GET'])
def conf_list():
    data = [{
              'id': "01",
              'name_cn': u"帅气",
              'name_en': "handsome",
              'desc_cn': "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              'desc_en': "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              'score': "5",
              'rating': "2"
            }, {
              'id': "02",
              'name_cn': u"经济",
              'name_en': "emkkk",
              'desc_cn': "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              'desc_en': "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              'score': "5",
              'rating': "2"
            }
      ]

    return json.dumps(data), 200

@app.route("/config/del", methods=['POST'])
def conf_del():
    pass

@app.route("/score/add/<username>/<target>", methods=['POST'])
def add_score(username, target):
    print username
    print target
    aa =  request.get_json()
    for a in aa:
        print a
        #r_client.set('score:'+username+':'+ target + a.name, a.score)
    return "", 200


@app.route("/score/list/<username>", methods=['POST'])
def score_list():
    pass

@app.route("/user/show/<user_id>", methods=['GET'])
def get_user_info(user_id):
    if int(user_id) != 888:
        return "", 500
    return u"陆康", 200

@app.route("/score/show/<username>/<targetname>", methods=['POST'])
def score_show():
    pass

@app.route("/score/delete/<username>/<targetname>", methods=['POST'])
def score_del():
    pass

if __name__ == '__main__':
    #app.config['UPLOAD_FOLDER'] = '/home/vcap/app/ui/'
    app.config['UPLOAD_FOLDER'] = '/root/share/score/ui/'
    app.run(host='0.0.0.0', port=8000)