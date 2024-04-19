
import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

# server_address = 
@sio.event
def connect():
    print("Successfully connected to the server.")
    # You can perform actions here after connection is established

@sio.event
def message(data):
    print("Received message:", data)
    # Handle incoming messages from the server

@sio.event
def disconnect():
    print("Disconnected from the server.")

if __name__ == '__main__':
    try:
        # Connect to the server using the URL of your GitHub Codespaces instance
        sio.connect(server_address, transports=['websocket'])

        print("Connected to the server")
        # Keep the client running to listen for incoming messages
        sio.wait()
    except socketio.exceptions.ConnectionError as e:
        print(f"Failed to connect to the server: {e}")
