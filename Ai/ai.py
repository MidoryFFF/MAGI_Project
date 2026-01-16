from Ai.binint import BinInt
import staticFuncs
import random
from Ai.zipper import *

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
        packAiWeaghts(_fileName, self.vec)

    def PrintWeights(self):
        print(*[i.get() for i in self.vec])

    def SetTrue(self):
        for i in self.vec:
            i.set(1, 1)

    def len(self):
        return len(self.vec)

    def GetWeights(self):
        return [i.getInt() for i in self.vec]

class NeuralNetwork:
    def __init__(self, leyersLength: int):
        self.layers: list[NeuronVector] = [NeuronVector(1)] + [NeuronVector(leyersLength[i]) for i in range(len(leyersLength))]

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

    def VizualizeOutput(self):
        vecInput = [-5]
        vecOutput = []
        b = True
        while b:
            vecOutput.append([[str(vecInput[0])], [str(i) for i in printAI(vecInput, self)]]) # + [[str(sum(vecInput))]]
            vecInput[0] += 1
            if (vecInput[0] > 5):
                b = False
            # for j in range(len(vecInput)):
            #     if vecInput[j] > 5:
            #         vecInput[j] = -5
            #         try:
            #             vecInput[j + 1] += 1
            #         except:
            #             pass
            # if (all([True if k > 5 else False for k in vecInput])):
            #     b = False

        with open("Output.txt", "+tw") as f:
            for i in range(len(vecOutput)):
                if (i != 0):
                    f.write("\n")
                for j in range(len(vecOutput[i])):
                    if (j < len(vecOutput[i]) - 1):
                        f.write(",".join(vecOutput[i][j]) + ",")
                    else:
                        f.write(",".join(vecOutput[i][j]))

    def EasyWeiteInFile(self, fileName: str):
        easyIntPacker(fileName, [i.GetWeights() for i in self.layers])

def printAI(vecInput : list[float], network : NeuralNetwork) -> list[int]:
    # vizualMatrix = []
    # for _ in range(11):
    #     vizualMatrix.append([" |" for _ in range(11)])
    temp = network.ForwardPropagation(vecInput)
    result = temp
    # temp = [i + 5 for i in temp]
    # print(vecInput, temp)
    # vizualMatrix[temp[0]][temp[1]] = "#|"
    # print("=|" * 11)
    # for i in vizualMatrix:
    #     print(''.join(i))
    # print("=|" * 11)
    return result
