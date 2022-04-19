from youtubesearchpython import *
import vlc
import random
import pafy
import time

class video:
    def __init__(self, keyword):
        self.list = []
        self.keyword = keyword
        if(keyword == "adventurous"):
            self.allSearch = Search('{0} places to go'.format(self.keyword))
        if(keyword == "sad"):
            self.allSearch = Search('Cute cat videos')
        for i in range(5):
            self.list.append(self.allSearch.result()['result'][i]['link'])
    
    def videoDisplay(self):
        count = 0
        url = str(random.choice(self.list))
        video = pafy.new(url)
        best = video.streams[0]
        media = vlc.MediaPlayer(best.url)
        media.play()
        while(count < video.length):
            time.sleep(1)
            count+=1
            if(input("> ").lower() == "stop"):
                break

if __name__ == '__main__':
    vid = video("sad")
    vid.videoDisplay()
