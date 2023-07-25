from tkinter import *
from tkinter.font import Font
from function import functions as f


PRETO = '#000000'
BRANCO = '#FFFFFF'
AZULMEDIO = '#2C6fAB'
AZULESCURO = '#035094'


master = Tk()


#====Imagens utilizadas====#
logoPET = PhotoImage(file="imagens/petLogoSmall.png")
logoLinus = PhotoImage(file="imagens/linusLogoSmall.png")
logoX1 = PhotoImage(file="imagens/logoX1.png")
botaoAzulEscrito = PhotoImage(file="imagens/botaoAzulEscrito.png")
botaoAmareloEscrito = PhotoImage(file="imagens/botaoAmareloEscrito.png")
botaoPergIngles = PhotoImage(file="imagens/botaoPergIngles.png")
botaoFatosUFJF = PhotoImage(file="imagens/botaoFatosUFJF.png")


#====Configurações da janela====#
master.title("Roleta")
master.iconphoto(False, logoX1)
master.geometry("1280x720")
master.state('zoomed')
master.config(background=AZULESCURO)


#====Fontes utilizadas====#
fontTema = Font(
    family="Lovelo Black",
    size=19,
    weight="bold")
fontPergunta = Font(
    family="Lovelo Black",
    size=30,
    weight="bold")
fontRespostas = Font(
    family = "GlacialIndifference-Regular",
    size=24,
    weight='normal')


#====Frames da página====#
framePergunta = Frame(
    master,
    background=AZULMEDIO,
    bd=4)
framePergunta.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.29)
frameRespostas = Frame(
    master,
    background=AZULMEDIO,
    bd=4)
frameRespostas.place(relx=0.02, rely=0.51, relwidth=0.96, relheight=0.32)
frameBotoes = Frame(
    master,
    background=AZULESCURO,
    bd=4)
frameBotoes.place(relx=0.00, rely=0.83, relwidth=1, relheight=0.16)
frameLogos = Frame(
    master,
    background=AZULESCURO,
    bd=4)
frameLogos.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2)


#====Botões====#
botaoA = Button(
    frameRespostas,
    relief=GROOVE,
    font=fontRespostas,
    bd=2,
    bg=AZULMEDIO,
    fg=BRANCO,
    activebackground=AZULMEDIO,
    activeforeground=PRETO,
    text="",
    wraplength=600,
    command=lambda: f.funOpcao(
        self=f, 
        opcao="A", 
        botao=botaoA))

botaoB = Button(
    frameRespostas,
    relief=GROOVE,
    font=fontRespostas,
    bd=2,
    fg=BRANCO,
    activebackground=AZULMEDIO,
    activeforeground=PRETO,
    bg=AZULMEDIO,
    text="",
    wraplength=600,
    command=lambda: f.funOpcao(
        self=f, 
        opcao="B", 
        botao=botaoB))

botaoC = Button(
    frameRespostas,
    relief=GROOVE,
    font=fontRespostas,
    bd=2,
    fg=BRANCO,
    activebackground=AZULMEDIO,
    activeforeground=PRETO,
    bg=AZULMEDIO,
    text="",
    wraplength=600,
    command=lambda: f.funOpcao(
        self=f, 
        opcao="C", 
        botao=botaoC))

botaoD = Button(
    frameRespostas,
    relief=GROOVE,
    font=fontRespostas,
    bd=2,
    fg=BRANCO,
    activebackground=AZULMEDIO,
    activeforeground=PRETO,
    bg=AZULMEDIO,
    text="",
    wraplength=600,
    command=lambda: f.funOpcao(
        self=f, 
        opcao="D", 
        botao=botaoD))

botaoSorteioNormal = Button(
    frameBotoes,
    bd=0,
    image=botaoAzulEscrito,
    background=AZULESCURO,
    foreground=BRANCO,
    activebackground=AZULESCURO,
    activeforeground=PRETO, 
    command=lambda: f.funSorteio(
        self=f,
        dificuldade="N", 
        txtTema=txtTema, 
        txtPergunta=txtPergunta, 
        botaoA=botaoA, 
        botaoB=botaoB, 
        botaoC=botaoC, 
        botaoD=botaoD))

