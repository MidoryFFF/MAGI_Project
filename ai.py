from binint import BinInt

class NeuronVector:
    def __init__(self, x: int):
        self.neuronCount = x
        self.vec: BinInt = [BinInt for _ in range(x)]
    
    def NextSumLayer(self, arg: BinInt):
        newVec = [] * len(self.vec)
        for i in range(len(self.vec)):
            newVec[i] = sum([j + self.vec[i] for j in arg])
        
        return newVec

    def PrintWeights(self):
        print(*[i.get(i) for i in self.vec])
    
    def SetTrue(self):
        for i in self.vec:
            i.set(i, 1, 1)


class NeuralNetwork:
    def __init__(self, leyersLength: int):
        self.layers: NeuronVector = [NeuronVector for i in range(len(leyersLength))]
        for i in range(len(leyersLength)):
            self.layers[i] = NeuronVector(leyersLength[i])
        
    def SumWithInput(self, xInput: int):
        for i in range(len(self.layers)):
            xInput = self.layers[i].NextSumLayer(xInput)
        
        return xInput
    
    def PrintNetwork(self):
        for i in self.layers:
            i.PrintWeights()
    
    def SetTrue(self):
        for i in self.layers:
            i.SetTrue()

network = NeuralNetwork([2, 3, 2])
network.PrintNetwork()
network.SetTrue()
network.PrintNetwork()
