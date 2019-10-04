class relay:
    def __init__(self):
        self.relayId = 0
        self.circuitIdList = []
        self.circuitBandList = []
        
    def sendRelayInfo():
        TCP_IP = '127.0.0.1'   #locaolhost for now, relay server ip for real calculation
        TCP_PORT = 3490
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = self.circuitToString()
        s.connect((TCP_IP, TCP_PORT))
        s.sendall(msg)
        
        
    def circuitsToString(self):
        msg = ""
        for circuitId, circuitBand in zip(self.circuitIdList, self.circuitBandList):
            msg+="I"
            msg+=str(circuitId)
            msg+="B"
            msg+=str(circuitBand)
            msg+="&"
        msg = msg[:-1]
        return msg
        
            
            
    def circuitsFromString(self,msg):
        self.circuitIdList = []
        self.circuitBandList = []
        infoList = msg.split('&')
        for info in infoList:
            
            i = info.find('I')
            b = info.find('B')
            circuitid = info[i+1:b]
            band = info[b+1:]
            self.circuitIdList.append(int(circuitid))
            self.circuitBandList.append(int(band))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        