import pandas as pd
import random
from tkinter import *
from openpyxl import load_workbook
from consts import *

class functions:
    def __init__ (self, arquivoExc, pergunta, aba, numPergunta, numAba):
        self.arquivoExc = arquivoExc
        self.pergunta = pergunta
        self.aba = aba
        self.numPergunta = numPergunta
        self.numAba = numAba

    #Isso aqui é uma grande gambiarra, mas funciona, futuramente melhorar isso
    def funSorteio (self, dificuldade, txtTema, txtPergunta, botaoA, botaoB, botaoC, botaoD):
        if dificuldade == "N":
            self.numPergunta = random.randint(0, 9)
            self.numAba = random.randint(1, 6)
        elif dificuldade == "D":
            self.numPergunta = random.randint(10, 14)
            self.numAba = random.randint(1, 5)
        elif dificuldade == "E":
            self.numPergunta = random.randint(15, 18)
            self.numAba = random.randint(1, 6)
        elif dificuldade == "F":
            self.numAba = 6
            self.numPergunta = random.randint(0,9)
        elif dificuldade == "M":
            self.numAba = 0
            self.numPergunta = random.randint(0,18)

        self.aba = abas[self.numAba]
        self.arquivoExc = pd.read_excel("planilha/PerguntasX1.xlsx", sheet_name=self.aba)
        self.pergunta = self.arquivoExc.iloc[self.numPergunta, 0]

        if dificuldade == "N" or dificuldade == "D" or dificuldade == "F" or dificuldade == "M":
            txtTema["text"] = self.aba
        if dificuldade == "E":
            txtTema["text"] = ingAbas[self.numAba]

        txtPergunta["text"] = self.pergunta

        botaoA["bg"] = AZULMEDIO
        botaoB["bg"] = AZULMEDIO
        botaoC["bg"] = AZULMEDIO
        botaoD["bg"] = AZULMEDIO

        botaoA["fg"] = PRETO
        botaoB["fg"] = PRETO
        botaoC["fg"] = PRETO
        botaoD["fg"] = PRETO

        botaoA["text"] = self.arquivoExc.iloc[self.numPergunta, 1]
        botaoB["text"] = self.arquivoExc.iloc[self.numPergunta, 2]
        botaoC["text"] = self.arquivoExc.iloc[self.numPergunta, 3]
        botaoD["text"] = self.arquivoExc.iloc[self.numPergunta, 4]

    def funOpcao (self, opcao, botao):
        if opcao == "A":
            planilha = load_workbook("planilha\PerguntasX1.xlsx", data_only = True)
            aba = planilha[abas[self.numAba]]
            cor = aba[f'B{(self.numPergunta)+2}'].fill.start_color.index

            if cor == "FF00FF00" or cor == "FFFF0000":
                botao["bg"] = VERDE
                botao["fg"] = PRETO

            else:
                botao["bg"] = VERMELHO
                botao["fg"] = PRETO



        if opcao == "B":
            planilha = load_workbook("planilha\PerguntasX1.xlsx", data_only = True)
            aba = planilha[abas[self.numAba]]
            cor = aba[f'C{(self.numPergunta) + 2}'].fill.start_color.index

            if cor == "FF00FF00" or cor == "FFFF0000":
                botao["bg"] = VERDE
                botao["fg"] = PRETO

            else:
                botao["bg"] = VERMELHO
                botao["fg"] = PRETO


        if opcao == "C":
            planilha = load_workbook("planilha\PerguntasX1.xlsx", data_only = True)
            aba = planilha[abas[self.numAba]]
            cor = aba[f'D{(self.numPergunta)+2}'].fill.start_color.index

            if cor == "FF00FF00" or cor == "FFFF0000":
                botao["bg"] = VERDE
                botao["fg"] = PRETO

            else:
                botao["bg"] = VERMELHO
                botao["fg"] = PRETO


        if opcao == "D":
            planilha = load_workbook("planilha\PerguntasX1.xlsx", data_only = True)
            aba = planilha[abas[self.numAba]]
            cor = aba[f'E{(self.numPergunta)+2}'].fill.start_color.index

            if cor == "FF00FF00" or cor == "FFFF0000":
                botao["bg"] = VERDE
                botao["fg"] = PRETO

            else:
                botao["bg"] = VERMELHO
                botao["fg"] = PRETO
#                tocaSom("e")
    
    def reset(self, botaoA, botaoB, botaoC, botaoD, txtTema, txtPerg):
        botaoA["text"]=""
        botaoB["text"]=""
        botaoC["text"]=""
        botaoD["text"]=""
        txtTema["text"]=""
        txtPerg["text"]=""
        botaoA["bg"]=AZULMEDIO
        botaoB["bg"]=AZULMEDIO
        botaoC["bg"]=AZULMEDIO
        botaoD["bg"]=AZULMEDIO