import wikipedia
from speek import say
print(wikipedia.summary("human", sentences =3))
print(say(wikipedia.search("hubble")))