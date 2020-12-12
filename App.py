import Server
from SendEmails import *

def main():
    # Create a new server instance:
    #  -> Can be created in two ways:
    #     - Server.Server(8000) : that makes the socket ip your 
    #       "Ethernet adapter VirtualBox Host-Only Network" ipv4
    #       you can the machine that is hosting to this ip but
    #       no other device can connect to it
    #
    #     - Server.Server(8000, "customMachineIp") : customMachineIp
    #       can be whatever ipv4 your machine has but if u choose the
    #       "Wireless LAN adapter Wi-Fi" ipv4 other devices in the same
    #       network can connect to the website
    server = Server.Server(8000, "192.168.1.76")

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