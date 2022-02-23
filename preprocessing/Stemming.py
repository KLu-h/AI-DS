from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer( )
text_example = "your text goes here"
words = word_tokenize (text_example)
for w in words :
 print(ps.stem(w))
