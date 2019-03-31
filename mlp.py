import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
import random,pickle,time
from math import ceil
from word import batch_generator,data_generator
from sklearn.model_selection import train_test_split
from keras.regularizers import l2
from keras.callbacks import TensorBoard,ModelCheckpoint

from keras.layers import Dense,InputLayer,Dropout,LSTM,Convolution1D,Flatten,GlobalAveragePooling1D,MaxPool1D

NB_EPOCH = 30
BATCH_SIZE = 100
#梯度下降算法
OPTIMIZER = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
input_shape=0
lens=0
log_dir="./log/"

class MLP:
	@staticmethod
	def build(input_shape, classes):
		model = Sequential()
		model.add(Dense(32, input_shape=input_shape, activation="relu"))
		model.add(Dropout(0.2))
		model.add(Dense(32, activation="relu"))
		model.add(Dropout(0.2))
		model.add(Flatten())
		model.add(Dense(classes, activation="softmax"))
		return model

def train_mlp():
	for line in open("./file/INPUT_SHAPE"):
		input_shape=int(line)
		print(input_shape)
	INPUT_SHAPE=(input_shape,16)
	for line in open("./file/len"):
		lens=int(line)
		print(lens)
	data_size=ceil(lens//(BATCH_SIZE*NB_EPOCH))
	print(data_size)
	for line in open("./file/valid_len"):
		valid_lens=int(line)
		print(valid_lens)
	valid_size=ceil(valid_lens//(BATCH_SIZE*NB_EPOCH))
	print(valid_size)
	model = MLP.build(input_shape=INPUT_SHAPE, classes=3)
	print('1')
	model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
		metrics=["accuracy"])
	print('2')
	call=TensorBoard(log_dir=log_dir+"mlp",write_grads=True)
	checkpoint = ModelCheckpoint(filepath='bestmlp',monitor='val_acc',mode='auto' ,save_best_only='True')
	next_batch=data_generator(BATCH_SIZE,input_shape,"./file/x_train")
	next_valid_batch=data_generator(BATCH_SIZE,input_shape,"./file/x_valid")
	model.fit_generator(batch_generator(next_batch,data_size),steps_per_epoch=data_size,
		epochs=NB_EPOCH,callbacks=[call,checkpoint],validation_data=batch_generator(next_valid_batch,data_size),
		nb_val_samples=valid_size)
	print('3')
	model.save('mlp')
	print("model save complete!")

train_mlp()