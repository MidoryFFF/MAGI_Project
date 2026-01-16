from Ai.binint import BinInt

def packBinIntToInt(weagths: list[int]):
    result = ""
    for i in weagths:
        result += str(bin(i)[2:]).zfill(2)
    return result

def interfaceOfPacker(weagths: list[list[int]]):
    result = "10"
    for i in weagths:
        result += packBinIntToInt(i) + "10"
        print(result)
    return result

def easyIntPacker(fileName: str, weagths: list[list[int]]):
    lenght = 2
    for i in weagths:
        lenght += len(i) + 2
    with open(fileName, "+wb") as f:
        f.write(int(interfaceOfPacker(weagths), 2).to_bytes(int(lenght/4), 'big', signed=False))

def packAiWeaghts(fileName: str, weagths: list[BinInt]):
    if (fileName[-3:] != ".AI"):
        fileName = fileName + ".AI"
    with open(fileName, "w") as file:
        if (file.writable()):
            file.writelines(str("".join(FillUpInChar([i.getTrueValues for i in weagths]))))
        else:
            print("Error: File can't be open")
        print("Weaghts was saved")

def packAiWeaghtsInBinary(fileName: str, weagths: list[BinInt]):
    with open(fileName, "+wb") as file:
        if (file.writable()):
            for i in range(len(weagths)):
                file.write(bytes(str(weagths[i].getTrueValues()), "utf-8"))
                print((weagths[i].getTrueValues()), bytes(str(weagths[i].getTrueValues()), "utf-8"))
        else:
            print("Error: File can't be open")

    print("Weaghts was saved")

def unpackAiWeaghts(fileName: str) -> list[BinInt]:
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

def unpackAiWeaghtsInBinary(fileName: str, layerNumber: int) -> list[BinInt]:
    weagths: list[BinInt]
    with open(fileName, "rb") as file:
        if (file.writable()):
            weagths = file.readline(layerNumber)
        else:
            print("Error: File can't be open")
            return

    print("Weaghts was extracted")

    return weagths

def FillUpInChar(vec: list[chr]) -> list[chr]:
    syzeOfChar = 4

    solution = []
    solution.append(0)
    while len(vec) > syzeOfChar/2:
        for _ in range(int(syzeOfChar/2)):
            solution[-1] = (solution[-1] + vec[0]) << 2
            vec.pop()
            solution.append(0)

    flag = False
    for _ in range(int(syzeOfChar/2)):
        if (not flag and vec):
            solution[-1] = (solution[-1] | vec[0]) << 2
            vec.pop()
        elif (not flag):
            solution[-1] = (solution[-1] | 0b10) << 2
            flag = True
        else:
            solution[-1] = (solution[-1] | 0b00) << 2

    anser = []
    for i in solution:
        print(bin(i))
        anser.append(bin(i))

    return anser
