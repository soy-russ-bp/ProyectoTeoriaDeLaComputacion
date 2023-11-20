
archivo = open("testfile.txt", "r")

reservadas = ["PROGRAMA", "FINPROG", "SI", "ENTONCES", "SINO", "FINSI", "REPITE", "VECES", "FINREP", "IMPRIME", "LEE"]
operadoresA = ["+", "-", "*", "/"]
operadoresR = [">", "<", "=="]
asignacion = ["="]

tokensSeñalados = []
tabla_datos = [[], [], []]

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
            if( t not in tabla_datos[0]):
                tabla_datos[0].append(t)
        elif EsNum(t):
            tokensSeñalados.append(t + "<NU>")
            if( t not in tabla_datos[1]):
                tabla_datos[1].append(t)
        elif EsTxt(t):
            tokensSeñalados.append(t + "<TX>")
            if( t not in tabla_datos[2]):
                tabla_datos[2].append(t)
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
    
        
tabla_simbolos = [ [], [], [] ]
 
def Tabla():
    i=1
    k=1
    for fila in tabla_datos:
        for posicion in fila:
            if EsIdentificador(posicion):
                tabla_simbolos[0].append(posicion + ', ' + "ID" + str(i))
                i += 1
            elif EsTxt(posicion):
                tabla_simbolos[1].append(posicion + ', ' + "TX" + str(k))
                k += 1
            elif EsNum(posicion):
                tabla_simbolos[2].append(posicion + ', ' + str(HexaADecimal(str(posicion))) )
            
        
def TablaTXT(factorialsim):
    with open(factorialsim, 'w') as archivo:
        # Identificadores
        archivo.write("IDS\n")
        archivo.write('\n'.join(tabla_simbolos[0]) + '\n\n')

        # Textos
        archivo.write("TXT\n")
        archivo.write('\n'.join(tabla_simbolos[1]) + '\n\n')

        # Números
        archivo.write("VAL\n")
        archivo.write('\n'.join(tabla_simbolos[2]) + '\n')

def ImprimirTest():
    for t in tokensSeñalados:
        print(t)

def HexaADecimal(hex_number):
    decimal_number = int(hex_number, 16)
    return decimal_number

#y generará los archivos “factorial.lex” con la siguiente secuencia de tokens:... (@Arturo, creo que falta eso, es decir,
# imprime en la consola, pero no genera el archivo factorial.txt)

SepararTokens()
IdentificarTipo()
ImprimirTest()
Tabla()
TablaTXT("factorialsim.txt")
#ImprimirTabla() #no sé qué es, pero no estaba hecha esta función, así que comenté la línea

#y el archivo“factorial.sim”con los siguientes arreglos de símbolos:
#IDS:
#TXT:
#VALS: 
# (done)
