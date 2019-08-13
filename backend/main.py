from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../frontend/templates')


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/data", methods=['POST'])
def data():
    username = request.form('username')
    password = request.form('password')
    print(username)
    print(password)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
