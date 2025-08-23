import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SistemaHorasTrabalhadas:
    def __init__(self):
        self.registros = []
        # Listas pré-definidas de colaboradores e clientes válidos
        self.colaboradores_validos = ["João Silva", "Maria Santos", "Pedro Costa", "Ana Oliveira", "Yago"]
        self.clientes_validos = ["Cliente A", "Cliente B", "Cliente C", "Cliente D", "Rian"]
    
    def verificar_colaborador_valido(self, nome):
        return nome in self.colaboradores_validos
    
    def verificar_cliente_valido(self, nome):
        return nome in self.clientes_validos
    
    def registrar_horas(self, colaborador, cliente, tarefa, data, horas_inicio, horas_fim):
        horas_trabalhadas = self._calcular_horas(horas_inicio, horas_fim)
        registro = {
            'colaborador': colaborador,
            'cliente': cliente,
            'tarefa': tarefa,
            'data': data,
            'horas_inicio': horas_inicio,
            'horas_fim': horas_fim,
            'horas_trabalhadas': horas_trabalhadas
        }
        self.registros.append(registro)
        return registro
    
    def _calcular_horas(self, inicio, fim):
        formato = "%H:%M"
        inicio_dt = datetime.strptime(inicio, formato)
        fim_dt = datetime.strptime(fim, formato)
        diferenca = fim_dt - inicio_dt
        return diferenca.total_seconds() / 3600
    
    def relatorio_por_colaborador(self, colaborador, periodo=None):
        horas_totais = 0
        relatorio = []
        
        for registro in self.registros:
            if registro['colaborador'] == colaborador:
                if periodo is None or registro['data'] == periodo:
                    relatorio.append(registro)
                    horas_totais += registro['horas_trabalhadas']
        
        return {
            'colaborador': colaborador,
            'periodo': periodo or 'Todos os períodos',
            'registros': relatorio,
            'total_horas': horas_totais
        }
    
    def relatorio_por_cliente(self, cliente, periodo=None):
        horas_totais = 0
        relatorio = []
        
        for registro in self.registros:
            if registro['cliente'] == cliente:
                if periodo is None or registro['data'] == periodo:
                    relatorio.append(registro)
                    horas_totais += registro['horas_trabalhadas']
        
        return {
            'cliente': cliente,
            'periodo': periodo or 'Todos os períodos',
            'registros': relatorio,
            'total_horas': horas_totais
        }
    
    def gerar_relatorio_completo(self, colaborador=None, cliente=None, data=None):
        resultados = []
        total_horas = 0
        
        for registro in self.registros:
            # Aplicar filtros
            if colaborador and registro['colaborador'] != colaborador:
                continue
            if cliente and registro['cliente'] != cliente:
                continue
            if data and registro['data'] != data:
                continue
                
            resultados.append(registro)
            total_horas += registro['horas_trabalhadas']
        
        return resultados, total_horas


class JanelaCadastro:
    def __init__(self, parent, titulo, tipo, sistema, callback):
        self.janela = tk.Toplevel(parent)
        self.janela.title(titulo)
        self.janela.geometry("300x150")
        self.janela.resizable(False, False)
        self.janela.grab_set()  # Torna a janela modal
        
        self.sistema = sistema
        self.tipo = tipo  # 'colaborador' ou 'cliente'
        self.callback = callback
        
        self.criar_interface()
    
    def criar_interface(self):
        ttk.Label(self.janela, text=f"Nome do {self.tipo}:").pack(pady=10)
        
        self.entry_nome = ttk.Entry(self.janela, width=30)
        self.entry_nome.pack(pady=5)
        self.entry_nome.focus()
        
        frame_botoes = ttk.Frame(self.janela)
        frame_botoes.pack(pady=10)
        
        btn_salvar = ttk.Button(frame_botoes, text="Salvar", command=self.salvar)
        btn_salvar.pack(side=tk.LEFT, padx=5)
        
        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar", command=self.janela.destroy)
        btn_cancelar.pack(side=tk.LEFT, padx=5)
    
    def salvar(self):
        nome = self.entry_nome.get().strip()
        if nome:
            if self.tipo == 'colaborador':
                self.sistema.colaboradores_validos.append(nome)
            else:
                self.sistema.clientes_validos.append(nome)
            
            self.callback(nome)
            self.janela.destroy()
            messagebox.showinfo("Sucesso", f"{self.tipo.capitalize()} cadastrado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, digite um nome válido.")


