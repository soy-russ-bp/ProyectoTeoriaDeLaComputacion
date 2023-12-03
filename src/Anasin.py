'''
Reglas:
<PROG> → PROGRAMA [id] <SENTS> FINPROG
<SENTS> → <SENT> <SENTS>
<SENTS> → <SENT>
<SENT> → [id] = <ELEM> [op_ar] <ELEM>
<SENT> → [id] = <ELEM>
<SENT> → SI <COMPARA> ENTONCES <SENTS> SINO <SENTS> FINSI
<SENT> → SI <COMPARA> ENTONCES <SENTS> FINSI
<SENT> → REPITE <ELEM> VECES <SENTS> FINREP
<SENT> → IMPRIME <ELEM>
<SENT> → IMPRIME [txt]
<SENT> → LEE [id]
<SENT> → # [comentario]
<ELEM> → [id]
<ELEM> → [val]
<COMPARA> → [id] [op_rel] <ELEM>
'''

tokens = open("factorial.lex", "r").readlines()

pila = []
index = 0

def PerteneceAlLenguaje():
    pila.append("FINPROG")
    if Token() != "PROGRAMA\n":
        print(Token())
        Error("Error en Programa")
        return
    Next()
    if Token() != "[id]\n":
        Error("Error en Programa 2")
        return
    Next()
    nuevaSentencia()

def nuevaSentencia():
    if Token() == "SI\n":
        pila.append("FINSI")
        Si()
        return

    elif Token() == "[id]\n":
        Id()
        return

    elif Token() == "IMPRIME\n":
        Imprime()
        return

    elif Token() == "LEE\n":
        Lee()
        return

    elif Token() == "REPITE\n":
        pila.append("FINREP")
        Repite()
        return

    elif Token() == "SINO\n":
        if UltimoDePila() == "FINSI":
            Next()
            nuevaSentencia()
            return
        else:
            Error("Error en sino")
            return

    elif Token() == "FINSI\n":
        if UltimoDePila() == "FINSI":
            SacarDePila()
            Next()
            nuevaSentencia()
            return
        else:
            Error("Error en finsi")
            return

    elif Token() == "FINREP\n":
        if UltimoDePila() == "FINREP":
            SacarDePila()
            Next()
            nuevaSentencia()
            return
        else:
            Error("Error en finrep")
            return

    elif Token() == "FINPROG\n":
        if UltimoDePila() == "FINPROG":
            SacarDePila()
            print("Compilacion exitosa")
            return
        else:
            Error("Error en finprog")
            return
        
    Error("FALLO EN LA DETECCION")
    
    

def Id():
    Next()
    if Token() != "=\n":
        Error("Error en id, deberia ser =")
        return
    Next()

    if Token() != "[id]\n":
        if Token() != "[val]\n":
            Error("Error en id, deberia ser id o val")
            return
    Next()

    if Token() != "[op_ar]\n":
        nuevaSentencia()
        return
    Next()

    if Token() != "[id]\n":
         if Token() != "[val]\n":
            Error("Error en id")
            return
    Next()
    nuevaSentencia()

def Si():
    Next()
    if Token() != "[id]\n":
        Error("Error en Si")
        return
    Next()
    if Token() != "[op_rel]\n":
        Error("Error en Si")
        return
    Next()

    if Token() != "[id]\n":
        if Token != "[val]\n":
            Error("Error en Si")
            return
    Next()
    if Token() != "ENTONCES\n":
        Error("Error en Si")
        return
    Next()
    nuevaSentencia()

def Repite():
    Next()
    if Token() != "[id]\n":
        if Token() != "[val]\n":
            Error("Error en Repite")
            return
    Next()
    if Token() != "VECES\n":
        Error("Error en Repite")
        return
    Next()
    nuevaSentencia()

def Imprime():
    Next()
    if Token() != "[id]\n":
        if Token() != "[val]\n":
            if Token() != "[txt]\n":
                Error("Error en Imprime")
                return
    Next()
    nuevaSentencia()

def Lee():
    Next()
    if Token() != "[id]\n":
        Error("Error en lee")
        return
    Next()
    nuevaSentencia()

def SacarDePila():
    pila.pop()

def UltimoDePila():
    return pila[len(pila)-1]

def Token():
    global index
    return tokens[index]

def SigToken():
    global index
    return tokens[index + 1]

def Next():
    global index
    index = index + 1

def Error(debugText):
    print(Token(), index)
    print("Error en compilacion")
    print(debugText)

PerteneceAlLenguaje()
