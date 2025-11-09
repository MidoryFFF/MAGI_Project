from binint import BinInt
import pickle

def packAiWeaghts(fileName: str, weagths: list[BinInt]):
    with open(fileName, "wb") as file:
        
        if (file.writable()):
            for i in range(len(weagths)):
                file.writelines(weagths)
        else:
            print("Error: File can't be open")
    
    print("Weaghts was saved")

def packAiWeaghtsByLayer(fileName: str, weagths: list[BinInt]):
    with open(fileName, "wb") as file:
        if (file.writable()):
            pickle.dump(weagths, file)
        else:
            print("Error: File can't be open")
    
    print("Weaghts was saved")


def unpackAiWeaghts(fileName: str):
    weagths: list[BinInt] = []
    with open(fileName, "rb") as file:
        if (file.writable()):
            while file.readline != None:
                weagths.append(file.readline())
        else:
            print("Error: File can't be open")
            return
    
    print("Weaghts was extracted")

    return weagths

def unpackAiWeaghtsByLayer(fileName: str, layerNumber: int):
    weagths: list[BinInt]
    with open(fileName, "rb") as file:
        if (file.writable()):
            weagths = file.readline(layerNumber)
        else:
            print("Error: File can't be open")
            return
    
    print("Weaghts was extracted")

    return weagths