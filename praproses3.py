from bs4 import BeautifulSoup as bs
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.moses import MosesDetokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
import os
import csv
import pprint
import numpy as np
import pandas as pnd

stop_words = set(stopwords.words('english'))
detokenizer = MosesDetokenizer()
lemmatizer = WordNetLemmatizer()
filelabelTest = "Label/TestingLabel.txt"
filelabelTrain = "Label/TrainingLabel.txt"
labelTest = pnd.read_csv(filelabelTest, delim_whitespace=True)
labelTrain = pnd.read_csv(filelabelTrain, delim_whitespace=True)
#Diubah ke matriks
labelTest = np.matrix(labelTest)
labelTrain = np.matrix(labelTrain)
# print(labelTrain)
# print(labelTest)
datasetTrain = []
label = []
output = []
fileName = './PrePrecessingTraining.csv'

for i in range(len(labelTrain)):
	soup = bs(open("Training/"+ str(labelTrain[i,0])+".xml",'r').read(),'html.parser')

	headline = soup.find("headline").get_text().replace('\n','')
	paragraph = soup.find("text").get_text().replace('\n','')
	label = int((labelTrain[i,1]) == "YES")
	datasetTrain.append([[str(headline)],[str(paragraph)],label])
# ==================================================
# Case Folding
tmp0 = []
tmp1 = []
for i in range(len(datasetTrain)):
	# print(datasetTrain[i][0])
	# print(datasetTrain[i][1])
	tmp0.append(datasetTrain[i][0])
	tmp1.append(datasetTrain[i][1])
# print(tmp0)
# print(tmp1)
for i in range(len(tmp0)):
	valsLower = [item.lower() for item in tmp0[i]]
	tmp0[i] = valsLower
# print(tmp0)
for i in range(len(tmp1)):
	valsLower1 = [item.lower() for item in tmp1[i]]
	tmp1[i] = valsLower1
# print(tmp1)

# ==================================================
#Remove Punctuation
for p in list(punctuation):
	for i in range(len(tmp0)):
		valsPunc0 = [item.replace(p, '') for item in tmp0[i]]
		tmp0[i] = valsPunc0
	for i in range(len(tmp1)):
		valsPunc1 = [item.replace(p, '') for item in tmp1[i]]
		tmp1[i] = valsPunc1
# print("INI PUNC 1",tmp0)
# print("INI PUNC 2",tmp1)
# ==================================================
# Tokenize
for i in range(len(tmp0)):
	valsToken = [word_tokenize(item) for item in tmp0[i]]
	tmp0[i] = valsToken
# print(tmp0)
for i in range(len(tmp1)):
	valsToken1 = [word_tokenize(item) for item in tmp1[i]]
	tmp1[i] = valsToken1
# print("TOKEN 33",tmp0)
# print("TOKEN 1",tmp1)
# ==================================================
# Stop Word Removal
FilteredSentences0 = []
FilteredSentences1 = []
for j in range(len(tmp0)):
	# print(j)
	for item in tmp0[j]:
		# print(item)
		item = " ".join(item)
		FilteredSentences0.append([item])
temp0 = []
for i in range(len(FilteredSentences0)):
	for item in FilteredSentences0[i]:
		temp0.append(item)

for j in range(len(tmp1)):
	# print(j)
	for item in tmp1[j]:
		# print(item)
		item = " ".join(item)
		FilteredSentences1.append([item])
temp1 = []
for i in range(len(FilteredSentences1)):
	for item in FilteredSentences1[i]:
		temp1.append(item)
stopWordRemov0 = []
stopWordRemov0 = [w for w in temp0 if not w in stop_words]
stopWordRemov1 = []
stopWordRemov1 = [w for w in temp1 if not w in stop_words]
# print("stopwords",stopWordRemov0)
# print("stopwords",stopWordRemov1)
# ==================================================
# Stemming
stemmer = PorterStemmer()
hasilStem0 = []
hasilStem1 = []
for word in stopWordRemov0:
	# print(stemmer.stem(word))
	hasilStem0.append(stemmer.stem(word))
for word in stopWordRemov1:
	# print(stemmer.stem(word))
	hasilStem1.append(stemmer.stem(word))
# print(hasilStem0)
# print("hasil stem",hasilStem1)
# ==================================================

# Memberi Label
for i in range(len(hasilStem0)):
	output.append([hasilStem0[i],hasilStem1[i],datasetTrain[i][2]])

# print(output)

# for i in range(len(output)):
# 	print(output[i])


with open(fileName, "w") as resultFile:
	wr = csv.writer(resultFile, delimiter=';', lineterminator='\n')
	for line in output:
		wr.writerow(line)
print('finish')
