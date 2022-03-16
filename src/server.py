from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/blog')
def get_blog():
    return render_template('index.html')

@app.route('/blog',methods=['POST'])
def post_blog():
    title = request.form['title']
    body = request.form['body']
    return f"タイトルは{title}です。本文は{body}です。"
    