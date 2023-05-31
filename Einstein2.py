# Importando tudo relacionado a biblioteca tkinter
from tkinter import *
import math

# Função
def calculo():
     a = int(entry_a.get())
     b = int(entry_b.get())
     c = int(entry_c.get())

     cor_fundo = '#394559'
  
     # Separando
     label_separar = Label(janela, width=30, height=1, text='~'*150, bg=cor_fundo, fg='white')
     label_separar.place(x=0,y=100)
     
     delta = int(math.pow(b, 2)- 4 * a * c)
     # Separando o delta em partes
     b_quadrado = int(math.pow(b, 2))
     quatro_vezes_a = int(-4 * a)
     quatro_a_vezes_c = int(quatro_vezes_a * c)

     # Mensagem delta
     label_msg_delta = Label(janela, width=20, height=1, text=f'Achando o valor de Delta:', bg='white', anchor=W)
     label_msg_delta.place(x=0, y=120)

     # Colocando o código na tela
     label_delta1 = Label(janela, width=30, height=1, text=f'delta = ({b})^2 - 4 * ({a}) * ({c})', anchor=W, bg=cor_fundo, fg='white' )
  
     label_delta2 = Label(janela, width=30, height=1, text=f'delta = ({b})^2 - 4 * ({a}) * ({c})', anchor=W, bg=cor_fundo, fg='white')

     label_delta3 = Label(janela, width=30, height=1, text=f'delta = {b_quadrado} - 4 * ({a}) * ({c})', anchor=W, bg=cor_fundo, fg='white')

     label_delta4 = Label(janela, width=30, height=1, text=f'delta = {b_quadrado} {quatro_vezes_a} * ({c})', anchor=W, bg=cor_fundo,  fg='white')
  
     label_delta5 = Label(janela, width=30, height=1, text=f'delta = ({b_quadrado}) + ({quatro_a_vezes_c})', anchor=W, bg=cor_fundo, fg='white')

     label_delta6 = Label(janela, width=30, height=1, text=f'delta = {delta}', anchor=W, bg='white')
  
     label_delta1.place(x=0, y=145)
     label_delta2.place(x=0, y=165)
     label_delta3.place(x=0, y=185)
     label_delta4.place(x=0, y=205)
     label_delta5.place(x=0, y=225)
     label_delta6.place(x=0, y=245)

     # condicional para caso o delta seja menor que zero(número negativo)
     if delta < 0:
       label_separar3 = Label(janela, width=30, height=1, text='~'*150, bg=cor_fundo, fg='white')
       label_separar3.place(x=0,y=265)
       label_msg_sem_raizes = Label(janela, width=20, height=1, text='Não possui raizes.', bg='white')
       label_msg_sem_raizes.place(x=0, y=285)
       
     if delta == 0:
       x = -b / 2*a
       # Separando
       label_separar3 = Label(janela, width=30, height=1, text='~'*150, bg=cor_fundo, fg='white')
       label_separar3.place(x=0,y=265)

      # label mensagem 
       label_msg_delta = Label(janela, width=40, height=1, text='O delta é igual a 0, então temos duas raizes iguais.')
       label_msg_delta.place(x=0,y=280)

       # label x com delta == 0
       label_x = Label(janela, width=10, height=7, text=f'x = {-b}\n      ----\n      2*({a})\n\nx = {-b}\n      ----\n      {2*a}', bg=cor_fundo, fg='white')
       label_r_x = Label(janela, width=10, height=1, text=f'x = {x}', bg='white')
       label_x.place(x=0,y=310)
       label_r_x.place(x=0, y=430)
       
      # caso o delta não seja nenhumas das condicionais acima, a conta vai seguir normal
     else:
       '''
       # achando o valor das duas raizes
       x1 = (-b+(math.sqrt(delta)) / (2*a)
       x2 = (-b-(math.sqrt(delta)) / (2*a)
       '''
       # separando o calculo em partes
       raiz_quadrada_delta = (int(math.sqrt(delta)))
       valor_b = -(b)
       menos_b_mais_raiz_quadrada_delta = - b + raiz_quadrada_delta
       menos_b_menos_raiz_quadrada_delta = - b - raiz_quadrada_delta
       denominador = 2*a
       divisao_x1 = menos_b_mais_raiz_quadrada_delta / denominador
       divisao_x2 = menos_b_menos_raiz_quadrada_delta / denominador
       label_separar2 = Label(janela, width=30, height=1, text='~'*150, bg='#394559', fg='white')
       label_separar2.place(x=0,y=265)

       label_msg_x1 = Label(janela, width=15, height=1, text='Achando o x1:', bg='white', anchor=W)

       label_msg_x2 = Label(janela, width=15, height=1, text='Achando o x2:', bg='white', anchor=W)

       label_msg_x1.place(x=0, y=285)
       label_msg_x2.place(x=125, y=285)
       
       label_x1 = Label(janela, width=15, height=12, text=f'x1 = -({b})+V({raiz_quadrada_delta})\n    -----\n2*({a})\n\nx1 = {-b} + {raiz_quadrada_delta}\n    -----\n{denominador}\n\nx1 = {menos_b_mais_raiz_quadrada_delta}\n     -----\n{denominador}', bg=cor_fundo, fg='white', anchor=W)
       label_r_x1 = Label(janela, width=15, height=1, text=f'x1 = {divisao_x1}')
       
       # Mostrando o valor de x1
       label_x1.place(x=0, y=305)
       label_r_x1.place(x=0, y=500)
       
       label_x2 = Label(janela, width=15, height=12, text=f'x2 = -({b})-V({raiz_quadrada_delta})\n    -----\n2*({a})\n\nx2 = {-b} - {raiz_quadrada_delta}\n    -----\n{denominador}\n\nx2 = {menos_b_menos_raiz_quadrada_delta}\n    -----\n{denominador}', bg=cor_fundo,  fg='white', anchor=W)
       label_r_x2 = Label(janela, width=15, height=1, text=f'x2 = {divisao_x2}')
       label_x2.place(x=130, y=305)
       label_r_x2.place(x=130, y=500)

