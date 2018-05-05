from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

#TrainingSet = "./PreProcessingTraining.csv"
#TestingSet = "./PreProcessingTesting.csv"

datasetTrain = []
labelTrain = []
with open('PrePrecessingTraining.csv') as resultFile:
	resultFile = resultFile.read().split("\n")
	for line in resultFile:
		line = line.split(";")
		try:
			datasetTrain.append(" ".join(line[0:-1]))
			labelTrain.append(str(line[-1]))
		except IndexError :
			continue
# print(datasetTrain)
# print(labelTrain)
# ==================================================

datasetTest = []
labelTest = []
with open('PrePrecessingTesting.csv') as resultFile:
	resultFile = resultFile.read().split("\n")
	for line in resultFile:
		line = line.split(";")
		try:
			datasetTest.append(" ".join(line[0:-1]))
			labelTest.append(str(line[-1]))
		except IndexError :
			continue

# print(datasetTest)
# print(labelTest)
# ==================================================
#Classifier 
count_vect = CountVectorizer()
Pembobotan = TfidfTransformer()
# ==================================================
# Naive Bayes

# Akurasi Data Train
MTrain = count_vect.fit_transform(datasetTrain)
TFIDFTrain = Pembobotan.fit_transform(MTrain)

klasifikasi = MultinomialNB().fit(TFIDFTrain, labelTrain)
prediksi = klasifikasi.predict(TFIDFTrain)
akurasi = 0
for i in range(len(labelTrain)):
	if labelTrain[i] == str(prediksi[i]):
		akurasi += 1

a=len(labelTrain)
b=akurasi
c=((float(b*100)/a)+1)
print("Akurasi : {} %".format(int(round(c))) )

# Akurasi Data Test

MTest = count_vect.fit_transform(datasetTest)
TFIDFTest = Pembobotan.fit_transform(MTest)

klasifikasi1 = MultinomialNB().fit(TFIDFTest, labelTest)
prediksi1 = klasifikasi1.predict(TFIDFTest)
akurasi1 = 0
for i in range(len(labelTest)):
	if labelTest[i] == str(prediksi1[i]):
		akurasi1 += 1

x=len(labelTest)
y=akurasi1
z=((float(y*100)/x)+1)

print("Akurasi : {} %".format(int(round(z))) )

# ==================================================
# SVM Classifier

# Akurasi Data Test
MTrain2 = count_vect.fit_transform(datasetTrain)
TFIDFTrain2 = Pembobotan.fit_transform(MTrain2)

klasifikasi2 = MultinomialNB().fit(TFIDFTrain2, labelTrain)
prediksi2 = klasifikasi.predict(TFIDFTrain2)
akurasi2 = 0
for i in range(len(labelTrain)):
	if labelTrain[i] == str(prediksi2[i]):
		akurasi2 += 1

u=len(labelTrain)
v=akurasi2
w=((float(v*100)/u)+1)
print("Akurasi : {} %".format(int(round(w))) )

# Akurasi Data Test

MTest3 = count_vect.fit_transform(datasetTest)
TFIDFTest3 = Pembobotan.fit_transform(MTest3)

klasifikasi3 = MultinomialNB().fit(TFIDFTest3, labelTest)
prediksi3 = klasifikasi3.predict(TFIDFTest3)
akurasi3 = 0
for i in range(len(labelTest)):
	if labelTest[i] == str(prediksi3[i]):
		akurasi3 += 1

e=len(labelTest)
f=akurasi3
g=((float(f*100)/e)+1)

print("Akurasi : {} %".format(int(round(g))) )