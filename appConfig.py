from tkinter import *
from tkinter.font import Font
from consts import *
from function import functions as f

class AppConfig():
    def __init__(self):
        self.master = Tk()
        
        #====Imagens====#
        self.logoPET = PhotoImage(file="imagens/petLogoSmall.png")
        self.logoLinus = PhotoImage(file="imagens/linusLogoSmall.png")
        self.logoX1 = PhotoImage(file="imagens/logoX1.png")
        self.botaoAzulEscrito = PhotoImage(file="imagens/botaoAzulEscrito.png")
        self.botaoAmareloEscrito = PhotoImage(file="imagens/botaoAmareloEscrito.png")
        self.botaoFatosUFJF = PhotoImage(file="imagens/botaoFatosUFJF.png")
        self.imgFundoPergResp = PhotoImage(file="imagens/fundoPergResp.png")

        #====Fontes====#
        self.fontTema = Font(
            family="Lovelo Black",
            size=19,
            weight="bold")
        self.fontPergunta = Font(
            family="Lovelo Black",
            size=30,
            weight="bold")
        self.fontRespostas = Font(
            family = "GlacialIndifference-Regular",
            size=24,
            weight='normal')
        
        #====Configurações da master====#
        self.master.title("Roleta")
        self.master.iconphoto(False, self.logoX1)
        self.master.geometry("1280x720")
        self.master.config(background=AZULESCURO)
        
    def SetupFrames(self):
        #FRAME QUE APARECE AS PERGUNTAS E AS OPÇÕES
        self.framePergResp = Frame(
            self.master,
            background=AZULMEDIO,
            bd=4)
        self.framePergResp.place(relx=0.02, rely=0.22, relwidth=0.96, relheight=0.61)
        
        #SUBFRAME QUE APARECE A PERGUNTA
        self.framePergunta = Frame(
            self.framePergResp,
            background=AZULMEDIO,
            bd=4)
        self.framePergunta.place(relx=0, rely=0, relwidth=1, relheight=0.47)
        
        #SUBFRAME QUE APARECE AS OPÇÕES
        self.frameRespostas = Frame(
            self.framePergResp,
            background=AZULMEDIO,
            bd=4)
        self.frameRespostas.place(relx=0, rely=0.47, relwidth=1, relheight=0.53)
        
        #FRAME DOS BOTÕES
        self.frameBotoes = Frame(
            self.master,
            background=AZULESCURO,
            bd=4)
        self.frameBotoes.place(relx=0.00, rely=0.83, relwidth=1, relheight=0.16)
        
        #FRAMES DAS LOGOS
        self.frameLogos = Frame(
            self.master,
            background=AZULESCURO,
            bd=4)
        self.frameLogos.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2)
              
    def SetupTextos(self):
        #TEXTO QUE MOSTRA O TEMA
        self.txtTema = Label(
            self.framePergunta,
            font=self.fontTema,
            fg=PRETO,
            bd=10,
            text="",
            background=AZULMEDIO)

        #TEXTO QUE MOSTRA A PERGUNTA
        self.txtPergunta = Label(
            self.framePergunta,
            font=self.fontPergunta,
            fg=PRETO,
            bd=10,
            text="",
            wraplength=1225, 
            background=AZULMEDIO)
        
        self.txtTema.place(relx=0, rely=0, relwidth=1, relheight=0.3)
        self.txtPergunta.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)
            
    def SetupBotoes(self):
        #OPÇÃO A
        self.botaoA = Button(
            self.frameRespostas,
            relief=GROOVE,
            font=self.fontRespostas,
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
                botao=self.botaoA))

        #OPÇÃO B
        self.botaoB = Button(
            self.frameRespostas,
            relief=GROOVE,
            font=self.fontRespostas,
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
                botao=self.botaoB))

        #OPÇÃO C
        self.botaoC = Button(
            self.frameRespostas,
            relief=GROOVE,
            font=self.fontRespostas,
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
                botao=self.botaoC))

        #OPÇÃO D
        self.botaoD = Button(
            self.frameRespostas,
            relief=GROOVE,
            font=self.fontRespostas,
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
                botao=self.botaoD))

        #BOTAO DO SORTEIO NORMAL
        self.botaoSorteioNormal = Button(
            self.frameBotoes,
            bd=0,
            image=self.botaoAzulEscrito,
            background=AZULESCURO,
            foreground=BRANCO,
            activebackground=AZULESCURO,
            activeforeground=PRETO, 
            command=lambda: f.funSorteio(
                self=f,
                dificuldade="N", 
                txtTema=self.txtTema, 
                txtPergunta=self.txtPergunta, 
                botaoA=self.botaoA, 
                botaoB=self.botaoB, 
                botaoC=self.botaoC, 
                botaoD=self.botaoD))

        #BOTAL DO SORTEIO DIFICL
        self.botaoSorteioDificil = Button(
            self.frameBotoes,
            bd=0,
            image=self.botaoAmareloEscrito,
            background=AZULESCURO,
            foreground=BRANCO,
            activebackground=AZULESCURO,
            activeforeground=PRETO, 
            command=lambda: f.funSorteio(
                self=f,
                dificuldade="D", 
                txtTema=self.txtTema, 
                txtPergunta=self.txtPergunta, 
                botaoA=self.botaoA, 
                botaoB=self.botaoB, 
                botaoC=self.botaoC, 
                botaoD=self.botaoD))

        #BOTAO SORTEIO FATOS DA UF
        self.botaoFatosUf = Button(
            self.frameBotoes,
            image=self.botaoFatosUFJF,
            bd=0,
            background=AZULESCURO,
            foreground=BRANCO,
            activebackground=AZULESCURO,
            command= lambda: f.funSorteio(
                self=f,
                dificuldade="F", 
                txtTema=self.txtTema, 
                txtPergunta=self.txtPergunta, 
                botaoA=self.botaoA, 
                botaoB=self.botaoB, 
                botaoC=self.botaoC, 
                botaoD=self.botaoD))
        
        self.botaoA.place(relx=0.05, rely=0.05, relwidth=0.43, relheight=0.4)
        self.botaoB.place(relx=0.52, rely=0.05, relwidth=0.43, relheight=0.4)
        self.botaoC.place(relx=0.05, rely=0.55, relwidth=0.43, relheight=0.4)
        self.botaoD.place(relx=0.52, rely=0.55, relwidth=0.43, relheight=0.4)
        
        self.botaoSorteioNormal.place(relx=0.02, rely=0.02, relwidth=0.29, relheight=0.96)
        self.botaoFatosUf.place(relx=(0.33+0.02),rely=0.02, relwidth=0.29, relheight=0.96)
        self.botaoSorteioDificil.place(relx=(0.66+0.02), rely=0.02, relwidth=0.29, relheight=0.96)
        
    def SetupLogos(self):
        self.logoPETLabel = Label(
            self.frameLogos,
            background=AZULESCURO,
            image=self.logoPET)

        self.logoLinusLabel = Button(
            self.frameLogos,
            background=AZULESCURO,
            activebackground=AZULESCURO,
            bd=0,
            image=self.logoLinus,
            command = lambda: f.reset(
                f,
                botaoA=self.botaoA,
                botaoB=self.botaoB,
                botaoC=self.botaoC,
                botaoD=self.botaoD,
                txtTema=self.txtTema,
                txtPerg=self.txtPergunta))
        
        self.logoPETLabel.place(relx=0.53, rely=0.02, relwidth=0.44, relheight=0.96)
        self.logoLinusLabel.place(relx=0.03, rely=0.02, relwidth=0.44, relheight=0.96)
