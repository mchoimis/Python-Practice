""" WordNet Interface
this is a line-by-line command
See http://nltk.googlecode.com/svn/trunk/doc/howto/wordnet.html
"""

# Importing nltk
# Importing wordnet as a dictionary

from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn

# Words
wn.synsets('dog')
wn.synsets('dog', pos=wn.VERB)
wn.synset('dog.n.01').definition
wn.synset('dog.n.01').examples
wn.synset('dog.n.01').lemmas
[lemma.name for lemma in wn.synset('dog.n.01').lemmas]
wn.lemma('dog.n.01.dog').synset

# Synsets
dog = wn.synset('dog.n.01')
dog.hypernyms()
dog.member_holonyms()
dog.root_hypernyms()

good = wn.synset('good.a.01')
good.antonyms() #antonyms are not installed
good.lemmas[0].antonyms()

# Lemmas
eat = wn.lemma('eat.v.03.eat')
eat
eat.key
eat.count()
wn.lemma_from_key(eat.key)
wn.lemma_from_key(eat.key).synset

# Similarity
dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')

# Return a score denoting how similar two word senses are, based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy.
# The score is in the range 0 to 1, except in those cases where a path cannot be found (will only be true for verbs as there are many distinct verb taxonomies),
# in which case -1 is returned.
# A score of 1 represents identity i.e. comparing a sense with itself will return 1.

dog.path_similarity(cat)
