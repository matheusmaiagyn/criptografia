from tkinter import *
from tkinter import messagebox

codalpha = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c', 'v', 'b', 'n', 'm',
            '#', '5', '4', '6', '7', '2', '1', '3', '9', '0', '8', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
            'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '&', 'õ', 'é', '[', 'ã', 'á', 'í', '{', '*', '@', '}']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'x', 'w', 'y', 'z', 'ç',
         '1', '2', '3', '4', '5', '6' '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'X', 'W', 'Y', 'Z', 'Ç', 'ã', 'õ', 'é', 'ô', 'í', 'á', ':', '.', ',', ' ']

#SE A CHECKBOX FOR MARCADA MOSTRA ALERTAS
def checkauto():
       if auto.get() == 1:
              messagebox.showinfo('Atenção', 'O limite de criptografia para essa opção é 54 vezes! \n\nCaso queira criptografar mais vezes, desmarque essa opção!')
              messagebox.showinfo('Atenção', 'Ao descriptografar sua mensagem essa opção não precisa ser marcada novamente!')

#FUNÇÃO PARA CRIPTOGRAFAR
def criptografar():
       key = ['w', 'd', 'v', 'e', 'f', 'b', 'r', 'g', 'n', 'o']
       number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
       qtcrip = str(cript.get())   #PEGA A CHAVE
       cripqt = []   #CRIA A LISTA PARA A CHAVE
       cripqt.extend(qtcrip)       #ADD CHAVE PARA LISTA
       qtdcod = []
       for i in range(len(cripqt)):
              for j in range(len(number)):
                     if cripqt[i] == number[j]:
                            qtdcod.append(key[j])

       #TRATAMENTO PARA CASO A QUANTIDADE INSERIDA SEJA LETRAS OU NULO
       try:
              qtcrip = int(qtcrip)
       except:
              messagebox.showerror('Erro', 'Digite a quantidade em números!')

       #SE A OPÇÃO DE DESCRIPTOGRAFAR AUTOMATICAMENTE FOI ESCOLHIDA, TRANDORMA A QUANTIDADE DE CRIPTOGRAFIA EM UMA CHAVE (ATÉ 54 NÚMEROS)
       if auto.get() == 1:
              keyauto = ['m', 'n', 'b', 'v', 'c', 'x', 'z', 'ç', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'p', 'o', 'i', 'u', 'y', 't', 'r', 'e', 'w', 'q',
                         'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'Ç', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'P', 'O', 'I', 'U' ,'Y', 'T', 'R', 'E', 'W', 'Q']
              for i in range(1, 55):
                     if qtcrip == i:
                            ncrip = keyauto[i-1]

       #PEGA A MENSAGEM A SER CRIPTOGRAFADA
       msg = e.get()
       msgli = []
       msgli.extend(msg)    #ADICIONA A MENSAGEM PARA UMA LISTA
       crip = 0 #CONTADOR
       codmsg = []
       for k in range(qtcrip):
              for i in range(len(msgli)):
                     for j in range(len(alpha)):
                            if msgli[i] == alpha[j]:
                                   codmsg.append(codalpha[j])
              msgli = codmsg
              cod = codmsg
              codmsg = []

       #INSERE VALORES DE CONTROLE PARA DESCRIPTOGRAFAR A MENSAGEM
       cod.insert(0, 1)
       cod.insert(1, 1)

       #CASO A DESCRIPTOGRAFIA SEJA AUTOMÁTICA
       if auto.get() == 1:
              #TRATAMENTO PARA CASO O USUÁRIO COLOQUE MAIS DE 54 VEZES A QUANTIDADE DE CRIPTOGRAFIA
              try:
                     #RETIRAR E INSERIR VALORES DE CONTROLE
                     cod.pop(1)
                     cod.pop(0)
                     cod.insert(0, ncrip)
                     cod.insert(1, 'a')
                     msgcod.set(''.join(str(i) for i in cod))  #DAR PRINT DA MENSAGEM NA TELA
              except:
                     messagebox.showerror('Erro', 'O limite de criptografia é 54 vezes! \n\nCaso queira criptografar mais, desmarque a opção "Descriptografar automaticamente"!')
       #CASO NÃO SEJA DESCRIPTOGRAFIA AUTOMÁTICA
       else:
              msgcod.set(''.join(str(i) for i in cod))  #PRINTAR A MENSAGEM NA TELA
              vchave = qtcrip, 'ou', ''.join([str(i) for i in qtdcod])       #PRINTAR A CHAVE A SER UTILIZADA
              vChave.set(vchave)   #PRINTAR A CHAVE A SER UTILIZADA
       auto.set(0)   #DESMARCA OPÇÃO DE DESCRIPTOGRAFIA AUTOMÁTICA

#FUNÇÃO PARA DESCRIPTOGRAFAR
def descriptografar():
       #PEGA AM ENSAGEM A SER DESCRIPTOGRAFADA
       msg = e.get()
       msgli = []
       msgli.extend(msg)    #ADICIONA A MENSAGEM A UMA LISTA
       crip = 0      #CONTADOR
       if msgli[1] == 'a' or msgli[1] == 'A':  #CASO NA HORA DE CRIPTOGRAFAR A OPÇÃO DE DESCRIPTOGRAFAR AUTOMÁTICAMENTE TENHA SIDO MARCADA, TRANSFORMA A LETRA DE CONTROLE NA MENSAGEM NA QUANTIDADE DE VEZES QUE SERÁ DESCRIPTOGRAFADA
              if msgli[0] == 'm':
                     qtcrip = 1
              elif msgli[0] == 'n':
                     qtcrip = 2
              elif msgli[0] == 'b':
                     qtcrip = 3
              elif msgli[0] == 'v':
                     qtcrip = 4
              elif msgli[0] == 'c':
                     qtcrip = 5
              elif msgli[0] == 'x':
                     qtcrip = 6
              elif msgli[0] == 'z':
                     qtcrip = 7
              elif msgli[0] == 'ç':
                     qtcrip = 8
              elif msgli[0] == 'l':
                     qtcrip = 9
              elif msgli[0] == 'k':
                     qtcrip = 10
              elif msgli[0] == 'j':
                     qtcrip = 11
              elif msgli[0] == 'h':
                     qtcrip = 12
              elif msgli[0] == 'g':
                     qtcrip = 13
              elif msgli[0] == 'f':
                     qtcrip = 14
              elif msgli[0] == 'd':
                     qtcrip = 15
              elif msgli[0] == 's':
                     qtcrip = 16
              elif msgli[0] == 'a':
                     qtcrip = 17
              elif msgli[0] == 'p':
                     qtcrip = 18
              elif msgli[0] == 'o':
                     qtcrip = 19
              elif msgli[0] == 'i':
                     qtcrip = 20
              elif msgli[0] == 'u':
                     qtcrip = 21
              elif msgli[0] == 'y':
                     qtcrip = 22
              elif msgli[0] == 't':
                     qtcrip = 23
              elif msgli[0] == 'r':
                     qtcrip = 24
              elif msgli[0] == 'e':
                     qtcrip = 25
              elif msgli[0] == 'w':
                     qtcrip = 26
              elif msgli[0] == 'q':
                     qtcrip = 27
              elif msgli[0] == 'M':
                     qtcrip = 28
              elif msgli[0] == 'N':
                     qtcrip = 29
              elif msgli[0] == 'B':
                     qtcrip = 30
              elif msgli[0] == 'V':
                     qtcrip = 31
              elif msgli[0] == 'C':
                     qtcrip = 32
              elif msgli[0] == 'X':
                     qtcrip = 33
              elif msgli[0] == 'Z':
                     qtcrip = 34
              elif msgli[0] == 'Ç':
                     qtcrip = 35
              elif msgli[0] == 'L':
                     qtcrip = 36
              elif msgli[0] == 'K':
                     qtcrip = 37
              elif msgli[0] == 'J':
                     qtcrip = 38
              elif msgli[0] == 'H':
                     qtcrip = 39
              elif msgli[0] == 'G':
                     qtcrip = 40
              elif msgli[0] == 'F':
                     qtcrip = 41
              elif msgli[0] == 'D':
                     qtcrip = 42
              elif msgli[0] == 'S':
                     qtcrip = 43
              elif msgli[0] == 'A':
                     qtcrip = 44
              elif msgli[0] == 'P':
                     qtcrip = 45
              elif msgli[0] == 'O':
                     qtcrip = 46
              elif msgli[0] == 'I':
                     qtcrip = 47
              elif msgli[0] == 'U':
                     qtcrip = 48
              elif msgli[0] == 'Y':
                     qtcrip = 49
              elif msgli[0] == 'T':
                     qtcrip = 50
              elif msgli[0] == 'R':
                     qtcrip = 51
              elif msgli[0] == 'E':
                     qtcrip = 52
              elif msgli[0] == 'W':
                     qtcrip = 53
              elif msgli[0] == 'Q':
                     qtcrip = 54
              msgli.pop(1)
              msgli.pop(0)

       #CASO N TENHA SIDO AUTOMÁTICA
       else:
              try:   #TRATAMENTO DE ERRO CASO NÃO TENHA INSERIDO NADA NO CAMPO DE QUANTIDADE
                     qtcrip = str(cript.get())   #PEGA QUANTIDADE DE VEZES
                     cripqt = []
                     cripqt.extend(qtcrip)       #ADICIONA PARA UMA LISA
                     qtdcod = ['1' if x == 'w' else     #TRANFORMA LETRAS DIGITAS EM NÚMEROS
                               '2' if x == 'd' else
                               '3' if x == 'v' else
                               '4' if x == 'e' else
                               '5' if x == 'f' else
                               '6' if x == 'b' else
                               '7' if x == 'r' else
                               '8' if x == 'g' else
                               '9' if x == 'n' else
                               '0' if x == 'o' else
                               '1' if x == 'W' else
                               '2' if x == 'D' else
                               '3' if x == 'V' else
                               '4' if x == 'E' else
                               '5' if x == 'F' else
                               '6' if x == 'B' else
                               '7' if x == 'R' else
                               '8' if x == 'G' else
                               '9' if x == 'N' else
                               '0' if x == 'O' else
                               '1' if x == x else       #CASO A LETRA DIGITADA NÃO SEJA NENHUMA VÁLIDA, É TRANSFORMADA EM 1
                               x for x in cripqt]
                     qtcrip = int(''.join((str(i) for i in qtdcod))) #TRANSFORMA A QUANTIDADE DE DESCRIPTOGRAFIA EM VARIÁVEL INTEIRO
              except:
                     messagebox.showerror('Erro', 'Digite a chave para a descriptografia!')

       codmsg = []
       for k in range(qtcrip):
              for i in range(len(msgli)):
                     for j in range(len(codalpha)):
                            if msgli[i] == codalpha[j]:
                                   codmsg.append(alpha[j])
              msgli = codmsg
              cod = codmsg
              codmsg = []

       msgcod.set(''.join(str(i) for i in cod))  #PRINT DA MENSAGEM FINAL
       auto.set(0)   #DESMARCA OPÇÃO DE DESCRIPTOGRAFIA AUTOMÁTICA

#DECLARAÇÃO DA TELA
master = Tk()
master.configure(bg='black')       #COR DA TELA
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_rowconfigure(3, weight=1)
master.grid_columnconfigure(2, weight=1)
master.wm_resizable(False, False)         #NÃO PERMITE AUMENTAR OU DIMINUIR O TAMANHO DA TELA
master.wm_title('Encript')         #TÍTULO DO PROGRAMA
window_height = 300         #TAMANHO
window_width = 650   #TAMANHO
screen_width = master.winfo_screenwidth()        #TAMANHO DE CONTROLE PARA CENTRALIZAR
screen_height = master.winfo_screenheight()      #TAMANH DE CONTROLE PARA CENTRALIZAR
x_cord = int((screen_width/2) - (window_width/2))       #CENTRALIZAR TELA
y_cord = int((screen_height/2) - (window_height/2))     #CENTRALIZAR TELA
master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cord, y_cord))  #FORMATA O TAMANHO DA TELA BASEADO NAS VARIÁVEIS ANTERIORES

