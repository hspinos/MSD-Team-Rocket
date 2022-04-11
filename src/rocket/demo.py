from Web import *
from bookParser import *
from eliza.eliza import *
'''  
      |         _________    _______       ________      _____ ______           ________      ________      ________      ___  __        _______       _________ 
     / \       |\___   ___\ |\  ___ \     |\   __  \    |\   _ \  _   \        |\   __  \    |\   __  \    |\   ____\    |\  \|\  \     |\  ___ \     |\___   ___\
    / _ \      \|___ \  \_| \ \   __/|    \ \  \|\  \   \ \  \\\__\ \  \       \ \  \|\  \   \ \  \|\  \   \ \  \___|    \ \  \/  /|_   \ \   __/|    \|___ \  \_| 
   |.o '.|          \ \  \   \ \  \_|/__   \ \   __  \   \ \  \\|__| \  \       \ \   _  _\   \ \  \\\  \   \ \  \        \ \   ___  \   \ \  \_|/__       \ \  \  
   |'._.'|           \ \  \   \ \  \_|\ \   \ \  \ \  \   \ \  \    \ \  \       \ \  \\  \|   \ \  \\\  \   \ \  \____    \ \  \\ \  \   \ \  \_|\ \       \ \  \ 
   |     |            \ \__\   \ \_______\   \ \__\ \__\   \ \__\    \ \__\       \ \__\\ _\    \ \_______\   \ \_______\   \ \__\\ \__\   \ \_______\       \ \__\
 ,'|  |  |`.           \|__|    \|_______|    \|__|\|__|    \|__|     \|__|        \|__|\|__|    \|_______|    \|_______|    \|__| \|__|    \|_______|        \|__|
/  |  |  |  \  
|,-'--|--'-.|   

'''

logging.basicConfig()
webScraper = Web("Sad")
parser = bookParser(webScraper.bookUrl())
parser.reduceSoup()
parser.initList()
main_ = Main(parser.printBook())

