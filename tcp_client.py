import os
import socket
from datetime import datetime


class TCPClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.conn_sock = None

    @staticmethod
    def printwt(msg: str) -> None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{timestamp}] {msg}')

    def create_socket(self) -> None:
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.printwt('Socket created')

    def interact_with_server(self) -> None:
        try:
            self.printwt(f'Connecting to server [{self.host} on port [{self.port}]')
            self.conn_sock.connect((self.host, self.port))

            self.printwt('Sending country to server to get capital...')
            country = 'Ireland'
            self.conn_sock.sendall(country.encode('utf-8'))
            self.printwt('[ SENT ]: ')
            self.printwt(country)

            resp = self.conn_sock.recv(1024)
            self.printwt('[ RECEIVED ]: ')
            print(resp.decode())

            self.printwt('Interaction completed successfully')
        except OSError as err:
            self.printwt('Cannae connect to server')
            print(err)
        finally:
            self.printwt('Closing connection socket...')
            self.conn_sock.close()
            self.printwt('Socket closed')


def main():
    tcp_client = TCPClient('127.0.0.1', 8080)
    tcp_client.create_socket()
    tcp_client.interact_with_server()


if __name__ == '__main__':
    main()
