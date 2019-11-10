from flask import Flask, escape, request

app = Flask(__name__)

class User:
    email = ''
    pwd = ''
        # parameterized constructor
    def __init__(self, f, s):
        self.email = f
        self.pwd = s


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
