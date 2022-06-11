import gensim.downloader as api
model = api.load('word2vec-google-news-300')
vec_king = model['king']
print(vec_king)
print("-----------------------------------")
print(len(vec_king))
print("-----------------------------------")
print(model.similarity("car", "bus"))
print("-----------------------------------")
print(model.similarity("car", "sun"))
print("-----------------------------------")
print(model.similarity("man", "women"))
print("-----------------------------------")
print(model.most_similar(positive=["king", "man"], negative=["women"], topn=5))
print("-----------------------------------")
print(model.most_similar(positive=["king", "man"], negative=["women"], topn=5))
print("-----------------------------------")
print(model.most_similar(positive=["royal", "women", "crown"], topn=5))

