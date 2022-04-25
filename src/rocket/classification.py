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

class keyword:

    def __init__(self):
        self.input = ""
        # create the list's for each emotion include the word itself
        self.sad = ["sad"]
        self.sad += synonyms("sad")
        self.happy = ["happy"]
        self.happy += synonyms("happy")
        self.fear = ["fear"]
        self.fear += synonyms("fear")
        self.disgust = ["disgust"]
        self.disgust += synonyms("disgust")
        self.anger = ["anger"]
        self.anger += synonyms("anger")
        self.surprise = ["surprise"]
        self.surprise += synonyms("surprise")
        self.adventurous = ["adventurous"]

        self.emotions = [self.sad, self.happy, self.fear, self.disgust, self.anger, self.surprise, self.adventurous]

    def compareInput(self):
        if(len(self.input) > 0):
            inputUse = self.input.split()
            for word in inputUse:
                for emotion in self.emotions:
                    for synonym in emotion:
                        if word in synonym:
                            return str(emotion[0])







# answer = input("how are you feeling ")
# k = keyword(answer)
# print(k.compareInput())