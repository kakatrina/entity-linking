# Entity Linking Model with Bi-LSTM CRF NER
Entity linking (EL) refers to the task of recognizing mentions of specific entities in text and assigning unique identifiers to them from an underlying knowledge repository.
With this model, Users can obtain the Wikipedia's page for certain entity in an article.

### Overview of the model
* Bi-LSTM CRF NER model
* REL Entity Disambiguity model

### Named Entity Recognition using multi-layered bidirectional LSTMs and Word2vec embeddings
Named Entity Recognition is a classification problem of identifying the names of people,organisations,etc (different classes) in a text corpus. I have implemented a 2 layer 
bidirectional LSTM with CRF layer network using Keras. 

#### Word Embedding
Sentences are used as inputs for the recurrent neural network. I used pre-trained 300d word2vec to represent each word in vector space. 

#### Bi-LSTM 
The model is built by one Bi-lstm layer with 300d dimension and 0.2 dropout rate, and one lstm layer with 300d dimension and 0.5 dropout rate. 

#### CRF
I added CRF layer because softmax classifier produces a probability distribution for the different tags for each token in the sentence. In this approach, 
each token in a sentence is considered independently and correlations between tags in a sentence cannot be taken into account. CRF classifier is able to maximize
the tag probability of the complete sentence. This is especially helpful for tasks with strong dependencies. 


