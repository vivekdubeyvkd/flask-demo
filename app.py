from flask import Flask, render_template, request
from lib.lib import returnInfo

app = Flask(__name__)
  
@app.route("/")
def main():
    #return "Welcome!"
	return render_template('index.html')
	
@app.route('/queryInfo')
def queryInfo():
    return render_template('queryInfo.html')
	
@app.route('/getInfo',methods=['POST' , 'GET'])
def getinfo():
    _key = request.form['person']
    return returnInfo(_key)
	
if __name__ == "__main__":
    app.run()
