from flask import Flask, render_template, request


app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/create-todo', methods=['GET', 'POST'])
def create_todo():
    if request.method == "POST":
        return render_template("success.html")
    if request.method == "GET":
        return render_template("create-todo.html")
    return render_template("create-todo.html")


if __name__ == '__main__':
    app.run(debug=True)
