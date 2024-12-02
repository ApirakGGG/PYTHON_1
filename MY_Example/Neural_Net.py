import tensorflow as tf #import tensorflow
import keras #call keras as API in tensorflow
from keras import layers , models

#โหลดข้อมูล MNIST (รูปภาพตัวเลขเขียนด้วยมือ)
mnist = tf.keras.datasets.mnist

#แยกข้อมูลการฝึกและทดสอบ
(x_train, y_train), (x_test , y_test) = mnist.load_data()
 
 #ปรับขนาดภาพให้เป็นขนาด 0 และ 1
x_train , x_test = x_train / 255.0 , x_test / 255.0

# สร้างmodels แบบ sequential (สร้างแบบจำลองที่มีlayers ต่อกัน)
model = models.Sequential()

#Add layers Convolutional 2D เพื่อดึงคุณสมบัติจากภาพ
model.add(layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)))

#Add layers Maxpooling เพื่อย่อขนาดลง
model.add(layers.MaxPooling2D((2,2)))

#Add layeres convolution 2D อีกชั้นหนึ่ง
model.add(layers.Conv2D(64, (3,3), activation="relu"))

#ADD MaxPooling again
model.add(layers.MaxPooling2D((2,2)))

#Add layers convolution 2D again 
model.add(layers.Conv2D(64, (3,3), activation="relu"))

#เปลี่ยนข้อมูลเป็นแบบเวกเตอร์ (Flatten())
model.add(layers.Flatten())

#เพิ่ม fully connected layers (Dense) เพื่อการประมวลผลเพิ่มเติม
model.add(layers.Dense(64 , activation="relu"))

#add layerse end ที่มีจำนวนหน่วยประมวลผมเท่ากัย 0-9
model.add(layers.Dense(10 , activation="softmax"))

#สรุปโครงสร้างmodel
model.summary()

#Compile model ดดยกำหนด loss function , optimizer และ metrics
model.compile(optimizer="adam",
               loss = "sparse_categorical_crossentropy",
               metrics = ["accuracy"])

#Train model by dataset
model.fit(x_train.reshape(-1, 28, 28, 1), y_train , epochs=5)

#ประเมินประสิทธิภาพของข้อมูลของโมเดลด้วยข้อมูลการทดสอบ
test_loss, test_acc = model.evaluate(x_test.reshape(-1 , 28 , 28, 1), y_test, verbose=2)

print(f"Accuracy on test data: {test_acc:.4f}")