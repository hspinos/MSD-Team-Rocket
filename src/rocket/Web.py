from bs4 import BeautifulSoup
import logging
import requests

'''
pip install google
pip install beautifulsoup4
pip install requests
'''

class Web:
    def __init__(self, keyword):
        self.keyword = keyword.lower()
        self.listForBooks = {"adventurous" : "https://www.booksamillion.com/summer-reading2?oxid=1162&oxname=summereadinglist&oxpage=summeradventure&oxpos=module2&oxdate=050621",
                             "happy" : "https://www.booksamillion.com/50bookstoreadbefore5",
                             "sad" : "https://www.booksamillion.com/personalgrowth?oxid=1777&oxname=personalgrowth&oxpage=consciousliving&oxpos=module3&oxdate=121420",
                             "love" : "https://www.booksamillion.com/romance",
                             "sci-Fi" : "https://www.booksamillion.com/scifi"}
        self.listForIMDB = {"adventurous" : "https://www.imdb.com/search/title/?genres=adventure&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=fd0c0dd4-de47-4168-baa8-239e02fd9ee7&pf_rd_r=AXGX0PGTGFTVN65B1RXV&pf_rd_s=center-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr4_i_2",
                            "happy" : "https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=AXGX0PGTGFTVN65B1RXV&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1",
                            "sad" : "https://www.imdb.com/search/title/?genres=drama&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f1cf7b98-03fb-4a83-95f3-d833fdba0471&pf_rd_r=AXGX0PGTGFTVN65B1RXV&pf_rd_s=center-3&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr3_i_1",
                            "love" : "https://www.imdb.com/search/title/?genres=romance&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r=AXGX0PGTGFTVN65B1RXV&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_1",
                            "sci-Fi" : "https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=AXGX0PGTGFTVN65B1RXV&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_2"}

    def bookUrl(self):
        try:
            webUrls = requests.get(self.listForBooks[self.keyword]).text
            Soup = BeautifulSoup(webUrls, 'lxml')
            return(Soup)

        except Exception as e:
            print(e)

    def imdbUrl(self):
        try:
            webUrls = requests.get(self.listForIMDB[self.keyword]).text
            Soup = BeautifulSoup(webUrls, 'lxml')
            return(Soup)
        except Exeception as e:
            print(e)

        
if __name__ == "__main__":
    web = Web("sad")
    web.bookUrl()

