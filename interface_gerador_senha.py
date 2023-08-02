import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(tk.END, senha)

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Senha copiada")

def mostrar_senha():
    estado_atual = btn_mostrar["text"]
    if estado_atual == "Mostrar Senha":
        entry_senha.config(show="")
        btn_mostrar.config(text="Ocultar Senha")
    else:
        entry_senha.config(show="*")
        btn_mostrar.config(text="Mostrar Senha")

#Janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("300x220")

#Rótulo
label_tamanho = tk.Label(root, text = "Tamanho da Senha: ")
label_tamanho.pack(pady=5)

#Entrada para tamanho da senha
entry_tamanho = tk.Entry(root)
entry_tamanho.pack(pady=5)

#Botão para gerar senha
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
btn_gerar.pack(pady=10)

#Exibir a senha gerada
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

#Botão para copiar a senha
btn_copiar = tk.Button(root, text="Copiar Senha", command=copiar_senha)
btn_copiar.pack(pady=10)

#Botão para mostrar a senha
btn_mostrar = tk.Button(root, text="Mostrar Senha", command=mostrar_senha)
btn_mostrar.pack(pady=5)

#Executa a janela principal
root.mainloop()