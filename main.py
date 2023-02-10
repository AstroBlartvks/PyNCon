from pyngrok import ngrok
from Pyngrok import pyngrok
from sys import argv as argumentsValue


def print_exception(exception):
    #print the exception and close programm
    print("\n[!] The exception: " + str(exception))
    input("")
    exit(-1)


def main():
    
    PyNgrok = pyngrok(ngrok)
    (port, authkey) = PyNgrok.getArguments(argumentsValue)

    #Get port and authkey
    if port == -1: port = input("[*] Write your port: ")
    if authkey == "": authkey = input("[*] Write your authkey: ")

    #Try to create tunnel
    tunnel = PyNgrok.create_tunnel(port)
    if tunnel is None: print_exception("Not connected")
    else: PyNgrok.print_addres(tunnel)

    #Set ngrok authkey 
    response = PyNgrok.set_authkey(authkey)
    if response is None: print_exception("AuthKey is not working")  
    else: print("[*] Authkey is valid")   
    
    #Show info about tunnel
    if not PyNgrok.print_info(tunnel): print_exception("Invalid tunnel info")
 
    #The cycle is waiting
    while True:
        to_close = input("[*] Write \"close\" to close: ")
        if to_close == "close": 
            ngrok.disconnect(tunnel)
            break


if __name__ == "__main__":
    main()
    input("")
