#encoding=utf-8
"""Cloud Foundry test"""
from flask import Flask, send_from_directory, request
import os
import json
import redis

app = Flask(__name__)
r_client = redis.Redis(host = 'local', port = 6357, db = 0)
#port = int(os.getenv("VCAP_APP_PORT")

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
              'name_cn': u"外表",
              'name_en': "Handsome",
              'desc_cn': u"外表很重要，因为人们的首轮效应，也就是第一印象很重要，外表不仅仅指一个人的长相，还包括穿衣打扮。",
              'desc_en': "please mark for his handsome",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "02",
              'name_cn': u"财富",
              'name_en': "Wealth",
              'desc_cn': u"这里的财富即物质，每个人对财富都有自己的定义，所谓贫贱夫妻百事哀,所以基本的房子车子还是要有的，还有能保障中产阶级生活品质的收入。",
              'desc_en': "please mark for his wealth",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "03",
              'name_cn': u"性格",
              'name_en': "Character",
              'desc_cn': u"是帅气暖男，还是霸道总裁？你喜欢哪款？",
              'desc_en': "please mark for his character",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "04",
              'name_cn': u"智慧",
              'name_en': "Wisdom",
              'desc_cn': u"智慧二字的组成，是日知而心彗。学如逆水行舟不进则退。有真正智慧的人，深知人性，了之人生，所以方能宁静淡泊以处事，忠厚仁义以待人。",
              'desc_en': "please mark for his wisdom",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "05",
              'name_cn': u"孝心",
              'name_en': "Filial love",
              'desc_cn': u"百善孝为先，有孝心的人，必定心地善良，但孝心并不是愚孝，万事要讲方式方法。",
              'desc_en': "please mark for his filial love",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "06",
              'name_cn': u"幽默",
              'name_en': "Humorous",
              'desc_cn': u"风趣的人，大多是十分乐观的人。具有积极向上的人生态度和百折不回的精神，不论遇到什么，都不忘记给你带来欢乐",
              'desc_en': "please mark for his humorous",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "07",
              'name_cn': u"浪漫",
              'name_en': "Romantic",
              'desc_cn': u"真正的浪漫是种感觉、一种与生俱来的气质，是两人之间的一种无声的默契，没法用语言去描述，也不好去照猫画虎的模仿",
              'desc_en': "please mark for his humorous",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "08",
              'name_cn': u"尊重",
              'name_en': "Respect",
              'desc_cn': u"懂得尊重你的人，他不会强逼你做不喜欢的事，如果他爱你，他会尊重你的个人喜好",
              'desc_en': "please mark for respect",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "09",
              'name_cn': u"信任",
              'name_en': "Trust",
              'desc_cn': u"信任是两个人在一起长久的基础，既然相爱就该要信任.既然不信任又何必在一起?",
              'desc_en': "please mark for his trust",
              'score': "5",
              'rating': "0"
            },
            {
              'id': "10",
              'name_cn': u"温柔体贴",
              'name_en': "gentleness",
              'desc_cn': u"生病时给你买药倒水，疲倦时给你捶背。关注细节，设身处地的为你着想。",
              'desc_en': "please mark for his gentleness",
              'score': "5",
              'rating': "0"
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
    items =  request.get_json()
    for item in items:
        print item
        r_client.set('score:'+username+':'+ target + item.name, item.score)
    return "", 200


@app.route("/score/list/<username>", methods=['POST'])
def score_list():
    pass

@app.route("/user/show/<user_id>", methods=['GET'])
def get_user_info(user_id):
    if int(user_id) == 888:
        return u"陆康", 200
    elif int(user_id) == 666:
        return u"李欣欣", 200
    return u"查无此人", 500

@app.route("/score/show/<username>/<targetname>", methods=['POST'])
def score_show():
    pass

@app.route("/score/delete/<username>/<targetname>", methods=['POST'])
def score_del():
    pass

if __name__ == '__main__':
    #app.config['UPLOAD_FOLDER'] = '/home/vcap/app/ui/'
    app.config['UPLOAD_FOLDER'] = '/home/cindy/tmp/score/ui/'
    app.run(host='0.0.0.0', port=8000)
