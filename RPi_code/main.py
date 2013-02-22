import serial
import time
from handlers import TempHandler
from handlers import TorrentHandler 

class SerialStats:
    def __init__(self):
        self.serial = serial.Serial('/dev/ttyACM0', 9600, timeout = 3)
        time.sleep(2)    #wait for the Serial to initialize
        self.serial.write('Starting...')
        self.modules = [TempHandler(), TorrentHandler()]
    
    def run(self):
        curr = 0
        while True:
            c = self.serial.read(1)
            if( c == '1'):	# '1' is to scroll through the list
                curr += 1
                if(curr >= len(self.modules)):
                    curr=0
            elif (c == '2'):	# '3' is to enter in to a list item
                self.modules[curr].handle(self.serial)
            
            self.serial.write(self.modules[curr].get_stat())

if __name__ == "__main__":
    SerialStats().run()
