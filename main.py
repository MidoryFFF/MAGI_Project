from ai import *

network = NeuralNetwork([2, 3, 2])
network.SetRandomWeigths()
network.EasyWeiteInFile("AIs/Melchior.AI")
print(network.RunNetwork([1, 0]))
network.PrintNetwork()