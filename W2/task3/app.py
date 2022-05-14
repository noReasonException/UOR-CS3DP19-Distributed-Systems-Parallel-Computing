from flask import Flask
from flask import request
app = Flask(__name__)

global id
id=0
db = [{'id':0,'title':'example','description':'example description','done':True}]
def dbAsJson(db):
    return {'tasks':db}

@app.route('/todo/api/v1.0/tasks')
def getTasks():
    return dbAsJson(db)

@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def addTask():
    global id,db
    db.append({'id':id+1,'title':request.json['title'],'description':request.json['description'],'done':False})
    id+=1
    return 'OK'






if __name__ == "__main__":
    app.run(debug=True)

