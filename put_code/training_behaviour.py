import random
import json
import pickle
import numpy as np

import nltk
nltk.download('punkt')

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
#lemmatizer = WordNetLemmatizer()
#D:\machine_learning\chat_bot\
'''


with open('D:\machine_learning\chat_bot\data.json', 'r') as file:
    intents = json.load(file)
'''
#intents = json.loads(open('D:\machine_learning\chat_bot\data.json').read())

with open(r'D:\machine_learning\detect_behavious\data_trainig_behaviour.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)
words =[]
classes = []
documents = []
ignore_letters =['?','!',',','.','/']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern) 
        #Sử dụng thư viện NLTK (Natural Language Toolkit) để tách câu/lời nói thành danh sách các từ riêng lẻ.
        words.extend(word_list)
        
        documents.append((word_list, intent['tag']))
        #Thêm một cặp gồm danh sách các từ và nhãn "intent" vào một danh sách lớn hơn gọi là documents. Danh sách này sẽ được sử dụng để huấn luyện mô hình phân loại
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


#print(documents)

#words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]

words = sorted(set(words))
classes = sorted(set(classes))
#set(words) loại bỏ các từ trùng lặp, tạo ra một tập hợp duy nhất các từ.
#sorted(set(words)) sắp xếp các từ theo thứ tự bảng chữ cái.


pickle.dump(words,open('words.pkl','wb'))
#lưu danh sách words vào tệp tin words.pkl. 'wb' nghĩa là "write binary", để ghi dữ liệu vào tệp tin ở dạng nhị phân.
pickle.dump(classes,open('classes.pkl', 'wb'))

training =[]
output_emtpy = [0] *len(classes)

print("-----------------------")
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_emtpy)
    output_row[classes.index(document[1])] =1
    training.append([bag, output_row])

random.shuffle(training)
print(training)

print("-----------------------")

'''
training = [[[0, 1, 1], [0, 1]],
            [[1, 1, 1], [0, 0]],
            [[1, 2, 3], [4, 5]]]

array1 = np.array([item[0] for item in training])
array2 = [item[1] for item in training]


print(array1)
print(array2)
'''
train_x = np.array( [item[0] for item in training])
train_y = np.array( [item[1] for item in training])


'''
#training = np.array(training)
#training = np.array(training)
#training = np.array(training[0])

#train_x = list(training[:,0])
#train_y =  list(training[:,1])
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),),  activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation='softmax'))


#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#model.compile(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose =1)
model.compile(loss='categorical_crossentropy', optimizer= sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y),epochs=200,batch_size=5,verbose =1)
#evaluation_results = model.evaluate(test_data['input'], test_data['output'])
model.save('chatbot_model1.h5',hist)
print('done')
'''