auto = IntVar()      #VARIÁVEL DE CONTROLE DA CHECKBOX
auto.set(0)   #VALORP ADRÃO DA VÁRIAVEL

topFrame = Frame(master, bg='black')      #FRAME TOP
topFrame.grid(column=1, row=1)     #ESPECIFICAÇÕES
bottonFrame = Frame(master, bg='black')   #FRAME BOT
bottonFrame.grid(column=1, row=2)  #ESPECIFICAÇÕES

cript=Entry(topFrame, width=100, bg='black', highlightbackground='#00a32c', highlightthickness='2', fg='#00d90e')      #ENTRADA DE QUANTIDADE DE CRIPTOGRAFIA OU DESCRIPTOGRAFIA
cript.pack(side=BOTTOM)     #MOSTRAR ENTRADA NA TELA
texto = Label(topFrame, text='Digite quantas vezes você quer criptografar:', bg='black', fg='#00d90e')   #LABEL
texto.pack(side=BOTTOM)     #MOSTRAR LABEL

e=Entry(topFrame, width=100, bg='black', highlightbackground='#00a32c', highlightthickness='2', fg='#00d90e')   #ENTRADA DA MENSAGEM A SER CRIPTOGRAFADA OU DESCRIPTOGRAFADA
e.pack(side=BOTTOM)  #MOSTRAR ENTRADA NA TELA
texto = Label(topFrame, text='Digite sua mensagem:', bg='black', fg='#00d90e')      #LABEL
texto.pack(side=BOTTOM)     #MOSTRAR LABEL

