import requests
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

url = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'

text = requests.get(url).text
raw_text = ' '.join(set(text.split())) # избавляемся от дубликатов
print(raw_text)


tokenized_text = nltk.word_tokenize(raw_text)
ttt = nltk.pos_tag(tokenized_text, tagset='universal')

tag_fd = nltk.FreqDist(tag for (word, tag) in ttt) # частота распределения
res = tag_fd.most_common() # сортировка от большего к меньшему
print(dict(res))
  

# 692 - существительные
# 268 - глаголы
# 199 - прилагательные
# 101 - наречия
# 57 - предлоги