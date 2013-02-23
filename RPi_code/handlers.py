from modules import Torrents
from modules import Temperature

class TorrentHandler:
    def __init__(self):
        self.module = Torrents()
        self.curr = 0
    
    def handle(self, ser):
        ser.write('Please wait...')
        while True:
            torrents = self.module.get('')
            c = ser.readline().strip()
            if( c == '1'):    # '1' is to scroll through the list
                self.curr += 1
                if(self.curr >= len(torrents)):
                    self.curr=0
            elif (c == '11'):
                self.handle_torrent(ser)
            elif (c == '2'):
                return
            
            ser.write(self.get_stat())
        
    def get_stat(self):
        torrents = self.module.get('')
        torrent = torrents[self.curr]
        return torrent['name'][:16] + '\n' + '{0:.2f}'.format(torrent['progress']) + '% '+torrent['eta']+' '+torrent['status'][:1]
    
    def handle_torrent(self, ser):
        ser.write('Please wait...')
        while True:
            torrents = self.module.get_objects()
            torrent = torrents[self.curr]
            ser.write(torrent.name[:16]+ '\n'+torrent.status[:3] + ' Start/Stop')
            c = ser.readline().strip()
            if( c == '1'):    # '1' is to scroll through the list
                if(torrent.status == 'downloading'):
                    torrent.stop()
                    ser.write('Please wait...')
                    ser.write(self.get_stat())
                    return
                else:
                    torrent.start()
                    ser.write('Please wait...')
                    ser.write(self.get_stat())
                    return
            elif (c == '2'):
                return
        
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
    