from random import randint
import os

isTrue = True
jogou = 1
Olinha = -1
Ocoluna = -1
vencedor = -1 # 1 = X, 0 = O

def printMatriz(Matriz):
    for i in Matriz:
        print(i)

def vertical_1_baixo(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[2][0] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][2] == "X"):
        if(matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if (matriz[0][1] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][1] != "O"):
                Olinha = 0
                Ocoluna = 1
                matriz[0][1] = "O"
                portaO = 0
                return 0
    elif (matriz[0][1] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_0_baixo(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[1][0] == "X"):
        if (matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if(matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][1] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2 
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[0][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    elif (matriz[0][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][0] != "O"):
            Olinha = 1 
            Ocoluna = 0
            matriz[1][0] = "O"
            portaO = 0
            return 0
    elif (matriz[2][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[2][1] != "O"):
            Olinha = 2
            Ocoluna = 1
            matriz[2][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_2_baixo(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[2][1] == "X"):
        if (matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if(matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
    elif (matriz[1][2] == "X"):
        if (matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[0][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    elif (matriz[0][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][2] != "O"):
            Olinha = 1
            Ocoluna = 2
            matriz[1][2] = "O"
            portaO = 0
            return 0
    elif (matriz[2][0] == "X"):
        if(verificaO(matriz)):
            return 0  
        if(matriz[2][1] != "O"):  
            Olinha = 2
            Ocoluna = 1
            matriz[2][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Meio0(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][0] == "X"):
        if (matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if(matriz[1][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[1][2] != "O"):
                Olinha = 1 
                Ocoluna = 2 
                matriz[1][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][0] == "X"):
        if (matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2) 
        Oculuna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Meio2(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][2] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][2] == "X"):
        if(matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if (matriz[1][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[1][0] != "O"):
                Olinha = 1
                Ocoluna = 0
                matriz[1][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2) 
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Meio1(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][0] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][2] == "X"):
        if(matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
                return 0
    elif (matriz[2][0] == "X"):
        if (matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[0][2] == "X"):
        if (matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][0] == "X"):
        if (matriz[1][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[1][2] != "O"):
                Olinha = 1
                Ocoluna = 2
                matriz[1][2] = "O"
                portaO = 0
                return 0
    elif (matriz[1][2] == "X"):
        if (matriz[1][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[1][0] != "O"):
                Olinha = 1
                Ocoluna = 0
                matriz[1][0] = "O"
                portaO = 0
                return 0
    elif (matriz[0][1] == "X"):
        if (matriz[2][1] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][1] != "O"):
                Olinha = 2
                Ocoluna = 1
                matriz[2][1] = "O"
                portaO = 0
                return 0
    elif (matriz[2][1] == "X"):
        if (matriz[0][1] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][1] != "O"):
                Olinha = 0
                Ocoluna = 1
                matriz[0][1] = "O"
                portaO = 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Cima0(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][1] == "X"):
        if (matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[1][0] == "X"):
        if(matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[2][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][0] != "O"):
            Olinha = 1
            Ocoluna = 0
            matriz[1][0] = "O"
            portaO = 0
            return 0
    elif (matriz[2][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    elif (matriz[0][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[0][1] != "O"):
            Olinha = 0
            Ocoluna = 1
            matriz[0][1] = "O"
            portaO = 0
            return 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Cima1(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][0] == "X"):
        if (matriz[0][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][2] != "O"):
                Olinha = 0
                Ocoluna = 2
                matriz[0][2] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if(matriz[2][1] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][1] != "O"):
                Olinha = 2
                Ocoluna = 1
                matriz[2][1] = "O"
                portaO = 0
                return 0
    elif (matriz[0][2] == "X"):
        if (matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
                return 0
    elif (matriz[2][1] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    if (jogou): 
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1

def vertical_Cima2(matriz,n,m):
    global vencedor
    global isTrue
    global Olinha
    global Ocoluna
    if (matriz[0][1] == "X"):
        if (matriz[0][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[0][0] != "O"):
                Olinha = 0
                Ocoluna = 0
                matriz[0][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][1] == "X"):
        if(matriz[2][0] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][0] != "O"):
                Olinha = 2
                Ocoluna = 0
                matriz[2][0] = "O"
                portaO = 0
                return 0
    elif (matriz[1][2] == "X"):
        if (matriz[2][2] == "X"):
            vencedor = 1
            isTrue = False
            return 0
        else:
            if(verificaO(matriz)):
                return 0
            if(matriz[2][2] != "O"):
                Olinha = 2
                Ocoluna = 2
                matriz[2][2] = "O"
                portaO = 0
                return 0
    elif (matriz[0][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[0][1] != "O"):
            Olinha = 0
            Ocoluna = 1
            matriz[0][1] = "O"
            portaO = 0
            return 0
    elif (matriz[2][0] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 1
            matriz[1][1] = "O"
            portaO = 0
            return 0
    elif (matriz[2][2] == "X"):
        if(verificaO(matriz)):
            return 0
        if(matriz[1][1] != "O"):
            Olinha = 1
            Ocoluna = 2
            matriz[1][2] = "O"
            portaO = 0
    if (jogou):
        Olinha = randint(0,2)
        Ocoluna = randint(0,2)
        quadrado_aleatorio(matriz, Olinha, Ocoluna)
    else:
        if(verificaO(matriz)):
            return 0
        quadradoPerfeito(matriz)
        portaO = 1
        

def quadrado_aleatorio(Matriz, n, m):
    while (Matriz[n][m] == "X"):
        n = randint(0,2)
        m = randint(0,2)

    Matriz[n][m] = "O"
    global jogou 
    jogou = 0
    portaO = 0

#Jogador O

def Overtical_2_baixo(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[1][2] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                vencedor = 0
                isTrue = False
                return 1
                

        if (matriz[1][2] == "-"):
            if(matriz[0][2] == "O"):
                matriz[1][2] = "O"
                isTrue = False
                vencedor = 0
                return 1

        if (matriz[2][1] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][1] == "-"):
            if(matriz[2][0] == "O"):
                matriz[2][1] = "O"
                isTrue = False
                vencedor = 0
                return 1

        if (matriz[1][1] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1

        if (matriz[1][1] == "-"):
            if(matriz[0][0] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """
        else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0
        """

def Overtical_0_baixo(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[1][0] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][0] == "-"):
            if(matriz[0][0] == "O"):
                matriz[1][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[0][2] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][1] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][1] == "-"):
            if(matriz[2][2] == "O"):
                matriz[2][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_1_baixo(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[1][1] == "O"):
            if(matriz[2][1] != "X"):
                matriz[2][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[0][1] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][0] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][2] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_0_meio(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][0] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][0] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[1][2] != "X"):
                matriz[1][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[1][2] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_1_meio(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][1] == "O"):
            if(matriz[2][1] != "X"):
                matriz[2][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][1] == "O"):
            if(matriz[0][1] != "X"):
                matriz[0][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][0] == "O"):
            if(matriz[1][2] != "X"):
                matriz[1][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][2] == "O"):
            if(matriz[1][0] != "X"):
                matriz[1][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[0][0] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][2] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[0][2] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[2][0] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_2_meio(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][2] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[2][2] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[1][0] != "X"):
                matriz[1][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[1][0] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_0_cima(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][1] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[0][1] == "-"):
            if(matriz[0][2] == "O"):
                matriz[0][1] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[1][0] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[1][0] == "-"):
            if(matriz[2][0] == "O"):
                matriz[1][0] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                vencedor = 0
                isTrue = False
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[2][2] == "O"):
                matriz[1][1] = "O"
                vencedor = 0
                isTrue = False
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_1_cima(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][0] == "O"):
            if(matriz[0][2] != "X"):
                matriz[0][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[0][2] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[2][1] != "X"):
                matriz[2][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[2][1] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def Overtical_2_cima(matriz,n,m):
    global vencedor
    global isTrue
    if (matriz[n][m] == "O"):
        if (matriz[0][1] == "O"):
            if(matriz[0][0] != "X"):
                matriz[0][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[0][1] == "-"):
            if(matriz[0][0] == "O"):
                matriz[0][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "O"):
            if(matriz[2][0] != "X"):
                matriz[2][0] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][1] == "-"):
            if(matriz[2][0] == "O"):
                matriz[1][1] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][2] == "O"):
            if(matriz[2][2] != "X"):
                matriz[2][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        if (matriz[1][2] == "-"):
            if(matriz[2][2] == "O"):
                matriz[1][2] = "O"
                isTrue = False
                vencedor = 0
                return 1
        return 0
        """else:
            if (jogou):
                global Olinha 
                Olinha = randint(0,2)
                global Ocoluna 
                Ocoluna = randint(0,2)
                #quadrado_aleatorio(matriz, Olinha, Ocoluna)
                return 0
            else:
                print("quadrado perfeito")
                return 0"""

def verificaO(matriz):
    if(Olinha == 0 and Ocoluna == 0):
        if(Overtical_0_cima(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 0 and Ocoluna == 1):
        if(Overtical_1_cima(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 0 and Ocoluna == 2):
        if(Overtical_2_cima(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 1 and Ocoluna == 0):
        if(Overtical_0_meio(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 1 and Ocoluna == 1):
        if(Overtical_1_meio(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 1 and Ocoluna == 2):
        if(Overtical_2_meio(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 2 and Ocoluna == 0):
        if(Overtical_0_baixo(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 2 and Ocoluna == 1):
        if(Overtical_1_baixo(Matriz, Olinha, Ocoluna)):
            return 1
        return 0
    elif(Olinha == 2 and Ocoluna == 2):
        if(Overtical_2_baixo(Matriz, Olinha, Ocoluna)):
            return 1
        return 0

def way_0_cima(matriz):
    global Ocoluna
    global Olinha
    if(matriz[0][1] == "-"):
        if (matriz[0][2] == "-"):
            matriz[0][2] = "O"
            Olinha = 0
            Ocoluna = 2
            return 0
    if(matriz[1][0] == "-"):
        if (matriz[2][0] == "-"):
            matriz[2][0] = "O"
            Olinha = 2
            Ocoluna = 0
            return 0
    if(matriz[1][1] == "-"):
        if(matriz[2][2] == "-"):
            matriz[2][2] = "O"
            Olinha = 2
            Ocoluna = 2
            return 0
    if(matriz[0][1] == "-"):
        matriz [0][1] = "O"
        Olinha = 0
        Ocoluna = 1
        return 0
    if(matriz[1][0] == "-"):
        matriz[1][0] = "O"
        Olinha = 1
        Ocoluna = 0
        return 0
    if(matriz[1][1] == "-"):
        Ocoluna = 1
        Olinha = 1
        return 0
    if(matriz[1][2] == "-"):
        Olinha = 1
        Ocoluna = 2
        return 0
    if(matriz[2][2] == "-"):
        Olinha = 1
        Ocoluna = 2
        return 0
    if(matriz[2][0] == "-"):
        Olinha = 2
        Ocoluna = 0
        return 0
    
def way_1_cima(matriz):
    global Ocoluna
    global Olinha
    if(matriz[1][1] == "-"):
        if(matriz[2][1] == "-"):
            matriz[2][1] = "O"
            Olinha = 2
            Ocoluna = 1
            return 0
    if(matriz[0][0] == "-"):
        if (matriz[0][2] == "-"):
            matriz[0][2] = "O"
            Olinha = 0
            Ocoluna = 2
            return 0
    if(matriz[0][2] == "-"):
        matriz[0][2] = "O"
        Olinha = 0
        Ocoluna = 2
        return 0
    if(matriz[1][1] == "-"):
        matriz [1][1] = "O"
        Olinha = 1
        Ocoluna = 1
        return 0
    if(matriz[0][1] == "-"):
        matriz[0][1] = "O"
        Olinha = 1
        Ocoluna = 0
        return 0
    if(matriz[2][1] == "-"):
        Olinha = 1
        Ocoluna = 2
        return 0

def way_2_cima(matriz):
    global Ocoluna
    global Olinha
    if(matriz[1][1] == "-"):
        if(matriz[2][0] == "-"):
            matriz[2][0] = "O"
            Olinha = 2
            Ocoluna = 0
            return 0
    if(matriz[0][1] == "-"):
        if (matriz[0][2] == "-"):
            matriz[0][2] = "O"
            Olinha = 0
            Ocoluna = 2
            return 0
    if(matriz[1][2] == "-"):
        if(matriz[2][2] == "-"):
            matriz[2][2] = "O"
            Olinha = 2
            Ocoluna = 2
            return 0
    if(matriz[0][1] == "-"):
        matriz [1][1] = "O"
        Olinha = 0
        Ocoluna = 1
        return 0
    if(matriz[1][1] == "-"):
        matriz[1][1] = "O"
        Olinha = 1
        Ocoluna = 1
        return 0
    if(matriz[1][2] == "-"):
        Olinha = 1
        Ocoluna = 2
        return 0
    if(matriz[0][0] == "-"):
        Olinha = 0
        Ocoluna = 0
        return 0
    if(matriz[2][0] == "-"):
        Olinha = 2
        Ocoluna = 0
        return 0
    if(matriz[2][2] == "-"):
        Olinha = 2
        Ocoluna = 2
        return 0

def way_0_meio(matriz):
    global Ocoluna
    global Olinha
    if(matriz[1][1] == "-"):
        if(matriz[1][2] == "-"):
            Olinha = 1
            Ocoluna = 2
            matriz[1][2] = "O"
            return 0
    if(matriz[0][0] == "-"):
        if(matriz[2][0] == "-"):
            Olinha = 2
            Ocoluna = 0
            matriz[2][0] = "O"
            return 0
    if(matriz[1][1] == "-"):
        Olinha = "1"
        Ocoluna = "1"
        matriz[1][1] = "O"
        return 0
    if(matriz[0][0] == "-"):
        Olinha = 0
        Ocoluna = 0
        matriz[0][0]
        return 0
    if(matriz[2][0] == "-"):
        Olinha = 2
        Ocoluna = 0
        return 0
    if(matriz[1][2] == "-"):
        Olinha = 1
        Ocoluna = 2
        return 0

def way_1_meio(matriz):
    global Olinha
    global Ocoluna
    if(matriz[0][0] == "-"):
        if(matriz[2][2] == "-"):
            matriz[2][2] = "O"
            Olinha = 2
            Ocoluna = 2
            return 0
    if(matriz[0][1] == "-"):
        if(matriz[2][1] == "-"):
            matriz[2][1] = "O"
            Olinha = 2
            Ocoluna = 1
            return 0
    if(matriz[0][2] == "-"):
        if(matriz[2][0] == "-"):
            matriz[2][0] = "O"
            Olinha = 2
            Ocoluna = 0
            return 0
    if(matriz[1][0] == "-"):
        if(matriz[1][2] == "-"):
            matriz[1][2] = "O"
            Olinha = 1
            Ocoluna = 2
            return 0
    if(matriz[0][0] == "-"):
        matriz[0][0] = "O"
        Olinha = 0
        Ocoluna = 0
        return 0
    if(matriz[0][1] == "-"):
        matriz[0][1] = "O"
        Olinha = 0
        Ocoluna = 1
        return 0
    if(matriz[0][2] == "-"):
        matriz[0][2] = "O"
        Olinha = 0
        Ocoluna = 2
        return 0
    if(matriz[1][0] == "-"):
        matriz[1][0] = "O"
        Olinha = 1
        Ocoluna = 0
        return 0
    if(matriz[1][2] == "-"):
        matriz[1][2] = "O"
        Olinha = 1
        Ocoluna = 2
        return 0
    if(matriz[2][0] == "-"):
        matriz[2][0] = "O"
        Olinha = 2
        Ocoluna = 0
        return 0
    if(matriz[2][1] == "-"):
        matriz[2][1] = "O"
        Olinha = 2
        Ocoluna = 1
        return 0
    if(matriz[2][2] == "-"):
        matriz[2][2] = "O"
        Olinha = 2
        Ocoluna = 2
        return 0

def way_2_meio(matriz):
    global Olinha
    global Ocoluna
    if(matriz[0][2] == "-"):
        if(matriz[2][2] == "-"):
            matriz[2][2] = "O"
            Olinha = 2
            Ocoluna = 2
            return 0
    if(matriz[1][1] == "-"):
        if(matriz[1][0] == "-"):
            matriz[1][0] = "O"
            Olinha = 1
            Ocoluna = 0
            return 0
    if(matriz[1][1] == "-"):
        matriz[1][1] = "O"
        Olinha = 1
        Ocoluna = 1
        return 0
    if(matriz[0][2] == "-"):
        matriz[0][2] = "O"
        Olinha = 0
        Ocoluna = 2
        return 0
    if(matriz[2][2] == "-"):
        matriz[2][2] = "O"
        Olinha = 2
        Ocoluna = 2 
        return 0
    if(matriz[1][0] == "-"):
        matriz[1][0] = "O"
        Olinha = 1
        Ocoluna = 0
        return 0

def way_0_baixo(matriz):
    global Olinha
    global Ocoluna
    if(matriz[1][0] == "-"):
        if(matriz[0][0] == "-"):
            Olinha = 0
            Ocoluna = 0
            matriz[0][0] = "O"
            return 0
    if(matriz[1][1] == "-"):
        if(matriz[0][2] == "-"):
            Olinha = 0
            Ocoluna = 2
            matriz[0][2] = "O"
            return 0
    if(matriz[2][1] == "-"):
        if(matriz[2][2] == "-"):
            Olinha = 2
            Ocoluna = 2
            matriz[2][2] = "O"
            return 0
    if(matriz[1][0] == "-"):
        Olinha = 1
        Ocoluna = 0
        matriz[1][0] = "O"
        return 0
    if(matriz[0][0] == "-"):
        Olinha = 0
        Ocoluna = 0
        matriz[0][0] = "O"
        return 0
    if(matriz[1][1] == "-"):
        Olinha = 1
        Ocoluna = 1
        matriz[1][1] = "O"
        return 0
    if(matriz[0][2] == "-"):
        Olinha = 0
        Ocoluna = 2
        matriz[0][2] = "O"
        return 0
    if(matriz[2][1] == "-"):
        Olinha = 2
        Ocoluna = 1
        matriz[2][1] = "O"
        return 0
    if(matriz[2][2] == "-"):
        Olinha = 2
        Ocoluna = 2
        matriz[2][2] = "O"
        return 0

def way_1_baixo(matriz):
    if(matriz[1][1] == "-"):
        if(matriz[0][1] == "-"):
            Olinha = 0
            Ocoluna = 1
            matriz[0][1] = "O"
            return 0
    if(matriz[2][0] == "-"):
        if(matriz[2][2] == "-"):
            Olinha = 2
            Ocoluna = 2
            matriz[2][2] = "O"
            return 0
    if(matriz[1][1] == "-"):
        Olinha = 1
        Ocoluna = 1
        matriz[1][1] = "O"
        return 0
    if(matriz[0][1] == "-"):
        Olinha = 0
        Ocoluna = 1
        matriz[0][1] = "O"
        return 0
    if(matriz[2][0] == "-"):
        Olinha = 2
        Ocoluna = 0
        matriz[2][0] = "O"
        return 0
    if(matriz[2][2] == "-"):
        Olinha = 2
        Ocoluna = 2
        matriz[2][2] = "O"
        return 0

def way_2_baixo(matriz):
    if(matriz[1][2] == "-"):
        if(matriz[0][2] == "-"):
            Olinha = 0
            Ocoluna = 2
            matriz[0][2] = "O"
            return 0
    if(matriz[1][1] == "-"):
        if(matriz[0][0] == "-"):
            Olinha = 0
            Ocoluna = 0
            matriz[0][0] = "O"
            return 0
    if(matriz[2][1] == "-"):
        if(matriz[2][0] == "-"):
            Olinha = 2
            Ocoluna = 0
            matriz[2][0] = "O"
            return 0
    if(matriz[1][2] == "-"):
        Olinha = 1
        Ocoluna = 2
        matriz[1][2] = "O"
        return 0
    if(matriz[1][1] == "-"):
        Olinha = 1
        Ocoluna = 1
        matriz[1][1] = "O"
        return 0
    if(matriz[2][1] == "-"):
        Olinha = 2
        Ocoluna = 1
        matriz[2][1] = "O"
    if(matriz[0][2] == "-"):
        Olinha = 0
        Ocoluna = 2
        matriz[0][2] = "O"
        return 0
    if(matriz[0][0] == "-"):
        Olinha = 0
        Ocoluna = 0
        matriz[0][0] = "O"
        return 0
    if(matriz[2][0] == "-"):
        Olinha = 2
        Ocoluna = 0
        matriz[2][0] = "O"
        return 0



def quadradoPerfeito(matriz):
    global Olinha
    global Ocoluna
    n = Olinha
    m = Ocoluna
    if( n == 2 and m == 0):
        way_0_baixo(matriz)
    elif( n == 2 and m == 1):
        way_1_baixo(matriz)
    elif( n == 2 and m == 2):
        way_2_baixo(matriz)
    elif( n == 1 and m == 0):
        way_0_meio(matriz)
    elif( n == 1 and m == 1):
        way_1_meio(matriz)
    elif( n == 1 and m == 2):
        way_2_meio(matriz)
    elif( n == 0 and m == 0):
        way_0_cima(matriz)
    elif( n == 0 and m == 1):
        way_1_cima(matriz)
    elif( n == 0 and m == 2):
        way_2_cima(matriz)



Matriz = [['-','-','-'],['-','-','-'],['-','-','-']]

isTrue = True

while(isTrue):
    #print(jogou)
    printMatriz(Matriz)
    n = int(input("Digite a linha da matriz"))
    m = int(input("Digite a coluna da matriz"))
    Matriz[n][m] = 'X'

    auxOlinha = Olinha
    auxOcoluna = Ocoluna
    
    if( n == 2 and m == 0):
        vertical_0_baixo(Matriz,n,m)
    elif( n == 2 and m == 1):
        vertical_1_baixo(Matriz,n,m)
    elif( n == 2 and m == 2):
        vertical_2_baixo(Matriz,n,m)
    elif( n == 1 and m == 0):
        vertical_Meio0(Matriz,n,m)
    elif( n == 1 and m == 1):
        vertical_Meio1(Matriz,n,m)
    elif( n == 1 and m == 2):
        vertical_Meio2(Matriz,n,m)
    elif( n == 0 and m == 0):
        vertical_Cima0(Matriz,n,m)
    elif( n == 0 and m == 1):
        vertical_Cima1(Matriz,n,m)
    elif( n == 0 and m == 2):
        vertical_Cima2(Matriz,n,m)

    os.system('cls')

    if(Matriz[0][0] != "-" and Matriz[0][1] != "-" and Matriz[0][2] != "-" and Matriz[1][0] != "-" and Matriz[1][1] != "-" and
Matriz[1][2] != "-" and Matriz[2][0] != "-" and Matriz[2][1] != "-" and Matriz[2][2] != "-"):
        print("Empate")
        isTrue = False

    if(vencedor == 1):
        print("X venceu")
    if(vencedor == 0):
        print("O Venceu")
    #print(jogou)
    #print(Olinha,Ocoluna)
    

printMatriz(Matriz)
    


