import numpy as np
import random

# Load the data from the file and return a list of lists, with each line as a list
def load_data(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    dataList = []
    
    for line in lines:
        lineList = line.split()
        string_token = lineList[0]
        dataList.append((string_token, int(lineList[1])))
    return dataList

def string_kernel(p, s, t):
    count = 0
    seen = []
    for i in range(0, len(s) - p + 1):
        v = s[i:(i+p)]
        # if v in t and v not in seen:
        if v in t:# and v not in seen:
            # Count the number of times v occurs in t and add it to count
            count += t.count(v)
            # seen.append(v)
    return count

def kernel_dot(p, w_list, vector):
    running_sum = 0
    for (protein, label) in w_list:
        running_sum += label * string_kernel(p, protein, vector)
    return running_sum

def perceptron(data_list, p):
    w_list = []
    for (protein, label) in data_list:
        if (label * kernel_dot(p, w_list, protein)) <= 0:
            w_list.append((protein, label))
    return w_list

def calc_error(data_list, w_list, p):
    error_count = 0
    for (protein, label) in data_list:
        if kernel_dot(p, w_list, protein) * label <= 0:
            error_count += 1
    return (error_count / len(data_list))

training_data = load_data("pa4train.txt")
test_data = load_data("pa4test.txt")

for p in range(2,6):
    w = perceptron(training_data, p)
    training_error = calc_error(training_data, w, p)
    test_error = calc_error(test_data, w, p)
    print("Training Error for P =", p, "is ", training_error)
    print("Test Error for P =", p, "is ", test_error)