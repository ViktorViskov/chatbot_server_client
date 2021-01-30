# 
# Import libs
# 

# flask
from flask import *

# Cross Origin Resource Sharing (CORS) (for use uncomment line under)
# from flask_cors import CORS

# bot
from bot import say_bot

# 
# Settings
# 

# server ip address
server_ip = '0.0.0.0'
# server port for listening
server_port = 81
# debug mode
enable_debug_mode = False

# 
# Creating server application
# 

# create server app
app = Flask(__name__)

# enabling CORS (for use uncomment line under)
# CORS(app)

# 
# Routing
# 

# Main page
@app.route('/', methods=['GET','POST'])
def main():
    
    # print main page
    if request.method == 'GET':
        return render_template('index.html')

    # if POST print error
    else:
        return render_template('page_not_found.html'), 404

# Bot for POST AJAX and GET its client
@app.route('/bot', methods=['GET','POST'])
def bot():
    # connect to bot
    if request.method == 'POST':
        return say_bot(request.json['message'])

    # if GET print error
    else:
        return render_template('bot.html')

# Bot for POST html form
@app.route('/bot_form', methods=['GET','POST'])
def bot_post():
    # connect to bot
    if request.method == 'POST':
        return say_bot(request.form['message'])

    # if GET print error
    else:
        return render_template('page_not_found.html'), 404

# Error
# If request not found, print error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# 
# Start server application
# 

# check that the server has been started from the terminal
if __name__ == "__main__":

    # debug mode for dev
    app.debug = enable_debug_mode

    # start web server
    app.run(host=server_ip, port=server_port)
