# -*- coding: utf-8 -*-
"""Text Generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ngDzISz4t8BF9E1nkczTKAQ1AWIhC8HD
"""

# Run this cell to mount your Google Drive.
from google.colab import drive
drive.mount('/content/drive')

# import the modules
import io
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense,LSTM
from keras.callbacks import LambdaCallback

# load the text into a string text
# here, cp1252 encoding scheme is used
path = "drive/My Drive/Datasets/alice in wonderland.txt"
with io.open(path, encoding='cp1252') as f:
    text = f.read().lower()

# the size of the input text
print(len(text))

# let us fix input sentence length to maxlen
# create a number of sample sentence with the next characters as output
maxlen = 40
step =3
sentences= []
out_chars=[]
for i in range(0,len(text)-maxlen,step):
  sentences.append(text[i:i+maxlen])
  out_chars.append(text[i+maxlen])
print("No of samples= ",len(sentences))

# a glimpse of the sampling
for i in range(20):
  print(sentences[i],' ',out_chars[i])

# the set of all characters used in text
list_chars=list(set(text))
print(list_chars)

# count of dictionary to be created
print(len(list_chars))

# create two dictionaries mapping characters to indices and vice versa
char2ind=dict()
ind2char=dict()
for i in range(len(list_chars)):
  ch=list_chars[i]
  char2ind[ch]=i
  ind2char[i]=ch

char2ind.items()

print(char2ind['a'])

print(ind2char.items())

print(ind2char[31])

# vectorise the input samples using numpy arrays
x = np.zeros((len(sentences),maxlen,len(list_chars)),dtype=np.bool)
y = np.zeros((len(sentences),len(list_chars)),dtype=np.bool)

# using dictionary to convert sample sentences into numpy arrays
for i,sentence in enumerate(sentences):
  for j,char in enumerate(sentence):
    x[i,j,char2ind[char]]=True
  y[i,char2ind[out_chars[i]]]=True

print(x[0])

print(x[0,0])

print(y[0])

print(type(x))

# build the model
model=Sequential()
model.add(LSTM(128,input_shape=(maxlen,len(list_chars))))
model.add(Dense(len(list_chars),activation='softmax'))

# generate text
def gen_text(epochs,_):
  seed=random.randint(0,len(text)-maxlen)
  base=text[seed:seed+maxlen]
  print("Base sentence ",base,end='....')
  for i in range(200):
    test_x=np.zeros((1,maxlen,len(list_chars)))
    for j,char in enumerate(base):
      test_x[0,j,char2ind[char]]=1.0
    res=model.predict(test_x)[0]
    res=np.asarray(res).astype('float64')
    res/=np.sum(res)
    res=np.random.multinomial(1,res,1)
    test_y=ind2char[np.argmax(res)]
    base=base[1:]+test_y
    print(test_y,end='')
  print()

cb_print=LambdaCallback(on_epoch_end=gen_text)

model.compile(loss='categorical_crossentropy',optimizer='adam')

model.fit(x,y,epochs=2,batch_size=64,callbacks=[cb_print])

