import subprocess
import transmissionrpc

TRANSMISSION_USER = 'USERNAME'
TRANSMISSION_PASSWORD = 'PASSWORD'

class Temperature:
    def get(self, params):
        list = subprocess.Popen(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE)
        out = list.communicate()
        return float(out[0].strip())/1000

class Torrents:
    def __init__(self):
        self.client = transmissionrpc.Client('localhost', port=9091, user = TRANSMISSION_USER, password = TRANSMISSION_PASSWORD)
        
    def getTorrent(self, torrent):
        return {'name': str(torrent.name), 'status': torrent.status, 'progress': torrent.progress, 'eta': str(torrent.eta)}
        
    def get(self, params):
        torrents = self.client.get_torrents()
        result = []
        for torrent in torrents:
            result.append(self.getTorrent(torrent))
        return result