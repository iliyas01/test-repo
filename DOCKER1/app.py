from flask import Flask, app,jsonify
app=Flask(__name__)
@app.route('/')
def iliyas():
    return "API"
if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0',port='5555')
    
