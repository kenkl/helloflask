from flask import Flask
import os

hitcount = 0
app = Flask(__name__)

@app.route('/')

def index():
    try:
        servername = os.environ['MYSERVERNAME']
    except KeyError:
        servername = '[MYSERVERNAME undefined]'
    global hitcount
    hitcount += 1
    message = f"Hello from Flask, running on {servername}!   {hitcount}   \n\n"

    return message

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=False)
