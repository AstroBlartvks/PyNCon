class pyngrok:
    def __init__(self, ngrok):
        print(f"\nHello, user. The program was created by Astro. Good luck using it.\n")
        self.port = 0
        self.authkey = ''
        self.ngrok = ngrok
    

    def getArguments(self, argString: str):
        """Return port and authkey from sys.argv"""

        port = -1
        authkey = ""

        if len(argString) < 2:
            return (port, authkey)

        if len(argString[1]) < 5 and ("help" in argString[1] or "h" in argString[1]):
            print("[p]\tp=port\tPort of server\tp=8080")
            print("[a]\ta=auth\tNgrok auth key\ta=abcdef01234...")
            return (port, authkey)

        for arg in argString[1:]:
            stripped = arg.strip().replace(" ", "")

            if "p=" == stripped[0:2]:
                port = int(stripped[2:])
            if "a=" in stripped[0:2]:
                authkey = str(stripped[2:])
        
        return (port, authkey)
        

    def set_authkey(self, authkey: str):
        try:
            self.ngrok.set_auth_token(authkey)
            return True
        except:
            return None


    def create_tunnel(self, port: str, type: str = "tcp"):
        try: return self.ngrok.connect(int(port), type)
        except: return None
        

    def print_addres(self, tunnel):
        print("[*] You are:", tunnel.config["addr"], "\n")

    
    def print_info(self, tunnel):
        try:
            tcpConnect = tunnel.public_url[6:]
            [your_url, port] = tcpConnect.split(":")
            print("[i] Your external url is", your_url)
            print("[i] Your external port is", port)
            print("\n")
            return True
        except:
            return False
        