limits = 5

def ActivationFunc(num):
    if (abs(num) > limits):
        return int(5 * num/abs(num))
    else:
        return num