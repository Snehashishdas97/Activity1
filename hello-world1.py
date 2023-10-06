from flask import Flask
#helloguys
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a release."

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
