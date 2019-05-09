#使用卷积网络进行监督训练
from keras.models import Sequential
from keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,Dropout
from myGO.utility.genDataFromHDF5 import HDF5OBJ
import keras
size=19

class modelConvEasy:
    def __init__(self):
        self.model=Sequential()
        self.model=constructModel()
    def constructModel(self):
        self.model.add(Conv2D(512,(2,2),input_shape=(19,19,3),activation='tanh',dilation_rate=(2, 2)))
        self.model.add(Dropout(rate=0.25))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Conv2D(512,(2,2),activation='tanh'))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(256,(2,2),activation='tanh'))
        self.model.add(Conv2D(256,(2,2),activation='tanh'))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(1024,activation='tanh'))
        self.model.add(Dropout(0.25))
        self.model.add(Dense(1024,activation='relu'))
        self.model.add(Dropout(0.25))
        self.model.add(Dense(512,activation='relu'))        
        self.model.add(Dense(size*size,activation='softmax'))

    def compile(self):
        opt = keras.optimizers.rmsprop(lr=0.0001,decay=1e-6)
        self.model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

    def run(self):

    def predict(self):

    def evaluate(self):


