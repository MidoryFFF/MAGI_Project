from binint import BinInt
import random

class NeuronVector:
    def __init__(self, x: int):
        self.neuronCount = x
        self.vec: list[BinInt] = [BinInt() for _ in range(x)]
    
    def NextSumLayer(self, arg: BinInt) -> list[int]:
        newVec: int = [int()] * len(self.vec)
        for i in range(len(self.vec)):
            newVec[i] = sum([self.vec[i] + j for j in arg])
        return newVec
    
    def SetRandomWeights(self):
        for i in self.vec:
            i.set(random.randint(0, 1), random.randint(0, 1))

    def PrintWeights(self):
        print(*[i.get() for i in self.vec])
    
    def SetTrue(self):
        for i in self.vec:
            i.set(i, 1, 1)


class NeuralNetwork:
    def __init__(self, leyersLength: int):
        self.layers: list[NeuronVector] = [NeuronVector(leyersLength[i]) for i in range(len(leyersLength))]
        
    def SumWithInput(self, xInput: int) -> list[int]:
        for i in range(len(self.layers)):
            xInput = self.layers[i].NextSumLayer(xInput)
        return xInput
    
    def SetRandomWeigths(self):
        for i in self.layers:
            i.SetRandomWeights()

    def RunNetwork(self, inputArgs: int):
        return max(self.ForwardPropagation(inputArgs))


    def ForwardPropagation(self, inputArgs: int):
        bufArgs = inputArgs
        for i in self.layers:
            bufArgs = i.NextSumLayer(bufArgs)
        return bufArgs
    
    def PrintNetwork(self):
        for i in self.layers:
            i.PrintWeights()
    
    def SetTrue(self):
        for i in self.layers:
            i.SetTrue()


network = NeuralNetwork([2, 3, 2])
network.SetRandomWeigths()
print(network.RunNetwork([1, 0, 1, -1]))
