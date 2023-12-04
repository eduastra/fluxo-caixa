from tkinter import *
#from tkinter import winsys
import time

# função para atualizar o relógio
def atualizar_relogio():
    relogio['text'] = time.strftime('%H:%M:%S')
    relogio.after(1000, atualizar_relogio) # chama a função novamente após 1 segundo (1000 ms)

# criando a janela principal
janela_principal = Tk()
janela_principal.title('Janela Principal')

# definindo o tamanho da janela principal
largura_janela = 840
altura_janela = 650

# obrigando a janela a manter as dimensões especificadas
janela_principal.minsize(largura_janela, altura_janela)
janela_principal.maxsize(largura_janela, altura_janela)

# criando a janela que contém os botões
janela_secundaria = Frame(janela_principal)
janela_secundaria.pack(expand=True, fill=BOTH)

# criando os botões
botao1 = Button(janela_secundaria, text='Botão 1', font=('Arial', 22))
botao2 = Button(janela_secundaria, text='Botão 2')
botao3 = Button(janela_secundaria, text='Botão 3')
botao4 = Button(janela_secundaria, text='Botão 4')

# posicionando os botões na janela secundária
botao1.pack(side=LEFT, padx=50, pady=50)
botao2.pack(side=LEFT, padx=50, pady=50)
botao3.pack(side=LEFT, padx=50, pady=50)
botao4.pack(side=LEFT, padx=50, pady=50)

# criando o relogio
relogio = Label(janela_principal, font=('Arial', 40), bg='white')
relogio.pack(pady=20)

# chamando a função atualizar_relogio para iniciar o relógio
atualizar_relogio()

# define a função para alternar a tela cheia
def toggle_fullscreen(event):
    # obtém o estado atual da tela cheia
    is_fullscreen = root.attributes('-fullscreen')
    
    # se a tela não estiver em modo cheio
    if not is_fullscreen:
        # alterna para o modo cheio
        root.attributes('-fullscreen', True)
    else:
        # alterna para o modo janela
        root.attributes('-fullscreen', False)

# define a função para fechar a janela principal
def close_program():
    janela_principal.destroy()

# define a função para maximizar a janela principal
def maximize_window():
    janela_principal.state('zoomed')

# associa a função toggle_fullscreen ao evento <F11>
janela_principal.bind('<F11>', toggle_fullscreen)

# associa a função close_program ao evento <Escape>
janela_principal.bind('<Escape>', close_program)

# associa a função maximize_window ao evento <Double-Button-1>
janela_principal.bind('<Double-Button-1>', maximize_window)

# loop principal
janela_principal.mainloop()