import socket
import threading
import time

# Server Configuration
HOST = "0.0.0.0"
PORT = 12345

clients = []
ready_clients = []

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    clients.append(client_socket)
    try:
        # Wait for the client to send readiness status
        status = client_socket.recv(1024).decode()
        if status == "READY":
            ready_clients.append(client_socket)
            print(f"[{address}] is ready.")
        while True:
            # Receive feedback from the client
            feedback = client_socket.recv(1024).decode()
            if feedback:
                print(f"[FEEDBACK FROM {address}] {feedback}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)
        print(f"[DISCONNECTED] {address} disconnected.")

# Broadcast commands to all clients
def broadcast_command(command):
    for client in clients:
        try:
            client.send(command.encode())
        except Exception as e:
            print(f"[ERROR] Failed to send command to a client: {e}")

# Main server loop
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    threading.Thread(target=command_input).start()
    threading.Thread(target=wait_for_ready_clients).start()
    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Function to take commands from the server admin
def command_input():
    while True:
        command = input("Enter command ('quit' to stop): ")
        if command.lower() == "quit":
            break
        broadcast_command(command)

def wait_for_ready_clients():
    print("[WAITING] Waiting for all clients to be ready...")
    while True:
        if len(ready_clients) >= expected_client_count:
            print("[ALL CLIENTS READY] Starting the game on all clients.")
            broadcast_command("START")
            break
        time.sleep(1)

if __name__ == "__main__":
    expected_client_count = 1  # Set the number of expected clients
    start_server()
