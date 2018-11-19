# BasicMenuServer Python 3.6
Purpose: Coding basic server-client 

Client:
  - Recieving input from user, send it to server
  - Printing server's answer

Server:
  - Getting legally Commands: EXIT, RAND, NAME, TIME
    - Exit - stop running
    - Rand - return random number between 1-10
    - Name - return server name (Amit's Server)
    - Time - return current time and date (YY-MM-DD)
  - Any other input = Error message to client
