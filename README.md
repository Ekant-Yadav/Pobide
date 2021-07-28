# PoBiDe.Ai


PoBiDe.Ai is a project aimed to address the problem of fake information and bias in news. It uses advanced natural language processing and machine learning algorithms to automate the detection of fake news and political bias.

The namesake of PoBiDe comes from the first two letters of every word in "Political Bias Detector"; pair this with artificial intelligence, and you have our name, "PoBiDe.Ai".


# Inspiration:

The pandemic took the world by storm. It pillaged our healthcare systems and caused millions of deaths. But if there were one thing to take out of it, it would be the effect of fake and biased news on the population.

Though the problem of fake/biased news may be too hard for humans to solve, computers aren’t out of the question. We can use machine learning models to automate the detection of fake and politically biased news, and hopefully stop it.

# What it Does:

The finished product is a fully functioning website. On the site, you enter a piece of text into a textbox, and then click verify to check the reliability of the text. Once the verify button is pressed, the site will state whether the text is fake, and the political bias of the text.


# How we built it:

Though the website design seems relatively simple, the inner workings of the program are not as much. To detect fake news we used Sci-kit Learn’s [Passive-Aggressive Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html), and for political bias, we used a fine-tuned version of Google’s [Bidirectional Encoder Representations from Transformers](https://github.com/google-research/bert) (BERT) hooked up to a long short term memory(LSTM) layer attached to a standard fully connected(FC) layer. Through a vast amount of testing, these models had the best accuracy on test datasets.

As one may see, there are two parts to this problem, each requiring two detectors, a Misinformation, and Political Bias Detector. 

The Misinformation Detector uses a [TF-IDF Vectorizer](https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a) to transform the dataset into a way that can be processed by the model, or a sparse matrix of TF-IDF features. The model and vectorizer are trained and saved onto pickled files. The model and vectorizer can be loaded and can predict text inputs in split-second time.

The political bias detector uses Google’s BERT to transform data. This transformed data is then fed into an LSTM layer which feeds its output into an FC layer, which classifies the data.








# Challenges we ran into:

There are not a lot of publicly available political bias datasets on the web. Our team spent a good chunk of time finding and preparing datasets for usage. After a ton of time and research, we found the [Ideological Book Corpus](https://people.cs.umass.edu/~miyyer/ibc/index.html), a dataset with 4062 individual labeled text samples. Though we found the dataset at the end, it proved hard to obtain.

Another challenge was the accuracy of the Misinformation Detector. Though it regularly achieved >99% accuracy, testing proved otherwise. The team eventually found the problem within the dataset, each factual news site had a label with the news site written on it, and the same news site was in almost all of the factual news examples, and nearly none of the fake news sources. By simply guessing based on the tag on the factual news sources, you would achieve a >99% accuracy. We tried to stop this problem by removing all of the tags, but the dataset still did not work very well. Then, as a last resort, we changed the dataset to a smaller but more accurate one.

The political bias detector also had its fair share of problems. We first tried to implement a similar approach to the misinformation detector but found that it had low accuracy of 48-56%. Then, we implemented a Multi-layer Perceptron Classifier with [fastText](https://fasttext.cc/) word embeddings, but the result was not much higher. Other word embeddings like [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) and [GloVe](https://nlp.stanford.edu/projects/glove/) also had similar accuracy. (word embeddings implemented with sci-kit learn via [Zeugma](https://github.com/nkthiebaut/zeugma)) We concluded that to detect political bias, we needed something deeply bidirectional, and Google’s BERT was a fit. In order to classify data, we added an LSTM layer attached to an FC layer, which yielded a 96% accuracy.




# Accomplishments We’re Proud Of:

We're proud of the massive amount of work and dedication put into this project. This was our first time creating and deploying a machine learning system with multiple models. This was also our first time using a fine-tuned BERT.






# What’s Next for PoBiDe.ai?

We have big goals. One feature that we hope to add in the future is the ability for users to provide data to train the model. This will make the model more accurate and versatile. One key feature needed is to add user accounts to the website, making it harder for people to sway the results.

Another goal is to make it so that the model can predict on audio recordings and images. This will make the model more convenient for the end-user.

