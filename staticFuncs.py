def CalculateGradient(LossFunc, ActivationFunc):
    m = 1/len()
    

#TODO need to think about activation function
def ActivationFunc(InputValue):
    if abs(InputValue) <= 5:
        return InputValue
    else:
        return 5 * (InputValue / abs(InputValue))

    # if InputValue > 0:
    #     return 1
    # elif InputValue < 0:
    #     return -1
    # return 0
