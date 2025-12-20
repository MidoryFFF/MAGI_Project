from binint import BinInt
import staticFuncs
import random
from zipper import *

class NeuronVector:
    def __init__(self, x: int):
        self.neuronCount = x
        self.vec: list[BinInt] = [BinInt() for _ in range(x)]
    
    def NextSumLayer(self, arg: BinInt) -> list[int]:
        newVec: int = [int()] * len(self.vec)
        for i in range(len(self.vec)):
            newVec[i] = staticFuncs.ActivationFunc(sum([self.vec[i] + j for j in arg]))
        return newVec

    def SetRandomWeights(self):
        for i in self.vec:
            rand = random.randint(0, 3)
            if (rand == 0):
                i.set(0, 0)
            elif (rand == 1):
                i.set(0, 1)
            elif (rand == 2):
                i.set(1, 1)

    def SetWeights(self, weights: list[BinInt]):
        for i in range(len(self.vec)):
            try:
                self.vec[i] = weights[i]
            except IndexError:
                print("Error: Compain, extending exist lyer")
                self.vec.append(weights[i])

    def WrightWeightsInFile(self, _fileName: str):
        for i in range(len(self.vec)):
            packAiWeaghtsByLayer(_fileName, self.vec[i])

    def PrintWeights(self):
        print(*[i.get() for i in self.vec])
    
    def SetTrue(self):
        for i in self.vec:
            i.set(1, 1)

    def GetWeights(self):
        return [i.getInt() for i in self.vec]


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
        return self.ForwardPropagation(inputArgs)

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

    def ReadWeaghtsFromFile(self, _fileName: str):
        weights = unpackAiWeaghts(_fileName)
        for i in range(len(self.layers)):
            try:
                self.layers[i].SetWeights(weights[i])
            except IndexError:
                print("Error: Compain, extending exist lyer")
                self.layers.append(weights[i])
    
    def WriteWeightsInFile(self, fileName: str):
        for i in range(len(self.layers)):
            self.layers[i].WrightWeightsInFile(fileName)

    def EasyWeiteInFile(self, fileName: str):
        easyIntPacker(fileName, [i.GetWeights() for i in self.layers])