class JanelaRelatorio:
    def __init__(self, parent, sistema, colaborador=None, cliente=None, data=None):
        self.janela = tk.Toplevel(parent)
        self.janela.title("Relatório Detalhado")
        self.janela.geometry("1000x500")
        self.janela.grab_set()
        
        self.sistema = sistema
        self.colaborador = colaborador
        self.cliente = cliente
        self.data = data
        
        self.criar_interface()
        self.carregar_dados()
    
    def criar_interface(self):
        # Informações do relatório
        frame_info = ttk.LabelFrame(self.janela, text="Filtros Aplicados")
        frame_info.pack(fill='x', padx=10, pady=5)
        
        info_text = f"Colaborador: {self.colaborador or 'Todos'} | "
        info_text += f"Cliente: {self.cliente or 'Todos'} | "
        info_text += f"Data: {self.data or 'Todas'}"
        
        ttk.Label(frame_info, text=info_text).pack(pady=5)
        
        # Treeview para mostrar resultados
        columns = ('colaborador', 'cliente', 'tarefa', 'data', 'inicio', 'fim', 'horas')
        self.tree = ttk.Treeview(self.janela, columns=columns, show='headings')
        
        headings = ['Colaborador', 'Cliente', 'Tarefa', 'Data', 'Início', 'Fim', 'Horas']
        for col, heading in zip(columns, headings):
            self.tree.heading(col, text=heading)
            if col == 'tarefa':
                self.tree.column(col, width=200)  # Largura maior para tarefa
            else:
                self.tree.column(col, width=120)
        
        # Scrollbar para a treeview
        scrollbar = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill='both', expand=True, padx=(10, 0), pady=5)
        scrollbar.pack(side=tk.RIGHT, fill='y', padx=(0, 10), pady=5)
        
        # Total de horas
        self.label_total = ttk.Label(self.janela, text="Total de horas: 0.00", font=('Arial', 12, 'bold'))
        self.label_total.pack(pady=5)
        
        # Botão de fechar
        btn_fechar = ttk.Button(self.janela, text="Fechar", command=self.janela.destroy)
        btn_fechar.pack(pady=5)
    
    def carregar_dados(self):
        resultados, total_horas = self.sistema.gerar_relatorio_completo(
            self.colaborador, self.cliente, self.data
        )
        
        for registro in resultados:
            self.tree.insert('', 'end', values=(
                registro['colaborador'],
                registro['cliente'],
                registro['tarefa'],  # Mostra a tarefa registrada
                registro['data'],
                registro['horas_inicio'],  # Mostra a hora de início
                registro['horas_fim'],     # Mostra a hora de fim
                f"{registro['horas_trabalhadas']:.2f}"
            ))
        
        self.label_total.config(text=f"Total de horas: {total_horas:.2f}")


class SistemaHorasTrabalhadasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Horas - Advocacia & Associados")
        self.root.geometry("800x600")
        
        self.sistema = SistemaHorasTrabalhadas()
        
        # Adicionar alguns registros de exemplo para teste
        self.adicionar_registros_exemplo()
        
        self.criar_interface()
    
    def adicionar_registros_exemplo(self):
        # Adicionar alguns registros de exemplo para demonstração
        exemplos = [
            ("Yago", "Rian", "Consulta jurídica sobre contrato de prestação de serviços", "2024-01-15", "09:00", "11:30"),
            ("Yago", "Rian", "Elaboração de contrato comercial com cláusulas específicas", "2024-01-15", "14:00", "17:30"),
            ("Yago", "Cliente A", "Reunião para discutir estratégia legal do caso", "2024-01-16", "10:00", "12:00"),
            ("Maria Santos", "Rian", "Atendimento ao cliente para esclarecimentos jurídicos", "2024-01-17", "08:30", "10:00"),
            ("João Silva", "Rian", "Pesquisa legal sobre jurisprudência do caso", "2024-01-18", "13:00", "15:30")
        ]
        
        for colaborador, cliente, tarefa, data, inicio, fim in exemplos:
            self.sistema.registrar_horas(colaborador, cliente, tarefa, data, inicio, fim)
        
    def criar_interface(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.frame_registro = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_registro, text='Registrar Horas')
        
        self.frame_relatorios = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_relatorios, text='Relatórios')
        
        self.criar_aba_registro()
        self.criar_aba_relatorios()
    
    def criar_aba_registro(self):
        labels = ['Colaborador:', 'Cliente:', 'Tarefa:', 'Data (YYYY-MM-DD):', 'Hora Início (HH:MM):', 'Hora Fim (HH:MM):']
        entries = []
        
        for i, label_text in enumerate(labels):
            label = ttk.Label(self.frame_registro, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
            
            entry = ttk.Entry(self.frame_registro, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
            entries.append(entry)
        
        self.entry_colaborador, self.entry_cliente, self.entry_tarefa, \
        self.entry_data, self.entry_inicio, self.entry_fim = entries
        
        # Preencher com dados de exemplo
        self.entry_colaborador.insert(0, "Yago")
        self.entry_cliente.insert(0, "Rian")
        self.entry_data.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_tarefa.insert(0, "Revisão de documento legal")
        self.entry_inicio.insert(0, "09:00")
        self.entry_fim.insert(0, "12:00")
        
        btn_registrar = ttk.Button(self.frame_registro, text="Registrar Horas", command=self.registrar_horas)
        btn_registrar.grid(row=6, column=0, columnspan=2, pady=10)
    
    def criar_aba_relatorios(self):
        frame_filtros = ttk.LabelFrame(self.frame_relatorios, text="Filtros")
        frame_filtros.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame_filtros, text="Colaborador:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_filtro_colab = ttk.Entry(frame_filtros, width=20)
        self.entry_filtro_colab.grid(row=0, column=1, padx=5, pady=5)
        self.entry_filtro_colab.insert(0, "Yago")
        
        ttk.Label(frame_filtros, text="Cliente:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_filtro_cliente = ttk.Entry(frame_filtros, width=20)
        self.entry_filtro_cliente.grid(row=0, column=3, padx=5, pady=5)
        self.entry_filtro_cliente.insert(0, "Rian")
        
        ttk.Label(frame_filtros, text="Data (opcional):").grid(row=0, column=4, padx=5, pady=5)
        self.entry_filtro_data = ttk.Entry(frame_filtros, width=15)
        self.entry_filtro_data.grid(row=0, column=5, padx=5, pady=5)
        
        btn_gerar = ttk.Button(frame_filtros, text="Gerar Relatório", command=self.gerar_relatorio)
        btn_gerar.grid(row=0, column=6, padx=10, pady=5)
        
        btn_limpar = ttk.Button(frame_filtros, text="Limpar", command=self.limpar_filtros)
        btn_limpar.grid(row=0, column=7, padx=5, pady=5)
    
    def mostrar_janela_cadastro(self, tipo, nome_atual):
        JanelaCadastro(
            self.root, 
            f"Cadastrar Novo {tipo.capitalize()}", 
            tipo, 
            self.sistema,
            lambda novo_nome: self.atualizar_campo(tipo, nome_atual, novo_nome)
        )
    
    def atualizar_campo(self, tipo, nome_antigo, novo_nome):
        if tipo == 'colaborador':
            self.entry_colaborador.delete(0, tk.END)
            self.entry_colaborador.insert(0, novo_nome)
        else:
            self.entry_cliente.delete(0, tk.END)
            self.entry_cliente.insert(0, novo_nome)
    
    def limpar_filtros(self):
        self.entry_filtro_colab.delete(0, tk.END)
        self.entry_filtro_cliente.delete(0, tk.END)
        self.entry_filtro_data.delete(0, tk.END)
    
    def registrar_horas(self):
        try:
            colaborador = self.entry_colaborador.get().strip()
            cliente = self.entry_cliente.get().strip()
            tarefa = self.entry_tarefa.get().strip()
            inicio = self.entry_inicio.get().strip()
            fim = self.entry_fim.get().strip()
            
            # Verificar se colaborador existe
            if not self.sistema.verificar_colaborador_valido(colaborador):
                resposta = messagebox.askyesno(
                    "Colaborador não encontrado", 
                    f"O colaborador '{colaborador}' não está cadastrado.\nDeseja cadastrar agora?"
                )
                if resposta:
                    self.mostrar_janela_cadastro('colaborador', colaborador)
                return
            
            # Verificar se cliente existe
            if not self.sistema.verificar_cliente_valido(cliente):
                resposta = messagebox.askyesno(
                    "Cliente não encontrado", 
                    f"O cliente '{cliente}' não está cadastrado.\nDeseja cadastrar agora?"
                )
                if resposta:
                    self.mostrar_janela_cadastro('cliente', cliente)
                return
            
            # Se ambos existem, prosseguir com o registro
            dados = {
                'colaborador': colaborador,
                'cliente': cliente,
                'tarefa': tarefa,
                'data': self.entry_data.get(),
                'inicio': inicio,
                'fim': fim
            }
            
            for campo, valor in dados.items():
                if not valor:
                    messagebox.showerror("Erro", f"Campo {campo} não pode estar vazio!")
                    return
            
            registro = self.sistema.registrar_horas(
                dados['colaborador'], dados['cliente'], dados['tarefa'],
                dados['data'], dados['inicio'], dados['fim']
            )
            
            messagebox.showinfo("Sucesso", f"Horas registradas com sucesso!\nTotal: {registro['horas_trabalhadas']:.2f} horas")
            
            # Limpar apenas alguns campos, mantendo colaborador, cliente e data
            self.entry_tarefa.delete(0, tk.END)
            self.entry_inicio.delete(0, tk.END)
            self.entry_fim.delete(0, tk.END)
            
            # Preencher com valores padrão para próximo registro
            self.entry_tarefa.insert(0, "Nova tarefa")
            self.entry_inicio.insert(0, "09:00")
            self.entry_fim.insert(0, "12:00")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar horas: {str(e)}")
    
    def gerar_relatorio(self):
        try:
            colaborador = self.entry_filtro_colab.get().strip() or None
            cliente = self.entry_filtro_cliente.get().strip() or None
            data = self.entry_filtro_data.get().strip() or None
            
            # Verificar se os filtros são válidos
            if colaborador and not self.sistema.verificar_colaborador_valido(colaborador):
                messagebox.showwarning("Aviso", f"Colaborador '{colaborador}' não encontrado.")
                return
            
            if cliente and not self.sistema.verificar_cliente_valido(cliente):
                messagebox.showwarning("Aviso", f"Cliente '{cliente}' não encontrado.")
                return
            
            # Abrir janela de relatório
            JanelaRelatorio(self.root, self.sistema, colaborador, cliente, data)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar relatório: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaHorasTrabalhadasGUI(root)
    root.mainloop()