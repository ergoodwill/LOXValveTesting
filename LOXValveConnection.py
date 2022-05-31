import Constants
import websocket


class LOXValveConnection:
    @staticmethod
    def establishConnection():
        websocket.enableTrace(True)
        ws = websocket.WebSocket()
        ws.connect(Constants.CONNECTION_URL)
        ws.send("Hello, Server")
        print(ws.recv())
        ws.close()

    @staticmethod
    def measureFlowRate(pressureDiff, pressure):
        # TODO: send pressureDiff and pressure via ws to LOX valve and receive flow rate in response from ws,
        #  return this
        return 2
