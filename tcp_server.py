import socket
from datetime import datetime

class TCPServer:

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.sock = None

    @staticmethod
    def printwt(msg) -> None:
        # Print message with timestamp 

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] {msg}')

    def configure_server(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.printwt('Socket created')

        self.sock.bind((self.host, self.port))
        self.printwt(f'Server bound to {self.host}:{self.port}')

    def wait_for_client(self) -> None:
        self.sock.listen(1)
        self.printwt('Server is listening for income connection')

        client_sock, client_address = self.sock.accept()
        self.printwt(f'Accepted connection from {client_address}')
        self.handle_client(client_sock, client_address)

    @staticmethod
    def get_capital(country) -> str:
        capitals= { 'Ireland': 'Dublin', 'Great Britain': 'London', 'Scotland': 'Edinburgh' }
        
        if country in capitals.keys():
            return f"{capitals[country]} is a capital of {country}"
        else:
            return f"No result for {country}. Is it country at all?"

    def handle_client(self, client_sock, client_address) -> None:
        try:
            data_enc = client_sock.recv(1024)
            while data_enc:
                country = data_enc.decode()
                resp = self.get_capital(country)

                self.printwt(f'[Requiest from {client_address}]: ')
                print(country)

                self.printwt(f'[Response to {client_address}]: ')
                print(resp)

                # More data, if it's greater than 1024 bytes limit
                data_enc = client_sock.recv(1024)

            self.printwt(f'Connection closed by {client_address}')

        except OSError as err:
            self.printwt(err)

        finally:
            client_sock.close()
            self.printwt(f'Client socket closed for {client_address}')

    def shutdown_server(self):
        self.printwt('Shutting down server...')
        self.sock.close()



def main():
    tcp_server = TCPServer('127.0.0.1', 4444)
    tcp_server.configure_server()
    tcp_server.wait_for_client()
    tcp_server.shutdown_server()


if __name__ == '__main__':
    main()