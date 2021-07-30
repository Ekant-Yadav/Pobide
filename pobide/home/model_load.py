import tensorflow as tf
from transformers import AutoTokenizer
import numpy as np
import re
from time import time

class Biases():
    def __init__(self):
        self.model = None
        self.SEQ_LEN = 350
        self.labels = ['Conservative','Liberal', 'Neutral']


    def load(self, model_path):
      self.model = tf.saved_model.load(model_path)

    def clean_text(self, text):
        text = re.sub(r'[^a-zA-Z\']', ' ', text)
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        text = text.lower()
        return text

    def tokenize(self,sentence):
        tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        tokens = tokenizer.encode_plus(sentence, max_length=self.SEQ_LEN,
                                    truncation=True, padding='max_length',
                                    add_special_tokens=True, return_attention_mask=True,
                                    return_token_type_ids=False, return_tensors='tf')
        return tokens

    def predict(self, statement):
        if not model:
            print('Model is of type NONE, Please load the model.')

        else:
            statement = self.clean_text(statement)
            sentence = self.tokenize(statement)
            pred_class = self.model([sentence['input_ids'], sentence['attention_mask']], False, None)
            pred_class = np.argmax(pred_class, axis = 1)
            print("Model Prediction is : ", self.labels[pred_class[0]])
            return self.labels[pred_class[0]]
            
statement = 'some text'
model = Biases()
model.load('./saved_model/')
model.predict(statement)