botaoSorteioDificil = Button(
    frameBotoes,
    bd=0,
    image=botaoAmareloEscrito,
    background=AZULESCURO,
    foreground=BRANCO,
    activebackground=AZULESCURO,
    activeforeground=PRETO, 
    command=lambda: f.funSorteio(
        self=f,
        dificuldade="D", 
        txtTema=txtTema, 
        txtPergunta=txtPergunta, 
        botaoA=botaoA, 
        botaoB=botaoB, 
        botaoC=botaoC, 
        botaoD=botaoD))

botaoIngles = Button(frameBotoes,
    bd=0,
    image=botaoPergIngles,
    background=AZULESCURO,
    activebackground=AZULESCURO,
    command=lambda: f.funSorteio(
        self=f,
        dificuldade="E", 
        txtTema=txtTema, 
        txtPergunta=txtPergunta, 
        botaoA=botaoA, 
        botaoB=botaoB, 
        botaoC=botaoC, 
        botaoD=botaoD))

botaoFatosUf = Button(
    frameBotoes,
    image=botaoFatosUFJF,
    bd=0,
    background=AZULESCURO,
    foreground=BRANCO,
    activebackground=AZULESCURO,
    command= lambda: f.funSorteio(
        self=f,
        dificuldade="F", 
        txtTema=txtTema, 
        txtPergunta=txtPergunta, 
        botaoA=botaoA, 
        botaoB=botaoB, 
        botaoC=botaoC, 
        botaoD=botaoD))

#==== CRIAÇÃO DO TEXTO EM QUE APARECERÁ O TEMA E A PERGUNTA ====#
txtTema = Label(
    framePergunta,
    font=fontTema,
    fg=BRANCO,
    bd=10,
    text="",
    background=AZULMEDIO)

txtPergunta = Label(
    framePergunta,
    font=fontPergunta,
    fg=BRANCO,
    bd=10,
    text="",
    wraplength=1225, 
    background=AZULMEDIO 
)


#====Criação das logos====#
logoPETLabel = Label(
    frameLogos,
    background=AZULESCURO,
    image=logoPET)

logoLinusLabel = Button(
    frameLogos,
    background=AZULESCURO,
    activebackground=AZULESCURO,
    bd=0,
    image=logoLinus,
    command = lambda: f.reset(
        f,
        botaoA=botaoA,
        botaoB=botaoB,
        botaoC=botaoC,
        botaoD=botaoD,
        txtTema=txtTema,
        txtPerg=txtPergunta
    ))


#====Posicionamento dos Widgets====#
#---Texto da pergunta e tema---#
txtTema.place(relx=0, rely=0, relwidth=1, relheight=0.3)
txtPergunta.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

#---Botões de respostas---#
botaoA.place(relx=0.05, rely=0.05, relwidth=0.43, relheight=0.4)

botaoB.place(relx=0.52, rely=0.05, relwidth=0.43, relheight=0.4)

botaoC.place(relx=0.05, rely=0.55, relwidth=0.43, relheight=0.4)

botaoD.place(relx=0.52, rely=0.55, relwidth=0.43, relheight=0.4)

#---Botões de sorteio---#
botaoSorteioNormal.place(relx=0.02, rely=0.02, relwidth=0.225, relheight=0.96)

botaoFatosUf.place(relx=((0.245)+0.02),rely=0.02, relwidth=0.225, relheight=0.96)

botaoIngles.place(relx=(2*(0.245)+0.02), rely=0.02, relwidth=0.225, relheight=0.96)

botaoSorteioDificil.place(relx=(3*(0.245)+0.02), rely=0.02, relwidth=0.225, relheight=0.96)

#---Logos---#
logoPETLabel.place(relx=0.53, rely=0.02, relwidth=0.44, relheight=0.96)

logoLinusLabel.place(relx=0.03, rely=0.02, relwidth=0.44, relheight=0.96)

master.mainloop()