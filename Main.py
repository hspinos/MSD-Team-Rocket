from WebScraper import *
from bookParser import *
from Web import *

#create web scraper object with specified URL
webScraperHorror = WebScraper("https://www.booksamillion.com/horrorbooks#")
webScraperMythology = WebScraper("https://www.booksamillion.com/mythology")
webScraperThriller = WebScraper("https://www.booksamillion.com/thrillers")
webScraperRomance = WebScraper("https://www.booksamillion.com/romance")

webScraperActionMovie = WebScraper("https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r=D1AXA5Y62P6TWDB9QFBR&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_2")

#create book parser with Soup object returned from web scraper
bookParser = bookParser(webScraperHorror.getHTML())
bookParser.reduceSoup()
bookParser.initList()
for i in bookParser.bookList:
    print(i.title + "\n")
    print(i.author + "\n")
    print(i.price + "\n")

#bookParser = movieParser(webScraperActionMovie.getHTML())
#bookParser.reduceSoup()
#bookParser.initList()
#for i in bookParser.bookList:
#    print(i.title + "\n")
#    print(i.author + "\n")
#    print(i.price + "\n")

