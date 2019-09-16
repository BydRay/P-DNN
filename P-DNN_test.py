import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



testdata_original = pd.read_csv('testing_dataset.csv', header=None)
testdata = testdata_original


test_tmp = testdata.iloc[:,0:41]
test_tmp = pd.concat([test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp,
                      test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp, test_tmp], axis=1, ignore_index=True)
x_test = np.array(test_tmp).astype(np.float32)
y_test = np.array(testdata.iloc[:,41])

x_test = tf.keras.utils.normalize(x_test, axis=1)
y_test_label = y_test
y_test = tf.keras.utils.to_categorical(y_test, 5)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(512, activation=tf.nn.relu, input_dim=820),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(32, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(5, activation=tf.nn.softmax)    # 这里使用 softmax 函数作为激活函数，因为我们想要找到预测结果的概率分布。（使用 reLU 得到的数字并没有这个意义）

])
model.compile(optimizer=tf.train.AdamOptimizer(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

file_path = 'best_modle.h5'
model.load_weights(file_path)

predict_y = model.predict(x_test)
y_predict_label = []
row_max = np.max(predict_y, axis=1).tolist()  # 每行最大
for i in range(len(row_max)):
    y_predict_label.append(np.where(predict_y[i] == row_max[i])[0][0])
predict_y_label = np.array(y_predict_label)

value_cnt = {}
for value in predict_y_label:
    value_cnt[value] = value_cnt.get(value, 0) + 1
print('predict_y_label', value_cnt)
value_cnt = {}
for value in y_test_label:
    value_cnt[value] = value_cnt.get(value, 0) + 1
print('y_test_label', value_cnt)
print('classification report')
print(classification_report(y_true=y_test_label, y_pred=predict_y_label, digits=3))
print('confusion matrix')
c_matrix = confusion_matrix(y_true=y_test_label, y_pred=predict_y_label)
print(c_matrix)
print('COST')
cost = [[0, 1, 2, 2, 2],
        [1, 0, 2, 2, 2],
        [2, 1, 0, 2, 2],
        [3, 2, 2, 0, 2],
        [4, 2, 2, 2, 0]]
print(np.sum(c_matrix * np.array(cost)) / 311029)