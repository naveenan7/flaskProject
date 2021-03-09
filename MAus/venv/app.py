__author__ = 'kai'

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    URL = request.form['url']
    return 'URL you entered %s <br/> ' \
           '<a href="/">Back Home</a>' % (URL)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host = '0.0.0.0', port = 3000)