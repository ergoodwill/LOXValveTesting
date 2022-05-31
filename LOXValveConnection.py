import Constants
import websocket

class LOXValveConnection:
    def establishConnection(self):
        pass
        # self.ws = create_connection(Constants.CONNECTION_URL)
        # print(self.ws.recv())
        # print("Sending 'hello'")
        # self.ws.send("hello")
        # self.ws.close()

    def measureFlowRate(self, pressureDiff, pressure):
        #TODO
        return 2