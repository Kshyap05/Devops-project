from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World!,my name is kashyap the upcoming enginner with all the efforts i will do all this"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
