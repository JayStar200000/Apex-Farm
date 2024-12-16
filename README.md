# Apex Farm

Really early stage not really for release. Apex Farm is a project designed to automate the control of the game Apex Legends on multiple PCs simultaneously. This project includes a server-client architecture where the server sends commands to clients to start, restart, and close the game. The clients execute these commands and send feedback to the server.

## Features

- **Start Game:** Simultaneously start Apex Legends on all connected clients.
- **Restart Game:** Restart Apex Legends on all connected clients.
- **Close Game:** Close Apex Legends on all connected clients.
- **Feedback Mechanism:** Clients send feedback to the server after executing commands.
- **Synchronization:** Ensures all clients are ready before starting the game.

## Setup Instructions

### Prerequisites

- Python 3.x installed on all PCs.
- Git installed on your development machine.
- Apex Legends installed on all client PCs.

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/JayStar200000/Apex-Farm.git
   cd Apex-Farm
   ```

2. **Configure Git User Information:**

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Set Up the Server:**

   - Navigate to the project directory:
     ```bash
     cd C:\Users\jerom\autoMproject
     ```
   - Run the server script:
     ```bash
     python server.py
     ```

4. **Set Up the Clients:**

   - Navigate to the project directory on each client PC:
     ```bash
     cd C:\Users\jerom\autoMproject
     ```
   - Run the client script:
     ```bash
     python client.py
     ```

5. **Automate the Process:**

   - Use the provided PowerShell script to start both the server and client:
     ```powershell
     .\start.ps1
     ```

## To-Dos

- [ ] Implement logging for better monitoring and debugging.
- [ ] Add error handling for network issues.
- [ ] Create a graphical user interface (GUI) for easier control.
- [ ] Add more commands for advanced game control.
- [ ] Implement security features to ensure only authorized clients can connect.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
