from binint import BinInt
import pickle

def packBinIntToInt(weagths: list[int]):
    result = ""
    for i in weagths:
        result += str(bin(i)[2:].zfill(2))
    return result

def interfaceOfPacker(weagths: list[list[int]]):
    result = "10"
    for i in weagths:
        result += packBinIntToInt(i) + "10"
    return result

def easyIntPacker(fileName: str, weagths: list[list[int]]):
    lenght = 2
    for i in weagths:
        lenght += len(i) + 2
    with open(fileName, "wb") as f:
        f.write(int(interfaceOfPacker(weagths), 2).to_bytes(int(lenght/4), 'big', signed=False))

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