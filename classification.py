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


class keyword:
    def __init__(self, feeling):
        self.feeling = feeling

    def compareInput(self):

        for i in sad:
            if self.feeling in i:
                print("a")
        for i in happy:
            if self.feeling in i:
                print("b")
        for i in fear:
            if self.feeling in i:
                print("c")
        for i in disgust:
            if self.feeling in i:
                print("d")
        for i in anger:
            if self.feeling in i:
                print("e")
        for i in surprise:
            if self.feeling in i:
                print("f")

answer = input("how are you feeling")
k = keyword(answer)
k.compareInput()
print(sad)
print(happy)
print(fear)
print(disgust)
print(anger)
print(surprise)

