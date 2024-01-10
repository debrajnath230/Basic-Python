import socket
import threading
from tkinter import *

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client, address = server_socket.accept()
        print(f"Connection established with {address}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            text_area.insert('end', 'Client: ' + message + '\n')  # Display client message in server chat box
            broadcast(message, client_socket)
        except ConnectionResetError:
            break

    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(bytes(message, 'utf-8'))
            except:
                clients.remove(client)

def send_server_message():
    server_message = server_entry.get()
    text_area.insert('end', 'Server: ' + server_message + '\n')
    broadcast(server_message, None)
    server_entry.delete(0, END)  # Clear the entry after sending the message

clients = []

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Tkinter GUI
root = Tk()
root.title("Server")

text_area = Text(root, height=10, width=50)
text_area.pack(pady=10)

server_entry = Entry(root, width=30)
server_entry.pack(pady=10)

send_button = Button(root, text="Send to Clients", command=send_server_message)
send_button.pack()

root.mainloop()

# Close the server socket when GUI is closed
server_socket.close()
