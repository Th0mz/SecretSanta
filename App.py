import Server
from SendEmails import *

def main():
    # Create a new server instance
    server = Server.Server(8000)

    # Start http server
    server.startServer()

    # Show registered entries 
    server.registeredEntities.printEntries()

    server.registeredEntities.shuffleEntries()
    #server.registeredEntities.printShuffledEntries()


    answer = input("\nAre the given inputs good? [Y/n] : ")
    # Send emails only if the user allows it 
    if answer == "Y":
        sendEmail(server.registeredEntities.shuffledEntities)
        print("\nAll Emails sent successfully\n")


# Run Main function
if __name__ == '__main__':
    main()