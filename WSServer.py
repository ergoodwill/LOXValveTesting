import logging
from websocket_server import WebsocketServer

class WSServer:
    def new_client(client, server):
        server.send_message_to_all("Hello, connection established")

    def establishServer(self):
        server = WebsocketServer(host='127.0.0.1', port=8000, loglevel=logging.INFO)
        server.set_fn_new_client(self.new_client)
        server.run_forever()