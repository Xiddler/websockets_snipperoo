from flask import Flask, render_template

from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 's33ookouiuorwoijdjfl4k5lj3lk45jl34j5lkjflkjdlfmysecret'
socketio = SocketIO(app)


def removeBadChars(strUser):
    ''' Helper function to prevent input of HTML accidentally or otherwise but allow URLs-- not finished yet '''
    import re
    strUser = re.sub(r'[^A-Za-z0-9_ /\*:\.\?=\+&]', "", strUser)
    return strUser

@socketio.on('message')
def handleMessage(msg):
    strUser = msg
    # send(msg, broadcast=True)
    try:
        send(removeBadChars(strUser), broadcast=True)
    except:
        print("Problem with send")



@app.route('/')
def index():
    # messages = ['Snippets:', ]
    messages = ['', ]
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0',  port=5000)
    socketio.run(app, host='0.0.0.0',  port=5000, debug=True)
    # socketio.run(app, host='0.0.0.0',  debug=True)
    # socketio.run(app, host='0.0.0.0', port=5000)
    # socketio.run(app, host='127.0.0.1', port=5000)
    # socketio.run(app)
