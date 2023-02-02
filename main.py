import datetime
import random

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    name = "START PAGE"
    return render_template("index.html", name= name)

@app.route('/about')
def about():

    return render_template("about.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "USER:" + name + "ID:" + str(id)

# @app.route('/test_1')
# def test_1():
#     a = 1
#     b = 3
#     c = 2
#     return render_template("test_1.html", numbers=(7, 5, 8, 0, 3), a=a, b=b, c=c)


#подсчет оперций
@app.route('/<float:a>/<string:znak>/<float:b>/')
def test_2(a, znak, b):
    if znak == ":":
        znak = '/'
        if b == 0:
            return render_template("test_2.html", final="Ошибка")
        else:
            final = eval(str(a) + znak + str(b))
            return render_template("test_2.html", final=final)
    final = eval(str(a)+znak+str(b))
    return render_template("test_2.html", final=final)


# вывод информации в шаблоны

# @app.route('/<float:number_float>/')
# def count_number(number_float):
#     number = number_float
#     output = number * 2
#     return render_template("index.html", text= "Ваше число {}, умноженное на 2: {}".format(number, output))
# @app.route('/<float:r>/')
# def count_number_2(r):
#     pi = 3.14
#     return render_template("index.html", pi=pi, r=r)




if __name__ == "__main__":
    app.run(debug=True)
