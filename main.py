from Ai.ai import *

network = NeuralNetwork([2, 3, 2])
network.SetRandomWeigths()
network.PrintNetwork()
network.VizualizeOutput()
network.EasyWeiteInFile("AIs/Melchior.AI")
