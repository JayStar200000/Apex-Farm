import socket
import subprocess
import time

# Client Configuration
SERVER = "127.0.0.1"  # Replace with the server's IP address
PORT = 12345

def open_game():
    """Simulate opening the game."""
    try:
        # Replace with the actual game executable path
        subprocess.run(r"C:\Program Files (x86)\Steam\steamapps\common\Apex Legends\ApexLauncher.exe", check=True)
        return "Game opened successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to open game: {e}"
    except Exception as e:
        return f"Unexpected error while opening game: {e}"

def restart_game():
    """Simulate restarting the game."""
    try:
        # Replace with the actual game executable path
        subprocess.run("taskkill /f /im r5apex.exe", check=True)  # Close game
        subprocess.run(r"C:\Program Files (x86)\Steam\steamapps\common\Apex Legends\ApexLauncher.exe", check=True)  # Open game again
        return "Game restarted successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to restart game: {e}"
    except Exception as e:
        return f"Unexpected error while restarting game: {e}"

def close_game():
    """Simulate closing the game."""
    try:
        # Replace with the actual game executable name
        subprocess.run("taskkill /f /im r5apex.exe", check=True)  # Close game
        return "Game closed successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to close game: {e}"
    except Exception as e:
        return f"Unexpected error while closing game: {e}"

def unknown_command(command):
    """Handle unknown commands."""
    return f"Unknown command: {command}"

def execute_command(command):
    """Route command to the appropriate function."""
    if command == "open_game":
        return open_game()
    elif command == "restart_game":
        return restart_game()
    elif command == "close_game":
        return close_game()
    else:
        return unknown_command(command)

def send_feedback(client, message):
    """Send feedback to the server."""
    try:
        client.send(message.encode())
    except Exception as e:
        print(f"[ERROR] Failed to send feedback: {e}")

def start_client():
    """Start the client and handle server communication."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"[CONNECTED] Connected to the server at {SERVER}:{PORT}")

    try:
        # Send readiness status to the server
        client.send("READY".encode())
        # Wait for the start signal
        while True:
            command = client.recv(1024).decode()
            if command == "START":
                feedback = execute_command("open_game")
                send_feedback(client, feedback)
                break
        while True:
            # Wait for commands from the server
            command = client.recv(1024).decode()
            if command:
                print(f"[COMMAND RECEIVED] {command}")
                feedback = execute_command(command)
                send_feedback(client, feedback)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client.close()
        print("[DISCONNECTED] Connection closed.")

if __name__ == "__main__":
    start_client()
