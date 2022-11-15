import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.qk1cs8d.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.sparta
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/join', methods=['POST'])
def api_register():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickName_receive = request.form['nickName_give']
    db.userinfo.insert_one({'name':name_receive, 'id': id_receive, 'pw': pw_receive, 'nickName' : nickName_receive})

    return jsonify({'result': '회원가입 성공!'})

@app.route('/join')
def register():
    return render_template('join.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5555, debug=True)