import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    conn = sqlite3.connect('myDataBase.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER                                          
       )  
   ''')
    conn.commit()
    conn.close()

def inserir_usuarios():
    nome  = entry_nome.get()
    idade = entry_idade.get()
    entr_id = entry_id.get()
    

    if nome and idade:
        conn = conectar()
        c = conn.cursor()    
        c.execute('INSERT INTO usuarios (id, nome, idade)values(?,?,?) ', ( entr_id, nome, idade))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados inseridos!')
        entry_nome.delete(0,tk.END)
        entry_idade.delete(0,tk.END)
        entry_id.delete(0,tk.END)
    else:
        messagebox.showerror('Erro','Preencha corretamente!')    

def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios  =  c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values = (usuario[0], usuario[1], usuario[2]))
    conn.close()        


def eliminar_():
    selecao = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ? ', (user_id))
        conn.commit()
        conn.close()