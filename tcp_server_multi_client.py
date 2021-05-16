import threading
import tcp_server


class TCPServerMultiClient(tcp_server.TCPServer):

    def __init__(self, host, port) -> None:
        super().__init__(host, port)

    def wait_for_client(self):
        try:
            self.printwt('Listening for incoming connections')
            # 3 clients before server refuse connection
            self.sock.listen(3)

            while True:
                client_sock, client_address = self.sock.accept()
                self.printwt(f'Accepted connection from {client_address}')
                c_thread = threading.Thread(target=self.handle_client,
                                            args=(client_sock, client_address))
                c_thread.start()

        except KeyboardInterrupt:
            self.shutdown_server()


def main():
    tcp_server_multi_client = TCPServerMultiClient('127.0.0.1', 8080)
    tcp_server_multi_client.configure_server()
    tcp_server_multi_client.wait_for_client()


if __name__ == '__main__':
    main()
