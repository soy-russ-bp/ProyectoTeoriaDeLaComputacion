
archivo = open("testfile.txt", "r")

reservadas = ["PROGRAMA", "FINPROG", "SI", "ENTONCES", "SINO", "FINSI", "REPITE", "VECES", "FINREP", "IMPRIME", "LEE"]
operadoresA = ["+", "-", "*", "/"]
operadoresR = [">", "<", "=="]
asignacion = ["="]

tokensSeñalados = []

def SepararTokens():
    contenidos = archivo.readlines()
    global tokens 
    tokens = []
    for s in contenidos:
        if s[0] != "#":
            if '"' in s:
                lineaDiv = s.split('"')
                tokens.append(lineaDiv[0].strip(" "))
                tokens.append('"' + lineaDiv[1] + '"')                 
            else:
                tokens += s.split()
                
    
def IdentificarTipo():
    for t in tokens:
        if t in reservadas:
            tokensSeñalados.append(t + "<PR>")
        elif t in operadoresA:
            tokensSeñalados.append(t + "<OA>")
        elif t in operadoresR:
            tokensSeñalados.append(t + "<OR>")
        elif t in asignacion:
            tokensSeñalados.append(t + "<AS>")
        elif EsIdentificador(t):
            tokensSeñalados.append(t + "<ID>")
        elif EsNum(t):
            tokensSeñalados.append(t + "<NU>")
        elif EsTxt(t):
            tokensSeñalados.append(t + "<TX>")
        else:
            tokensSeñalados.append(t + "<NA>") 
            
def EsIdentificador(s):
    if s[0].isalpha() and len(s) <= 16:
        return True
    else:
        return False
    
def EsNum(s):
    if s[0] + s[1] == "0x":
        for c in s:
            if EsCharHex(c) == False:
                return False
        return True
    else:
        return False


def EsCharHex(c):
    if c == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        return True
    elif c == "A" or "B" or "C" or "D" or "E" or "F":
        return True
    else:
        return False

def EsTxt(s):
    if '"' in s:
        return True
    else:
        return False
    
def ImprimirTest():
    for t in tokensSeñalados:
        print(t)

SepararTokens()
IdentificarTipo()
ImprimirTest()




