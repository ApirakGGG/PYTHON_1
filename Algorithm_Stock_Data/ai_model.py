import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

def train_model(data):
    x = data[['EMA_10', 'EMA_20', 'EMA_50', 'MACD', 'RSI']].values
    y = data['BUY_SIGNAL'].astype(int).values

    #แบ่งข้อมูลสำหรับ train & test 
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, shuffle = False)

    #create model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(x.shape[1],)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])


    model.compile(optimizer = 'adam', loss ='binary_crossentropy', metrics = ['accuracy'])
    model.fit(x_train, y_train, epochs=50, batch_size=32, validation_data=(x_test, y_test))

    #reutrn ข้อมูล model
    return model