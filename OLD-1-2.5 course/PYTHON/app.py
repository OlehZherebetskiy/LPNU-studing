import requests
from flask import Flask, request, jsonify, make_response, make_response, Response
from json import dumps
import json
import pymongo
import logging
from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import config as cfg
from flask_appbuilder import AppBuilder
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_mongoengine import MongoEngine
import time

current_milli_time = lambda: str(round(time.time() * 1000))
app = Flask(__name__)
ismoder = False

""" swagger specific """
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "test"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
""" end swagger specific """


#////////////////////////////////////////////



dbmongo = MongoEngine(app)

import models
#////////////////////////////////////////////////
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
users = mydb["Users"]
articles = mydb["Articles"]

#/////////////////////////////











@app.route('/user/reg/', methods=['post'])
def reg():
    str =  request.get_json();
    name = str["username"];
    password = str["password"];
    id = (current_milli_time())
    user = {"username":name,"password":password,"moderator":False,"id": id}
    x = users.insert_one(user)
    return jsonify("OK")

@app.route('/user/log/', methods=['post'])
def log():
    global ismoder
    str = request.get_json();
    name = str["username"];

    user = {"username": name}
    x = users.find_one(user)
    if x:
        myquery = {"username": name}
        newvalues = {"$set": {"moderator": True}}

        users.update_one(myquery, newvalues)
        ismoder = x["moderator"]
        print(ismoder)
        return jsonify({"username": x["username"], "moderator": x["moderator"],"id": x["id"]})
    else:
        return Response('{"error": "not registered"}', status=403, mimetype='application/json')


#////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////

@app.route('/getallart/', methods=['get'])
def getallart():
    arr = list(articles.find())
    lis =  []
    for i in arr:

        print(i)

        if not i['requested']:
            del i['text']
            del i['requested']
            del i['username']
            del i["_id"]
            i['patron_id'] = i['patron_id']
            lis.append(i)
    print(lis)
    if len(lis)>0:
        return Response(json.dumps(lis),  mimetype='application/json')
    else:
        return Response('{"msg":"List of articles is empty"}', status = 403, mimetype='application/json')

@app.route('/getarttext/', methods=['post'])
def getarttext():
    str = request.get_json();
    title = str["title"];
    arr = list(articles.find({"title":title,"requested":False}))
    lis = []
    for i in arr:
        if not i['requested']:
            del i['_id']
            i['patron_id'] = i['patron_id']
            lis.append(i)
    print(lis)
    if len(lis) > 0:
        return Response(json.dumps(lis), mimetype='application/json')
    else:
        return Response('{"msg":"There is not articles with this title"}', status=403, mimetype='application/json')


#//////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////


@app.route('/userputmarge/', methods=['put'])
def userputmarge():
    str = request.get_json();
    name = str["username"];
    title = str["title"];
    text = str["text"];
    requested = True;

    articles.insert_one({"username":name,"title":title,"text":text,"requested":requested})

    return jsonify("OK")

@app.route('/useraddart/', methods=['put'])
def useraddart():
    str = request.get_json();
    name = str["username"];
    title = str["title"];
    text = str["text"];
    requested = False;
    x=list(users.find({"username":name}))
    if len(x)>0:
        print(x[0].values())
        patron_id=x[0]["id"]

        articles.insert_one({"username":name,"title":title,"text":text,"requested":requested,"patron_id":patron_id})
        return jsonify("OK")
    else:
        return jsonify("No such user")


# //////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////

@app.route('/mod/getallart/', methods=['get'])
def modgetallart():
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    arr = list(articles.find())
    lis =  []
    for i in arr:
        del i['text']
        del i['username']
        del i['_id']
        i['patron_id'] = i['patron_id']
        lis.append(i)
    print(lis)
    if len(lis) > 0:
        return Response(json.dumps(lis), mimetype='application/json')
    else:
        return Response('{"msg":"List of articles is empty"}', status=403, mimetype='application/json')


@app.route('/mod/getrequestart/', methods=['get'])
def getrequestart():
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    arr = list(articles.find())
    lis = []
    for i in arr:
        if i['requested']:
            del i['text']
            del i['requested']
            del i['username']
            del i['_id']
            i['patron_id'] = i['patron_id']
            lis.append(i)
    print(lis)
    if len(lis) > 0:
        return Response(json.dumps(lis), mimetype='application/json')
    else:
        return Response('{"msg":"List of articles is empty"}', status=403, mimetype='application/json')


@app.route('/mod/getarttext/', methods=['post'])
def modgetarttext():
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    str = request.get_json();
    title = str["title"];
    arr = list(articles.find({"title": title}))
    lis = []
    for i in arr:
        del i['_id']
        i['patron_id'] = i['patron_id']
        lis.append(i)
    print(lis)
    if len(lis) > 0:
        return Response(json.dumps(lis), mimetype='application/json')
    else:
        return Response('{"msg":"There are no articles with this title"}', status=403, mimetype='application/json')

@app.route('/mod/modmarge/', methods=['put'])
def modmarge():
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    str = request.get_json();
    title = str["title"];
    user = str["username"];
    text= str["text"];
    myquery = {"username": user,"title":title,"requested":False}
    if not articles.find_one({"username": user,"title":title,"requested":True}):
        return Response('{"msg": "Nothing find"}', status=403, mimetype='application/json')
    articles.delete_one({"username": user,"title":title,"requested":True})
    newvalues = {"$set": {"text": text}}

    articles.update_one(myquery, newvalues)
    return jsonify("OK")


@app.route('/mod/moddel/', methods=['delete'])
def moddel():
    #user = list(users.find());
    #for i in user:
    #   users.delete_one({"_id":i["_id"]})
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    str = request.get_json();
    title = str["title"];
    user = str["username"];
    requested = str["requested"];
    if not articles.find_one({"title":title,"requested":requested,"username":user}):
        return jsonify("Nothing find")
    articles.delete_one({"title":title,"requested":requested,"username":user})
    return jsonify("OK")





@app.route('/mod/givemoder/', methods=['put'])
def givemoder():
    global ismoder
    if not ismoder:
        return Response('{"msg":"You are not moderator"}', status = 403,  mimetype='application/json')
    str = request.get_json();
    user = str["username"];
    myquery = {"username": user}
    newvalues = {"$set": {"moderator": True}}

    users.update_one(myquery, newvalues)
    return jsonify("OK")

# //////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////





if __name__ == '__main__':
    app.run(debug=True)

