# Entity Linking Model with Bi-LSTM CRF NER
Entity linking (EL) refers to the task of recognizing mentions of specific entities in text and assigning unique identifiers to them from an underlying knowledge repository.
With this model, Users can obtain the Wikipedia's page for certain entity in an article.

### Overview of this work
* Explorative Analysis
* Bi-LSTM CRF NER model
* REL Entity Disambiguity model

### Explorative work
Before apply any machine learning models, the explorative analysis is imperative needed to understand on our data. The data is crawlled from a daily local newspaper website. To fully understand the categories and content of news, the LDA Mallet has been used to extract topics.

Further, to visualize the ditribution of sections in an interective environment. The dash API has been utilized to visualize the distribution of sections. The user are able to  choose a main category and see the distriution of sub-categories. 

### Named Entity Recognition using multi-layered bidirectional LSTMs and Word2vec embeddings
Named Entity Recognition is a classification problem of identifying the names of people,organisations,etc (different classes) in a text corpus. I have implemented a 2 layer 
bidirectional LSTM with CRF layer network using Keras. 

#### Word Embedding and Bi-LSTM
Sentences are used as inputs for the recurrent neural network. I used pre-trained 300d word2vec to represent each word in vector space.  
The model is built by one Bi-lstm layer with 300d dimension and 0.2 dropout rate, and one lstm layer with 300d dimension and 0.5 dropout rate. 

#### CRF
I added CRF layer because softmax classifier produces a probability distribution for the different tags for each token in the sentence. In this approach, 
each token in a sentence is considered independently and correlations between tags in a sentence cannot be taken into account. CRF classifier is able to maximize
the tag probability of the complete sentence. This is especially helpful for tasks with strong dependencies. 


