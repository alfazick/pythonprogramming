# 1. Basic: Simple Echo Server

# pip install python-socketio
# pip install eventlet  # or gevent
# pip install uvicorn   # for the ASGI application in the advanced example
# pip install flask

from flask import Flask
import socketio

# Create a new Flask application
app = Flask(__name__)

# Create a Socket.IO server
sio = socketio.Server()

# Event handler for new connections
@sio.event
def connect(sid, environ):
    print("Client connected: ", sid)

# Event handler for message
@sio.event
def message(sid, data):
    print("Message from", sid, ":", data)
    # Echo message back to the client
    sio.send(sid, data)

# Event handler for client disconnects
@sio.event
def disconnect(sid):
    print("Client disconnected: ", sid)

# Flask route to handle the root URL
@app.route('/')
def index():
    return "Socket.IO Server is running!"

# Wrap Flask application with socket.io's middleware
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, app)
