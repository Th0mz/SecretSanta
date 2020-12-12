from socket import *
from urllib.parse import unquote

from Entities import * 

class Server:

    # Constructor
    def __init__(self, port, serverIp=gethostbyname(gethostname())):
        self.serverIp = serverIp 
        self.port = port
        
        # Create socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)

        self.registeredEntities = Entities()

    def startServer(self):
        """ Starts the server """
        try:
            # Bind name to the server (url)
            self.serverSocket.bind((self.serverIp, self.port))
            
            print("Server Started connect with : " + self.serverIp + ":" + str(self.port))
            # Initialize the request queue
            self.serverSocket.listen(5)

            # Receive and send message loop
            while (True):
                (clientSocket, address) = self.serverSocket.accept()
                
                # Receive message
                message = clientSocket.recv(5000).decode()
                messagePieces = message.split("\n")

                if len(messagePieces) > 0:
                    # Process message and send response
                    htmlFile = self.processMessage(messagePieces[0])
                    self.sendMessage(htmlFile, clientSocket)

                    print("Message Received from " + address[0] + ":" + str(address[1]) + " [" + htmlFile.replace(".html", "").upper() + "]")

                # End comunication line between server and client
                clientSocket.shutdown(SHUT_WR)

        except KeyboardInterrupt:
            print("\nStop collecting information ...")
            print("Website shuttedown\n")
        except Exception as exception:
            print("Error:\n")
            print(exception)


    def processMessage(self, message):
        """ Given the message from the client choses with htmlFile
            should send to the client in response and process the
             input so the server makes what the client expects """

        def parseMessage(message):
            """Message is something like this GET /?name=inputName&email=inputEmail HTTP/1.1
            the next commands are to separate the name and email inputs from the rest of  
                                      the information """

            message = message[5:-9]
            message = message.split("&")

            # Name cleaning and decode url encoding
            message[0] = message[0].replace("?name=", "")
            # Email cleaning
            message[1] = message[1].replace("email=", "")
            

            # Decode url encoding
            for i in range(len(message)):
                message[i] = unquote(message[i]).replace("+", " ")           

            return message
        
        # Checks if the url was name and email paramters => client filed the form
        if ("name" in message) and ("email" in message):

            (name, email) = parseMessage(message)
            if not ((name == "") or (email == " ")): 
                self.registeredEntities.addEntity(name, email)
                return "success.html"

        return "form.html"
        

    def sendMessage(self, htmlFile, clientSocket):
        """ Sends the htmlFile content to the clientSocket """

        def processHTML(htmlFile):                 
            """ Given a htmlFile process it into a string message"""
            with open(htmlFile, "r") as html:
                messagePieces = html.readlines()

            message = ""
            for piece in messagePieces:
                message += piece.replace("\n", "") + "\r\n\r\n"

            return message

        
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n\r\n"
        data += processHTML(htmlFile)

        # Send all data
        clientSocket.sendall(data.encode())



