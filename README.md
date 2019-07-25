# Text-Generation
This repository is intended to provide support and guidance to all those who are looking for simple yet introduce all major aspects of Deep learning with Recurrent Neural Networks.
Text generation is an important division in AI. This is because it allows the machine to pick up patterns across different pieces of text. For example, a model trained over a number of C++ programs learns that it need to open a curly braces after a function header and that every opening brace should have a closing brace as well. Similarly when trained on Shakespeare's writings, the model picks up the English words and grammar of Shakespearan era.

## Application
Efficient text generation models along with other Natural language processing tools can be used to improve responses of voice assistants. The AI machine can answer in a local dialect which can be better understood by people. This will help bring AI much more closer to humans.

## Model
Text Generations is done as either character level modelling or word level modelling. In character level modelling, the model reads a line of text of a constant length and tries to predict the next character. The window is then shifted by a unit to generate longer sequences. Here in my project,I am using random sampling technique to pick the next character after training is completed.

## Things Learnt
1. Sampling sentences from text data
2. Vectorise a sentence into numpy array
3. Generate text through random sampling with Normal distribution
4. Implementing Callbacks in Keras
