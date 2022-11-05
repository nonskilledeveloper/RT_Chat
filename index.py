from ensurepip import bootstrap
from flask import Flask, render_template, request
data = ''
prev_message = ''
app = Flask(__name__)

@app.route('/conversation', methods = ['GET'])
def conversacion(username=None):
    global data
    global prev_message
    if request.method == 'GET':
        """"Aquí va lo que verá el usuario"""
    return render_template('conversation.html', data=data)

@app.route('/chat/<username>', methods = ['GET', 'POST'])
def chat(username=None):
    global data
    global prev_message
    if request.method == 'GET':
        """"Aquí va lo que verá el usuario"""
    elif request.method == 'POST':
        if request.form['mensaje'] in prev_message:
            prev_message = ''
        else:
            data = data + "<p>"+username+": " + request.form['mensaje']+'<br>'
        print(data)
    return render_template('chat.html', username=username)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")