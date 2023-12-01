from  flask import  Flask

app = Flask(__name__)

@app.route('/')
def index ():
    a=1
    return  {"name":"kenny"}

if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=8081)