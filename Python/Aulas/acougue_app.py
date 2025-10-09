import acougue_app as tk
from acougue_app import messagebox, simpledialog
import requests

# --- DADOS DO AÇOUGUE ---
acougue = {
    'Carne': ['Patinho', 'Picanha', 'Coxão Mole', 'Maminha', 'Fraldinha', 'Linguiça'],
    'Preço/kg': [35.9, 80.00, 24.78, 50.00, 49.85, 15],
    'Estoque': [10, 50, 30, 15, 20, 100],
    'Validade': ['4', '7', '5', '9', '20', '50']
}

carrinho = {
    'Endereço': {'Rua': '', 'Bairro': '', 'Nº': '', 'CEP': ''},
    'Itens': {},
    'Valor Total': 0
}

indices = {acougue['Carne'][i]: i for i in range(len(acougue['Carne']))}


# --- TKINTER APP ---
class AcougueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Açougueria Agnello 🍖")
        self.root.geometry("800x600")
        self.root.config(bg="#1C1C1C")  # grafite escuro

        self.tipo_usuario = None

        self.create_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Açougueria Agnello 🍖", font=("Helvetica", 26, "bold"),
                 fg="#D4AF37", bg="#1C1C1C").pack(pady=40)

        tk.Label(self.root, text="Você é:", font=("Helvetica", 16), fg="white", bg="#1C1C1C").pack(pady=10)

        tk.Button(self.root, text="Cliente", font=("Helvetica", 14), bg="#D4AF37", fg="black", width=15,
                  command=self.cliente_view).pack(pady=10)

        tk.Button(self.root, text="Funcionário", font=("Helvetica", 14), bg="#D4AF37", fg="black", width=15,
                  command=self.funcionario_view).pack(pady=10)

    def cliente_view(self):
        self.tipo_usuario = 'cliente'
        self.clear_screen()
        self.cadastro_endereco()
        self.menu_cliente()

    def funcionario_view(self):
        self.tipo_usuario = 'funcionario'
        self.menu_funcionario()

    # --- Cliente: Endereço + Carrinho ---
    def cadastro_endereco(self):
        cep = simpledialog.askstring("Endereço", "Digite seu CEP:")
        try:
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if resposta.status_code == 200:
                dados = resposta.json()
                carrinho['Endereço'] = dados
                carrinho['Endereço']['Nº'] = simpledialog.askstring("Endereço", "Digite o número da residência:")
                carrinho['Endereço']['Complemento'] = simpledialog.askstring("Endereço", "Complemento (opcional):")
            else:
                messagebox.showerror("Erro", "CEP inválido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao buscar CEP: {e}")

    def menu_cliente(self):
        self.clear_screen()
        tk.Label(self.root, text="Escolha seu produto", font=("Helvetica", 20), fg="#D4AF37", bg="#1C1C1C").pack(pady=10)

        for carne in acougue['Carne']:
            i = indices[carne]
            texto = f"{carne} - R$ {acougue['Preço/kg'][i]:.2f} - Estoque: {acougue['Estoque'][i]}kg"
            tk.Button(self.root, text=texto, font=("Helvetica", 12), width=50,
                      command=lambda c=carne: self.adicionar_ao_carrinho(c)).pack(pady=5)

        tk.Button(self.root, text="Ver Carrinho", font=("Helvetica", 14, "bold"), bg="#8B0000", fg="white",
                  command=self.mostrar_carrinho).pack(pady=20)

    def adicionar_ao_carrinho(self, item):
        i = indices[item]
        qtd = simpledialog.askinteger("Quantidade", f"Quantos kg de {item} você deseja?")
        if qtd is None:
            return
        if qtd > acougue['Estoque'][i]:
            messagebox.showwarning("Estoque insuficiente", f"Apenas {acougue['Estoque'][i]}kg disponíveis.")
            return
        acougue['Estoque'][i] -= qtd
        carrinho['Valor Total'] += qtd * acougue['Preço/kg'][i]
        carrinho['Itens'][item] = carrinho['Itens'].get(item, 0) + qtd
        messagebox.showinfo("Adicionado", f"{qtd}kg de {item} adicionados ao carrinho.")

    def mostrar_carrinho(self):
        self.clear_screen()
        tk.Label(self.root, text="Seu Carrinho", font=("Helvetica", 20), fg="#D4AF37", bg="#1C1C1C").pack(pady=10)

        for item, qtd in carrinho['Itens'].items():
            preco_total = qtd * acougue['Preço/kg'][indices[item]]
            tk.Label(self.root, text=f"{item}: {qtd}kg - R$ {preco_total:.2f}",
                     font=("Helvetica", 14), bg="#1C1C1C", fg="white").pack()

        tk.Label(self.root, text=f"Total: R$ {carrinho['Valor Total']:.2f}", font=("Helvetica", 16, "bold"),
                 fg="#D4AF37", bg="#1C1C1C").pack(pady=10)

        tk.Button(self.root, text="Finalizar Compra", bg="#D4AF37", fg="black", font=("Helvetica", 12),
                  command=self.finalizar_compra).pack(pady=10)
        tk.Button(self.root, text="Voltar", bg="#2F4F4F", fg="white", command=self.menu_cliente).pack(pady=10)

    def finalizar_compra(self):
        endereco = carrinho['Endereço']
        resumo = f"Compra realizada para {endereco.get('logradouro', '')}, Nº {endereco.get('Nº', '')}, {endereco.get('bairro', '')}.\n\n"
        resumo += f"Total: R$ {carrinho['Valor Total']:.2f}\nObrigado pela preferência!"
        messagebox.showinfo("Compra Confirmada", resumo)
        self.root.destroy()

    # --- FUNCIONÁRIO ---
    def menu_funcionario(self):
        self.clear_screen()
        tk.Label(self.root, text="Painel do Funcionário", font=("Helvetica", 20), fg="#D4AF37", bg="#1C1C1C").pack(pady=20)

        tk.Button(self.root, text="Cadastrar Produto", bg="#D4AF37", fg="black", command=self.cadastrar_produto).pack(pady=10)
        tk.Button(self.root, text="Remover Produto", bg="#D4AF37", fg="black", command=self.remover_produto).pack(pady=10)
        tk.Button(self.root, text="Atualizar Produto", bg="#D4AF37", fg="black", command=self.atualizar_produto).pack(pady=10)
        tk.Button(self.root, text="Voltar", bg="#2F4F4F", fg="white", command=self.create_start_screen).pack(pady=20)

    def cadastrar_produto(self):
        nome = simpledialog.askstring("Produto", "Nome da carne:")
        preco = simpledialog.askfloat("Preço", f"Preço por kg de {nome}:")
        estoque = simpledialog.askinteger("Estoque", f"Quantidade em kg de {nome} no estoque:")
        validade = simpledialog.askstring("Validade", f"Validade em dias de {nome}:")

        if None in (nome, preco, estoque, validade):
            messagebox.showwarning("Cancelado", "Cadastro incompleto ou cancelado.")
            return

        acougue['Carne'].append(nome)
        acougue['Preço/kg'].append(preco)
        acougue['Estoque'].append(estoque)
        acougue['Validade'].append(validade)
        indices[nome] = len(acougue['Carne']) - 1

        messagebox.showinfo("Sucesso", f"{nome} cadastrado com sucesso!")
    def remover_produto(self):
        if not acougue['Carne']:
            messagebox.showinfo("Vazio", "Nenhum produto cadastrado.")
            return

        item = simpledialog.askstring("Remover", "Qual carne deseja remover?\n" + "\n".join(acougue['Carne']))
        if item not in acougue['Carne']:
            messagebox.showerror("Erro", "Carne não encontrada.")
            return

        i = indices[item]
        for key in acougue.keys():
            acougue[key].pop(i)
        indices.clear()
        for idx, carne in enumerate(acougue['Carne']):
            indices[carne] = idx

        messagebox.showinfo("Removido", f"{item} foi removido com sucesso.")
    def atualizar_produto(self):
        item = simpledialog.askstring("Atualizar", "Qual carne deseja atualizar?\n" + "\n".join(acougue['Carne']))
        if item not in acougue['Carne']:
            messagebox.showerror("Erro", "Carne não encontrada.")
            return

        i = indices[item]
        preco = simpledialog.askfloat("Novo preço", f"Preço atual: R${acougue['Preço/kg'][i]:.2f}")
        estoque = simpledialog.askinteger("Novo estoque", f"Estoque atual: {acougue['Estoque'][i]} kg")
        validade = simpledialog.askstring("Nova validade", f"Validade atual: {acougue['Validade'][i]} dias")

        if preco is not None:
            acougue['Preço/kg'][i] = preco
        if estoque is not None:
            acougue['Estoque'][i] = estoque
        if validade is not None:
            acougue['Validade'][i] = validade

        messagebox.showinfo("Atualizado", f"{item} atualizado com sucesso.")
