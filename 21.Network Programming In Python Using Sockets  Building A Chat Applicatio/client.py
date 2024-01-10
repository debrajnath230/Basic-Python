import socket
import threading
from tkinter import *

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    threading.Thread(target=receive_messages).start()

def send_message():
    message = entry.get()
    text_area.insert('end', 'You: ' + message + '\n')
    entry.delete(0, END)
    client_socket.send(bytes(message, 'utf-8'))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            text_area.insert('end', 'Server: ' + message + '\n')
        except ConnectionResetError:
            break

# Tkinter GUI
root = Tk()
root.title("Client")

text_area = Text(root, height=10, width=50)
text_area.pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=10)

send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Start the client
start_client()

root.mainloop()

# Close the client socket when GUI is closed
client_socket.close()
