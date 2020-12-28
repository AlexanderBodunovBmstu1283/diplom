import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM, SpatialDropout1D
from keras.datasets import imdb
import os
import random
from collections import deque
import matplotlib.pyplot as plt

# Загружаем данные
#(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)
#**********************************************************
import math

def activation(x,a):
    return int(x>a)


def error_value(F,A):
    sum=0
    for i in range(len(F)):
        sum+=abs(F[i]-A[i])
    print("Количество ошибок = ",sum)


def classic(x,a):
    result=[]
    for i in x:
        g_i=sum(i)/len(i)
        Fi=activation(g_i,a)
        result.append(Fi)
    return result


def harington(x,x1,x2,x3):
    def T(x,x1,x2,x3):
        if x>=0.8:
            return 1
        if x>=0.63:
            return x1
        if x>=0.37:
            return x2
        if x>=0.2:
            return x3
        return 0
    result = []
    for i in x:
        D_i=1
        for j in i:
            f_i_j=math.exp((-1)*math.exp(2-8*j))
            D_i*=f_i_j
        D_i=D_i**(1/len(i))
        F_i=T(D_i,x1,x2,x3)
        result.append(F_i)
    return result

def statistics_double(x,a,b):
    result = []
    for i in x:
        g_i = sum(activation(j,a) for j in i) / len(i)
        Fi = activation(g_i, b)
        result.append(Fi)
    return result


def calculate_params(x,A):
    '''
    for a in range(0,100):
        Fi=classic(x,a/100)
        error_value(Fi,A)
    '''

    '''

    for x1 in range(0,2):
        for x2 in range(0, 2):
            for x3 in range(0, 2):
                if x1>=x2>=x3:
                    Fi = harington(x,x1,x2,x3)
                    error_value(Fi, A)
    '''

    for a in range(0, 100):
        for b in range(0, 100):
            Fi = statistics_double(x,a/100,b/100)
            error_value(Fi, A)

#calculate_params()
#**********************************************************

def read_poem_lenght(arr,dir_name,index_of_set):
    global arr_recognized
    dir_name=dir_name+'/'+dir_name
    sum=0
    all_lengths=[]
    num_poems_indicated=0
    dir_read_length =dir_name+"/meta/"
    num_files_1 = (len(os.listdir(dir_read_length)))
    _curr_index=0
    all_1_s_texts=[]
    for i in range(0,num_files_1):
        with open (dir_name+"/meta/"+str(i)+".txt","r") as file:
            [result]=(deque(file, maxlen=1) or [''])
            #print(result)
            try:
                sum+=int(result)
                all_lengths.append(result)
            except:
                pass
        all_1_s = True
        with open(dir_name + "/prediction/" + str(i) + ".txt", "w+") as file:
            pass
        with open(dir_name+"/prediction/" + str(i) + ".txt", "a") as file:
                file.write("\nprediction\n")
                for j in range (_curr_index,_curr_index+int(result)):
                    try:
                        print(arr[j])
                        file.write(str(arr[j]))
                        all_1_s=all_1_s and arr[j]
                    except:
                        all_1_s=False
        _curr_index += int(result)+1

        with open(dir_name+"/prediction_final/" + str(i) + ".txt", "a") as file:
            #file.write(str(int(all_1_s)))
            if all_1_s:
                file.write(root_dirs[index_of_set])

        #print (all_1_s)
        if all_1_s:
            #arr_recognized[index_of_set].append(glush)
            num_poems_indicated+=1
            with open(dir_name+"/texts/" + str(i) + ".txt", "r") as file:
                for _string in file:
                    print(_string)
            print("\n\n")
        else:
            pass
            #arr_recognized[index_of_set].append(0)
    print (num_poems_indicated)
    return all_lengths


def recognize_single_poem(model,dir,num_set_weights):
    X_recognize = ""#load_single_poem(dir)
    X_recognize = sequence.pad_sequences(X_recognize, maxlen=maxlen)
    model.load_weights(root_dirs[num_set_weights] + "weights.h5")
    print("Веса:", model.weights[0])
    print("Количество объектов для предсказаний", len(X_recognize))
    arr = model.predict(X_recognize)

def recognize_poem_set(model,num_set,num_set_weights,index_of_set):
    set_for_recognize = load_data_mixer(root_dirs[num_set], section_dirs[num_set], "test")
    X_recognize = set_for_recognize[0]  # [[12,max_features-glush,14,111,14],[14,67,86,12],[134,64,86,32]]
    Y_recognize=set_for_recognize[1]

    with open("11111.txt","w") as file:
        file.write(str(X_recognize))

    X_recognize=sequence.pad_sequences(X_recognize, maxlen=maxlen)
    model.load_weights(root_dirs[num_set_weights] + "weights.h5")
    print("Веса:",model.weights[0])
    print("Количество объектов для предсказаний",len(X_recognize))
    arr = model.predict(X_recognize)
    arr1=arr

    #lengs_author_poems=[7,5,4,2,8,7,5,6,3,1,6,2,3,5,2,6,8,9,7,3]
    #lengs_author_poems=[18,10,8,13,11,16,9,6,12,12,6,2,3,4,2,5,8,9,7,3]
    lengs_author_poems=[4,5,6,6,4,4,8,5,3,2,4,4,6,16,3,3,9,6,4,10]
    neuro_prediction=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(lengs_author_poems)):
        neuro_prediction[i]=[i[0] for i in arr[0:lengs_author_poems[i]]]
        arr= arr[lengs_author_poems[i]:]






    with open ("nostalgic_pedictions.txt","w") as file:
        file.write("Оценка автора:\n")
        for i in Y_recognize:
            file.write(str(i))
        file.write("\nОценка нейросети:\n")
        for i in arr1:
            file.write(str(i))
        file.write("\nОценка нейросети:\n")
        #for i in neuro_prediction:
            #file.write(str(i)+"\n")
        file.write(str(neuro_prediction))
    '''
    _results=[]
    with open ("mikafox.txt","w") as file:
        for i in arr:
            if i[0]==1:
                prediction_result=1
            else:
                prediction_result=0
            file.write(str(prediction_result)+"\n")
            _results.append(prediction_result)
    read_poem_lenght(_results,root_dirs[num_set],index_of_set)
    '''

