import math
def sigmoid(x):
    y =  1.0 / (1 + math.exp(-x))
    return y
def activation(inputs, weights):
    h = 0
    for x, w in zip(inputs, weights):
        h += x*w
    return sigmoid(h) 
if __name__ == "__main__":
    inputs = [.5, .3, .2]
    weights = [.4, .7, .2]
    output = activation(inputs, weights)
    print("output : ", output)
