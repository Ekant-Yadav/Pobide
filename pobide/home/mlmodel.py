
# def biases(news):
#     return "biases"

import wikipedia, pickle, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from wikipedia.exceptions import DisambiguationError, PageError
from wikipedia.wikipedia import summary

class MisinformationDetector():
	def __init__(self):
		self.model = None
		self.tV = None

	def train(self):
		print ("Program Log: Training has begun.")
		
		self.data = pd.read_csv(r'home/train.csv')
		self.data = self.data.dropna(how='any',axis=0)

		self.tV = TfidfVectorizer(stop_words='english', max_df=0.7)

		
		lb = self.data.label
		x_train,x_test,y_train,y_test=train_test_split(self.data['text'], lb, test_size=0.2, shuffle=True, random_state=7)
		train=self.tV.fit_transform(x_train) 

		test=self.tV.transform(x_test)

		self.model=PassiveAggressiveClassifier(early_stopping=True, warm_start=True)
		self.model.fit(train,y_train)
		y_predict=self.model.predict(test)
		score=accuracy_score(y_test,y_predict)

		print ('Program Log: Model has been trained on the dataset.')
		print ("The accuracy is:",round(score*100,2))

		print (confusion_matrix(y_test,y_predict, labels=[1,0]))

	def save(self):
		#saving model
		if not self.model:
			raise TypeError('Model is of type None. Please define by training the model first.')
		filename = 'Pickled_Misinformation_PAC_Model'
		with open(filename, 'wb') as file:  
			pickle.dump(self.model, file)
		print ('Program Log: Model successfully saved.')
		
		#saving vectorizer
		if not self.tV:
			raise TypeError('Vectorizer is of type None. Please define by training the model first.')
		filename = 'Pickled_Misinformation_TFIDF_Vectorizer'
		with open(filename,'wb') as file:
			pickle.dump(self.tV,file)
		print ('Program Log: Vectorizer successfully saved.')

	def load(self):
		#Loading PAC model
		try:
			with open('Pickled_Misinformation_PAC_Model', 'rb') as file:  
				self.model = pickle.load(file)
			# print ('Program Log: Model successfully loaded.')
		except FileNotFoundError:
			print ('Program Log: File not loaded because file was not found.')
		
		#Loading TFIDF Vectorizer
		try:
			with open('Pickled_Misinformation_TFIDF_Vectorizer', 'rb') as file:  
				self.tV = pickle.load(file)
			# print ('Program Log: Vectorizer successfully loaded.')
		except FileNotFoundError:
			print ('Program Log: File not loaded because file was not found.')

	def think(self,string):
		if not self.model or not self.tV:
			raise TypeError('Model or Vectorizer is of type None. Please define by training or loading the model first.')
		# print ('Program Log: Model has predicted',self.model.predict(self.tV.transform([string])))
		return(self.model.predict(self.tV.transform([string])))
	
	def search(self,news):
		try:
			term = wikipedia.suggest(news)
			if term == None:
				return ("1"+wikipedia.summary(news))
			return ("2"+wikipedia.page(title=term).url)
		except PageError:
			return ("1Page not found")
		except DisambiguationError:
			return ("1Too many results for page or query too vague")

# news="Last year a mysterious shipment was caught smuggling Coronavirus from Canada. It was traced to Chinese agents working at a Canadian lab. Subsequent investigation by GreatGameIndia linked the agents to Chinese Biological Warfare Program from where the virus is suspected to have leaked causing the Wuhan Coronavirus outbreak. The findings of this investigation has been corroborated by none other than the Bioweapons expert Dr. Francis Boyle who drafted the Biological Weapons Convention Act followed by many nations. The report has caused a major international controversy and is suppressed actively by a section of mainstream media."



def verification(news):
    APP = MisinformationDetector()
    APP.load()
    return APP.think(news)

def wiki(news1):
	APP1 = MisinformationDetector()
	return APP1.search(news1)