cor_fundo0 = '#394559'

janela = Tk()
# Nome da janela
janela.title('Einstein 2')
# Dimenção da tela
janela.geometry('480x640')
# Cor de fundo da tela
janela.config(bg=cor_fundo0)
'''
# Icone da janela
janela.iconphoto(False, (PhotoImage(file='/storage/emulated/0/Download/icone_coracao.png')))
'''
# Mensagem para digitar o valor de a,b e c
label_mensagem = Label(janela, width=20, height=1, text='Digite o valor de A, B e C:', bg=cor_fundo0, fg='white')
label_mensagem.place(x=0, y=0)

# Texto das letras
# Texto 'a'
label_a = Label(janela, width=3, height=1, text='a:', bg='white')
label_a.place(x=0, y=20)
# Texto 'b'
label_b = Label(janela, width=3, height=1, text='b:', bg='white')
label_b.place(x=0, y=50)
# Texto 'c'
label_c = Label(janela, width=3, height=1, text='c:', bg='white')
label_c.place(x=0, y=80)

# Recebendo os valores
# Receber valor de a
entry_a = Entry(janela, width=10, font='Arial 5')
entry_a.place(x=30, y=22)
# Receber valor de b
entry_b = Entry(janela, width=10, font='Arial 5')
entry_b.place(x=30, y=52)
# Receber valor de c
entry_c = Entry(janela, width=10, font='Arial 5')
entry_c.place(x=30, y=82)

# Botão para fazer o calculo
botao = Button(janela, width=5,height=1, text='calcular', relief='raised', command=calculo)
botao.place(x=150, y=46)

# Esse codigo sempre tem que ficar no final do codigo (NÃO REMOVE ELE!!!)
janela.mainloop()