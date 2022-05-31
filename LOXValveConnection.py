import Constants
import websocket

class LOXValveConnection:
    def establishConnection(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocket()
        ws.connect(Constants.CONNECTION_URL)
        ws.send("Hello, Server")
        print(ws.recv())
        ws.close()

    def measureFlowRate(self, pressureDiff, pressure):
        #TODO:
        return 2