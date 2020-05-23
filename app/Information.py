import Client
from time import sleep

class Info:
    def __init__(self,ip,host):
        self.connection= Client.Socket()
        self.ip=ip
        self.host=host
        self.memoryInstaled=0
        self.networkInfo=0
        self.cpuTemperature=0
        self.memoryTemp=0
        self.memoryUsage=0
        self.fanSpeed=0
        self.cpuAvgUsage=0
        self.diskInfo=0
        self.diskFreeSpace=0
        self.networkSpeedUpload=0
        self.networkSpeedDownload=0
        self.data={}
        self.connected=False

    def connect(self):
        self.connection.connect(self.ip,self.host)
    def disconnect(self):
        self.connection.disconnect()

    def request(self, user, notifier):
        self.connection.request(user,notifier) #s-a efectuat conexiunea
        self.getDataFromClient()

    def getDataFromClient(self):
        sleep(3)
        self.data=self.connection.getData()
        if(self.connected==False):
            self.parseDataOneTime()
            self.connected=True
        else:
            self.parseData()

    def parseDataOneTime(self):
        self.memoryInstaled=self.data['memoryInstaled']
        self.networkInfo=self.data['networkInfo']['AF_INET1']['IP Address']
        self.diskInfo=self.data['diskInfo']['Disk0']['Total Size']
        self.diskFreeSpace=self.data['diskInfo']['Disk0']['Free']

    def parseData(self):
        self.cpuTemperature=self.data['cpuTemp']['CpuAVG1']
        self.memoryTemp=self.data['memoryTemp']['Memory0']
        self.memoryUsage=self.data['memoryUsage']['MemoryPercent']
        self.fanSpeed=self.data['fanSpeed']['Fan0']
        self.networkSpeedUpload=self.data['networkSpeed']['Send speed']
        self.networkSpeedDownload=self.data['networkSpeed']['Recive speed']
        self.cpuAvgUsage=self.data['cpuavgpercent']

    def getDataRepeat(self):
        return self.cpuTemperature,self.memoryTemp,self.memoryUsage,self.fanSpeed,self.networkSpeedUpload,self.networkSpeedDownload,self.cpuAvgUsage

    def getDataOnce(self):
        return self.memoryInstaled,self.networkInfo,self.diskInfo,self.diskFreeSpace

    def getCPUTemp(self):
        return float(self.cpuTemperature)

    def getAvgUsage(self):
        return self.cpuAvgUsage
   
    def getMemoryUsage(self):
        return float(self.memoryUsage)

if __name__=="__main__":
    info = Info('192.168.2.169', 8080)
    info.connect()
    #info.request("cristian.pal93@e-uvt.ro", 0)
    a = info.getDataOnce()
    print(a)
    while True:
        sleep(10)
        #info.request("cristian.pal93@e-uvt.ro", 0)
        b = info.getDataRepeat()
        print(b)
        print(a)
