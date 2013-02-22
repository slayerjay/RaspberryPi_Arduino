from modules import Torrents
from modules import Temperature

class TorrentHandler:
    def __init__(self):
        self.module = Torrents()
        self.curr = 0
    
    def handle(self, ser):
        while True:
            torrents = self.module.get('')
            c = ser.read(1)
            if( c == '1'):	# '1' is to scroll through the list
                self.curr += 1
                if(self.curr >= len(torrents)):
                    self.curr=0
                
            elif (c == '2'):	# '2' is to exit from the list
                return
            
            ser.write(self.get_stat())
        
    def get_stat(self):
        torrents = self.module.get('')
        torrent = torrents[self.curr]
        return torrent['name'][:16] + '\nProgress: ' + str(torrent['progress']) + '%'
    
class TempHandler:
    def __init__(self):
        self.module = Temperature()
    
    def handle(self, ser):
        while True:
            c = ser.read(1)
            if( c == '1'):
                return
            elif (c == '2'):
                return
            
            ser.write(self.get_stat())
        
    def get_stat(self):
        temp = self.module.get('')
        return 'Temp: ' + str(temp) + ' C'
    