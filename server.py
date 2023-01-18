from flask import Flask,request,jsonify
import os,json,pytz


db ={}
db_filename ="db.json"

if os.path.exists(db_filename):
    with open(db_filename,'r') as f:
        db = json.load(f)
else:
    
    db = {
        "jobs":[]
    }

    with open(db_filename,'w+') as f:
        json.dump(db,f,indent=4)

app=Flask(__name__)

#Post data

@app.route('/job',methods = ['POST'])
def addJob():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        db['jobs'].append(data)
        
        with open(db_filename,"r+") as f:
            f.seek(0)
            json.dump(db,f,indent=4)
        return 'Jobs Added successfully'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port='3000',debug = True)
