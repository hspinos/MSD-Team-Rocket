from Web import Web
from nltk.corpus import wordnet
import requests
from bs4 import BeautifulSoup


# function that grabs synonyms for words from thesaurus.com
def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in
            soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]  # 'css-1gyuw4i eh475bn0' for less relevant synonyms


# create the list's for each emotion include the word itself
sad = ["sad"]
sad += synonyms("sad")
happy = ["happy"]
happy += synonyms("happy")
fear = ["fear"]
fear += synonyms("fear")
disgust = ["disgust"]
disgust += synonyms("disgust")
anger = ["anger"]
anger += synonyms("anger")
surprise = ["surprise"]
surprise += synonyms("surprise")

emotions = [sad, happy, fear, disgust, anger, surprise]


class keyword:

    def __init__(self, feeling):
        self.feeling = feeling

    def compareInput(self):
        for i in emotions:
            for n in i:
                if self.feeling in n:
                    print("found " + n)
                    return str(n)


answer = input("how are you feeling")
k = keyword(answer)
k.compareInput()

