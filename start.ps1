# Change to the project directory
cd C:\Users\jerom\autoMproject

# Start server.py in a new PowerShell window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python server.py"

# Wait for 5 seconds
Start-Sleep -Seconds 5

# Start client.py in a new PowerShell window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python client.py"