def load_data_mixer(root_dir,section_dir,type_set):
    def read_data(root_dir,name,type_set):
        result=[]
        if type_set=="train":
            dir_open="result"
        else:
            dir_open="test_result"
        with open (root_dir+"/"+dir_open+"/"+name) as file:
            for i in file:
                result.append(int(i.replace("\n","")))
        return result
    if type_set=="train":
        dir1=root_dir+"/result/"+section_dir[0]+"/"
        dir2=root_dir+"/result/"+section_dir[1]+"/"
    else:
        dir1 = root_dir+"/test_result/"+section_dir[0]+"/"
        dir2 = root_dir+"/test_result/"+section_dir[1]+"/"
    num_files_1=(len(os.listdir(dir1))-1)
    num_files_2=(len(os.listdir(dir2))-1)
    type1_index=0
    type2_index=0
    result_X=[]
    result_Y=[]
    if type_set == "train":
        while (type1_index<num_files_1 or type2_index<num_files_2):
            if random.randint(0,1)==1:
                if type1_index<num_files_1:
                    result_X.append(read_data(root_dir,section_dir[0]+"/"+str(type1_index)+".txt",type_set))
                    result_Y.append([1])
                    type1_index+=1
                else:
                    result_X.append(read_data(root_dir,section_dir[1]+"/"+str(type2_index)+".txt",type_set))
                    result_Y.append([0])
                    type2_index+=1
            else:
                if type2_index<num_files_2:
                    result_X.append(read_data(root_dir,section_dir[1]+"/"+str(type2_index)+".txt",type_set))
                    result_Y.append([0])
                    type2_index += 1
                else:
                    result_X.append(read_data(root_dir,section_dir[0]+"/" + str(type1_index) + ".txt",type_set))
                    result_Y.append([1])
                    type1_index += 1
        #print(len(result_X))
        #print(np.array(result_Y))
    else:
        while type1_index<num_files_1:
            result_X.append(read_data(root_dir, section_dir[0] + "/" + str(type1_index) + ".txt", type_set))
            result_Y.append([1])
            type1_index += 1
        while type2_index<num_files_2:
            result_X.append(read_data(root_dir, section_dir[1] + "/" + str(type2_index) + ".txt", type_set))
            result_Y.append([0])
            type2_index += 1
    return [result_X,np.array(result_Y)]


def train_model(model,root_dir,section_dir):
    max=0
    for i in range(0,1):
        set_for_train=load_data_mixer(root_dir,section_dir,"train")
        set_for_test=load_data_mixer(root_dir,section_dir,"test")
        X_train=set_for_train[0]#[[12,max_features-glush,14,111,14],[14,67,86,12],[134,64,86,32]]
        y_train=set_for_train[1]#np.array([[0],[0],[0]])
        X_test=set_for_test[0] #[[12,max_features-glush,15,111,14],[14,67,86,12],[134,64,86,32]]
        y_test=set_for_test[1] #np.array([[0],[0],[0]])

        # Заполняем или обрезаем рецензии
        X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
        X_test = sequence.pad_sequences(X_test, maxlen=maxlen)

        # Обучаем модель
        history=model.fit(X_train, y_train, batch_size=64, epochs=5,
                  validation_data=(X_test, y_test), verbose=2)
        # Проверяем качество обучения на тестовых данных
        print("Обучение закончено")
        N = 20
        scores = model.evaluate(X_test, y_test,
                                batch_size=64)
        print (scores)
        if (scores[1]>max):
            model.save_weights(root_dirs[num_set]+"weights.h5")
            max=scores[1]
            print("Точность на тестовых данных: %.2f%%" % (scores[1] * 100))
        print("Финальная точтость:"+str(max*100))
# Создаем сеть
print("Компиляция закончена")
#num_set=6
num_sets=[13,5,15,8,10,6,11,8,1]
index_=0
'''
for num_set in num_sets:
    #train_model(model,num_set)
    index_+=1
    recognize_poem_set(model,17,num_set,index_)
'''

#recognize_poem_set(model,13,13,13)
#print(section_dirs[num_set])
#model.save_weights(root_dirs[num_set]+"weights.h5")

train_model(model,root_dir,section_dir)