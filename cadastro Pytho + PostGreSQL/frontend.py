import customtkinter as ctk
from tkinter import ttk
from backend import validar_cadastro
from backend import inserir_usuario
from backend import buscar_usuario
from backend import buscar_recentes

janela = ctk.CTk()
janela.title("Cadastro")
janela.geometry('400x500')
janela.resizable(False, False)
#frame1
main_frame = ctk.CTkFrame(janela)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

titulo = ctk.CTkLabel(main_frame, text='Cadastro', font=("Arial", 22, "bold"))
titulo.pack(pady=10)

nome_label = ctk.CTkLabel(main_frame, text='Nome Completo')
nome_label.pack(anchor="w", padx=10)

nome_row = ctk.CTkFrame(main_frame, fg_color="transparent")
nome_row.pack(pady=5)

fn_entry = ctk.CTkEntry(nome_row, placeholder_text='Primeiro nome', width=140)
fn_entry.pack(side='left', padx=5)

ln_entry = ctk.CTkEntry(nome_row, placeholder_text='Último nome', width=140)
ln_entry.pack(side='left', padx=5)

email_label = ctk.CTkLabel(main_frame, text='Email')
email_label.pack(anchor="w", padx=10)

email_entry = ctk.CTkEntry(main_frame, placeholder_text='Digite seu E-mail', width=290)
email_entry.pack(pady=5)

telefone_label = ctk.CTkLabel(main_frame, text='Telefone')
telefone_label.pack(anchor="w", padx=10)

telefone_entry = ctk.CTkEntry(main_frame, placeholder_text='(00) 00000-0000', width=290)
telefone_entry.pack(pady=5)

endereco_label = ctk.CTkLabel(main_frame, text='Endereço')
endereco_label.pack(anchor="w", padx=10)

endereco_entry = ctk.CTkEntry(main_frame, placeholder_text='Digite seu endereço', width=290)
endereco_entry.pack(pady=5)

cadastro_label = ctk.CTkLabel(main_frame, text='')
cadastro_label.pack(pady=5)

def enviar():
    nome = fn_entry.get()
    sobrenome = ln_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get()

    resposta = validar_cadastro(nome, sobrenome, email, telefone, endereco)
    
    if resposta > 0:
        fn_entry.configure(placeholder_text='Nome inválido')
        ln_entry.configure(placeholder_text='Sobrenome inválido')
        email_entry.configure(placeholder_text='Email inválido')
        telefone_entry.configure(placeholder_text='Telefone inválido')
        endereco_entry.configure(placeholder_text='Endereço inválido')

        janela.after(3000, lambda: fn_entry.configure(placeholder_text='Primeiro nome'))
        janela.after(3000, lambda: ln_entry.configure(placeholder_text='Último nome'))
        janela.after(3000, lambda: email_entry.configure(placeholder_text='Digite seu E-mail'))
        janela.after(3000, lambda: telefone_entry.configure(placeholder_text='(00) 00000-0000'))
        janela.after(3000, lambda: endereco_entry.configure(placeholder_text='Digite seu endereço'))

    else:
        inserir_usuario(nome, sobrenome, email, telefone, endereco)
        cadastro_label.configure(text='Cadastro realizado com sucesso', text_color='green')
        janela.after(3000, lambda: cadastro_label.configure(text=''))

def tela2():
    main_frame.pack_forget()
    pagina_dois.pack(padx=20, pady=20, fill='both', expand=True)

def tela1():
    janela.geometry('400x500')
    pagina_dois.pack_forget()
    main_frame.pack(padx=20, pady=20, fill='both', expand=True)

def update():
    janela.geometry('700x500')
    carregar_tabela()
    tela2()

botao = ctk.CTkButton(main_frame, text='Enviar', command=enviar)
botao.pack()
x = ctk.CTkButton(main_frame, text='Cadastrados', command=update)
x.pack(pady=10)
#frame2
def buscar():
    email = entrya.get()
    dados = buscar_usuario(email)

    if dados:
        print(dados)
    else:
        print("Usuário não encontrado")

def carregar_tabela():
    for row in tabela.get_children():
        tabela.delete(row)

    dados = buscar_recentes()

    for usuario in dados:
        tabela.insert("", "end", values=usuario)

pagina_dois = ctk.CTkFrame(janela)
pagina_dois.pack(padx=20, pady=20, fill="both", expand=True)

container = ctk.CTkFrame(pagina_dois)
container.pack(fill="both", expand=True)

topo = ctk.CTkFrame(container, fg_color="transparent")
topo.pack(pady=40)

entrya = ctk.CTkEntry(topo, placeholder_text='Digite o Email do cadastrado', width=220)
entrya.pack(side='left', padx=5)

botao_buscar = ctk.CTkButton(topo, text='🔍', width=40, command=buscar)
botao_buscar.pack(side='left', padx=5)

espaco = ctk.CTkFrame(container, fg_color="transparent")
espaco.pack(expand=True)
#######tabela
tabela_frame = ctk.CTkFrame(espaco)
tabela_frame.pack(pady=10, fill="both", expand=True)

colunas = ("Nome", "Email", "Telefone")

tabela = ttk.Treeview(tabela_frame, columns=colunas, show="headings", height=5)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center")

tabela.pack(fill="both", expand=True)
########
rodape = ctk.CTkFrame(container, fg_color="transparent")
rodape.pack(pady=20)

botao_voltar = ctk.CTkButton(rodape, text='Voltar', command=tela1, width=250)
botao_voltar.pack(side='left', padx=10)

janela.mainloop()
