import wikipedia
from textblob import TextBlob


def wiki(name="Indian Institute of Science", length=1):

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    results = wikipedia.search(name)
    return results


def phrase(name):
    material = wiki(name)
    blob = TextBlob(material)
    return blob.noun_phrases