checkbox_a = Checkbutton(bottonFrame, text='Descriptografar automaticamente', variable=auto, onvalue=1, offvalue=0, command=checkauto, bg='black', fg='#00d90e', selectcolor='black')        #CHECKBOX
checkbox_a.grid(row=1,columnspan=3)       #MOSTRAR CHECKBOX

spacebuttonframe = Frame(bottonFrame, width=50, bg='black')    #FRAME PARA SEPARAR OS BOTÕES
spacebuttonframe.grid(row=2, column=1)    #MOSTRAR BOTÃO

a = Button(bottonFrame,text='Criptografar', fg='red', bg='black', command=criptografar)    #BOTÃO DE CRIPTOGRAFAR
a.grid(row=2, column=0)     #MOSTRAR BOTÃO

b = Button(bottonFrame,text='Descriptografar', fg='red', bg='black', command=descriptografar)     #BOTÃO DE DESCRIPTOGRAFAR
b.grid(row=2, column=2      )#MOSTRAR BOTÃO

result = Label(bottonFrame, text='O resultado é:', bg='black') #LABEL
result.grid(columnspan=3)   #MOSTRAR LABEL

msgcod = StringVar() #VARIÁVEL DA MENSAGEM
vChave = StringVar() #VARIÁVEL DA CHAVE

lblMsg = Label(bottonFrame, text='A sua mensagem é:', bg='black', fg='#00d90e')     #LABEL
lblMsg.grid(columnspan=3)   #MOSTRAR LABEL
resultmsg = Entry(bottonFrame, textvariable=msgcod, state='readonly', justify='center', width=100, readonlybackground='black', highlightbackground='#00a32c', highlightthickness='2', fg='#00d90e') #CAMPO ONDE MOSTRAR RESULTADO
resultmsg.grid(columnspan=3)       #MOSTRAR CAMPO
lblChave = Label(bottonFrame, text='A chave para descriptografar é:', bg='black', fg='#00d90e')   #LABEL
lblChave.grid(columnspan=3)        #MOSTRAR LABEL
chave = Entry(bottonFrame, textvariable=vChave, state='readonly', justify='center', width=100, readonlybackground='black', highlightbackground='#00a32c', highlightthickness='2', fg='#00d90e')     #CAMPO PARA MOSTRAR CHAVE
chave.grid(columnspan=3)    #MOSTRAR CAMPO

master.mainloop()    #MANTER O PROGRAMA RODANDO ATÉ SER FECHADO!
