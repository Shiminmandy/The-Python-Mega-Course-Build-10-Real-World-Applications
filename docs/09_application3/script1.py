# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
from flask import Flask, render_template

# 网页浏览器可以读取HTML文件，并将其渲染成可视化网页。

app = Flask(__name__)


@app.route('/')
def home():
    # return "Homepage here"   # search http://127.0.0.1:5000/
    return render_template("home.html")

@app.route('/about/')  # we need to search http://127.0.0.1:5000/about/ instead
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)
