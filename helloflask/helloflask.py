from flask import Flask

hitcount = 0
app = Flask(__name__)

@app.route('/')

def index():
    global hitcount
    hitcount += 1
    message = f"Hello from Flask, running on [insert server name]!   {hitcount}   \n\n"

    return message

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=False)
