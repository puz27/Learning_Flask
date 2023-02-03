from flask import request
from flask import make_response
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    data = "START PAGE"
    return render_template("index.html", data= data), 200

@app.route('/about/')
def about():
    data = "ABOUT PAGE"
    user_agent = request.headers.get('User-Agent')
    list = [1, 2, 3]
    addres_info = url_for('about', _external=True)

    return render_template("about.html", data= data, user_agent= user_agent, list= list, addres_info= addres_info)


@app.route('/cookie/')
def cookie():
    data = "COOKIE PAGE"
    response = make_response("CARRIES COOKIE!")
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "USER:" + name + "ID:" + str(id)

@app.route('/pictures/')
def pictures():
    return render_template("pictures.html")


@app.errorhandler(404)
def error_404(data):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)

