from datetime import datetime
from tkinter import *
from tkinter import ttk
from morador import Morador
from colaborador import Colaborador
from visitantes import Visitante
from PIL import Image, ImageTk
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class Interface:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Splash Residence Club")
        self.janela.geometry("800x600")


        
        # ícone da janela
        try:
            self.janela.iconbitmap(r".\image\logo.ico")
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

        try:
            logo_img = Image.open(r".\image\logo.png")
            logo_img = logo_img.resize((80, 80), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")
            self.logo = None

        header_frame = Frame(self.janela, bg="white")
        header_frame.pack(fill=X, side=TOP, pady=10)

        if self.logo:
            label_logo = Label(header_frame, image=self.logo)
            label_logo.pack(side=LEFT, padx=10)

        label_titulo = Label(
            header_frame,
            text="Sistema de Condomínio",
            font=("Arial", 20, "bold"),
           
        )
        label_titulo.pack(side=LEFT, padx=10)

        self.criar_gui()

        self.janela.mainloop()


    def criar_gui(self):
        notebook = ttk.Notebook(self.janela)
        notebook.pack(fill="both", expand=True)
        self.criar_moradores_tab(notebook)
        self.criar_colaboradores_tab(notebook)
        self.criar_visitantes_tab(notebook)

    def gerar_relatorio_pdf(self, dados, titulo, nome_arquivo):

        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        width, height = A4
        y = height - inch 

        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, y, titulo)
        y -= 0.5 * inch

        c.setFont("Helvetica", 12)
        y -= 0.3 * inch

        c.setFont("Helvetica", 10)
        for item in dados:
            linha = str(item)
            c.drawString(inch, y, linha)
            y -= 0.2 * inch
            if y < inch:  # Se chegou ao fim da página, criar nova página
                c.showPage()
                y = height - inch
                c.setFont("Helvetica", 10)

        c.save()
        print(f"Relatório gerado: {nome_arquivo}")

    def imprimir_relatorio_moradores(self):
        moradores = Morador.listar_moradores()
        if not moradores:
            self.texto_listar_moradores.config(text="Nenhum morador cadastrado!")
            return
        dados = [f"Nome: {m.nome}, Bloco: {m.bloco}, Apt: {m.apartamento}, Telefone: {m.telefone}, Veículo: {m.veiculo}, Placa: {m.placa}" for m in moradores]
        self.gerar_relatorio_pdf(dados, "Relatório de Moradores", "relatorio_moradores.pdf")
        self.texto_listar_moradores.config(text="Relatório gerado: relatorio_moradores.pdf")

    def imprimir_relatorio_colaboradores(self):
        colaboradores = Colaborador.listar_colaboradores()
        if not colaboradores:
            self.texto_cad_colaborador.config(text="Nenhum colaborador cadastrado!")
            return
        dados = [f"Nome: {c.nome}, Registro: {c.registro}, Cargo: {c.cargo}, CPF: {c.cpf}, Admissão: {c.admissao}, Demissão: {c.demissao}, Telefone: {c.telefone}, Email: {c.email}" for c in colaboradores]
        self.gerar_relatorio_pdf(dados, "Relatório de Colaboradores", "relatorio_colaboradores.pdf")
        self.texto_cad_colaborador.config(text="Relatório gerado: relatorio_colaboradores.pdf")

    def imprimir_relatorio_visitantes(self):
        visitantes = Visitante.listar_visitantes()
        if not visitantes:
            self.texto_cad_visitantes.config(text="Nenhum visitante cadastrado!")
            return
        dados = [f"Nome: {v.nome}, Documento: {v.documento}, Telefone: {v.telefone}, Morador: {v.morador_visitado}, Bloco: {v.bloco}, Apt: {v.apartamento}, Veículo: {v.veiculo}, Placa: {v.placa}, Entrada: {v.entrada}, Saída: {v.saida}" for v in visitantes]
        self.gerar_relatorio_pdf(dados, "Relatório de Visitantes", "relatorio_visitantes.pdf")
        self.texto_cad_visitantes.config(text="Relatório gerado: relatorio_visitantes.pdf")

    def criar_moradores_tab(self, notebook):
        moradores_tab = ttk.Frame(notebook)
        notebook.add(moradores_tab, text='Moradores')

        Label(moradores_tab, text="Nome", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=1, padx=10, pady=5, sticky=E)
        self.entrada_nome_morador = Entry(moradores_tab)
        self.entrada_nome_morador.grid(column=1, row=1, padx=10, pady=5)

        Label(moradores_tab, text="Bloco", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=2, padx=10, pady=5, sticky=E)
        self.entrada_bloco_morador = Entry(moradores_tab)
        self.entrada_bloco_morador.grid(column=1, row=2, padx=10, pady=5)

        Label(moradores_tab, text="Apartamento:", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=3, padx=10, pady=5, sticky=E)
        self.entrada_apartamento_morador = Entry(moradores_tab)
        self.entrada_apartamento_morador.grid(column=1, row=3, padx=10, pady=5)

        Label(moradores_tab, text="Telefone:", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=4, padx=10, pady=5, sticky=E)
        self.entrada_telefone_morador = Entry(moradores_tab)
        self.entrada_telefone_morador.grid(column=1, row=4, padx=10, pady=5)

        Label(moradores_tab, text="Veículo:", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=5, padx=10, pady=5, sticky=E)
        self.entrada_veiculo_morador = Entry(moradores_tab)
        self.entrada_veiculo_morador.grid(column=1, row=5, padx=10, pady=5)

        Label(moradores_tab, text="Placa:", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=6, padx=10, pady=5, sticky=E)
        self.entrada_placa_morador = Entry(moradores_tab)
        self.entrada_placa_morador.grid(column=1, row=6, padx=10, pady=5)

        botao_cadastrar = Button(moradores_tab, text='Cadastrar Morador', font=("Arial", 10, "normal"), command=self.cadastrar_morador)
        botao_cadastrar.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

        self.texto_cadastro_moradores = Label(moradores_tab, text='', bg="white", font=("Arial", 12, "normal"))
        self.texto_cadastro_moradores.grid(column=0, row=8, columnspan=2, padx=10, pady=10)

        botao_imprimir_relatorio = Button(moradores_tab, text='Imprimir Relatório', font=("Arial", 10, "normal"), command=self.imprimir_relatorio_moradores)
        botao_imprimir_relatorio.grid(column=0, row=12, columnspan=2, padx=10, pady=10)

        self.texto_listar_moradores = Label(moradores_tab, text='', justify=RIGHT, bg="white")
        self.texto_listar_moradores.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

    def listar_morador(self):
        moradores = Morador.listar_moradores()
        texto = "\n".join([f"{m.nome}, Bloco {m.bloco}, Apt {m.apartamento}" for m in moradores])
        self.texto_listar_moradores.config(text=texto)

    def cadastrar_morador(self):
        nome = self.entrada_nome_morador.get()
        bloco = self.entrada_bloco_morador.get()
        apartamento = self.entrada_apartamento_morador.get()
        telefone = self.entrada_telefone_morador.get()
        veiculo = self.entrada_veiculo_morador.get()
        placa = self.entrada_placa_morador.get()

        novo_morador = Morador(nome, bloco, apartamento, telefone, veiculo, placa)
        novo_morador.salvar_no_bd()
        
        self.texto_cadastro_moradores.config(text=f"Morador {nome} cadastrado com sucesso!")

    def criar_colaboradores_tab(self, notebook):
        colaboradores_tab = ttk.Frame(notebook)
        notebook.add(colaboradores_tab, text='Colaboradores')

        Label(colaboradores_tab, text="Nome", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=1, padx=10, pady=5, sticky=E)
        self.entrada_nome_colaborador = Entry(colaboradores_tab)
        self.entrada_nome_colaborador.grid(column=1, row=1, padx=10, pady=5)

        Label(colaboradores_tab, text="Registro", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=2, padx=10, pady=5, sticky=E)
        self.entrada_registro_colaborador = Entry(colaboradores_tab)
        self.entrada_registro_colaborador.grid(column=1, row=2, padx=10, pady=5)

        Label(colaboradores_tab, text="Cargo", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=3, padx=10, pady=5, sticky=E)
        self.entrada_cargo_colaborador = Entry(colaboradores_tab)
        self.entrada_cargo_colaborador.grid(column=1, row=3, padx=10, pady=5)

        Label(colaboradores_tab, text="CPF", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=4, padx=10, pady=5, sticky=E)
        self.entrada_cpf_colaborador = Entry(colaboradores_tab)
        self.entrada_cpf_colaborador.grid(column=1, row=4, padx=10, pady=5)

        Label(colaboradores_tab, text="Admissao", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=5, padx=10, pady=5, sticky=E)
        self.entrada_admissao_colaborador = Entry(colaboradores_tab)
        self.entrada_admissao_colaborador.grid(column=1, row=5, padx=10, pady=5)

        Label(colaboradores_tab, text="Demissao", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=6, padx=10, pady=5, sticky=E)
        self.entrada_demissao_colaborador = Entry(colaboradores_tab)
        self.entrada_demissao_colaborador.grid(column=1, row=6, padx=10, pady=5)

        Label(colaboradores_tab, text="Telefone", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=7, padx=10, pady=5, sticky=E)
        self.entrada_telefone_colaborador = Entry(colaboradores_tab)
        self.entrada_telefone_colaborador.grid(column=1, row=7, padx=10, pady=5)

        Label(colaboradores_tab, text="Email", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=8, padx=10, pady=5, sticky=E)
        self.entrada_email_colaborador = Entry(colaboradores_tab)
        self.entrada_email_colaborador.grid(column=1, row=8, padx=10, pady=5)

        botao_cadastrar = Button(colaboradores_tab, text='Cadastrar Colaborador', font=("Arial", 10, "normal"), command=self.cadastrar_colaborador)
        botao_cadastrar.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

        self.texto_cad_colaborador = Label(colaboradores_tab, text='', bg="white", font=("Arial", 12, "normal"))
        self.texto_cad_colaborador.grid(column=0, row=10, columnspan=2, padx=10, pady=10)

        botao_imprimir_relatorio = Button(colaboradores_tab, text='Imprimir Relatório', font=("Arial", 10, "normal"), command=self.imprimir_relatorio_colaboradores)
        botao_imprimir_relatorio.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

    def cadastrar_colaborador(self):
        nome = self.entrada_nome_colaborador.get()
        registro = self.entrada_registro_colaborador.get()
        cargo = self.entrada_cargo_colaborador.get()
        cpf = self.entrada_cpf_colaborador.get()
        admissao = self.entrada_admissao_colaborador.get()
        demissao = self.entrada_demissao_colaborador.get()
        telefone = self.entrada_telefone_colaborador.get()
        email = self.entrada_email_colaborador.get()

        try:
            if admissao:
                admissao = datetime.strptime(admissao, "%d/%m/%Y").strftime("%Y-%m-%d")
            else:
                admissao = None
        except ValueError:
            self.texto_cad_colaborador.config(text="Erro: Data de admissão inválida! Use o formato DD/MM/YYYY.")
            return

        try:
            if demissao:
                demissao = datetime.strptime(demissao, "%d/%m/%Y").strftime("%Y-%m-%d")
            else:
                demissao = None
        except ValueError:
            self.texto_cad_colaborador.config(text="Erro: Data de demissão inválida! Use o formato DD/MM/YYYY.")
            return

        novo_colaborador = Colaborador(nome, registro, cargo, cpf, admissao, demissao, telefone, email)
        novo_colaborador.salvar_no_bd()
        self.texto_cad_colaborador.config(text=f"Colaborador {nome} cadastrado com sucesso!")

    def criar_visitantes_tab(self, notebook):
        visitantes_tab = ttk.Frame(notebook)
        notebook.add(visitantes_tab, text='Visitantes')

        Label(visitantes_tab, text="Nome", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=1, padx=10, pady=5, sticky=E)
        self.entrada_nome_visitante = Entry(visitantes_tab)
        self.entrada_nome_visitante.grid(column=1, row=1, padx=10, pady=5)

        Label(visitantes_tab, text="Documento", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=2, padx=10, pady=5, sticky=E)
        self.entrada_documento_visitante = Entry(visitantes_tab)
        self.entrada_documento_visitante.grid(column=1, row=2, padx=10, pady=5)

        Label(visitantes_tab, text="Telefone", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=3, padx=10, pady=5, sticky=E)
        self.entrada_telefone_visitante = Entry(visitantes_tab)
        self.entrada_telefone_visitante.grid(column=1, row=3, padx=10, pady=5)

        Label(visitantes_tab, text="Morador", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=4, padx=10, pady=5, sticky=E)
        self.entrada_morador_visitado_visitante = Entry(visitantes_tab)
        self.entrada_morador_visitado_visitante.grid(column=1, row=4, padx=10, pady=5)

        Label(visitantes_tab, text="Bloco", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=5, padx=10, pady=5, sticky=E)
        self.entrada_bloco_visitante = Entry(visitantes_tab)
        self.entrada_bloco_visitante.grid(column=1, row=5, padx=10, pady=5)

        Label(visitantes_tab, text="Apartamento", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=6, padx=10, pady=5, sticky=E)
        self.entrada_apartamento_visitante = Entry(visitantes_tab)
        self.entrada_apartamento_visitante.grid(column=1, row=6, padx=10, pady=5)

        Label(visitantes_tab, text="Veiculo", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=7, padx=10, pady=5, sticky=E)
        self.entrada_veiculo_visitante = Entry(visitantes_tab)
        self.entrada_veiculo_visitante.grid(column=1, row=7, padx=10, pady=5)

        Label(visitantes_tab, text="Placa", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=8, padx=10, pady=5, sticky=E)
        self.entrada_placa_visitante = Entry(visitantes_tab)
        self.entrada_placa_visitante.grid(column=1, row=8, padx=10, pady=5)

        Label(visitantes_tab, text="Entrada", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=9, padx=10, pady=5, sticky=E)
        self.entrada_entrada_visitante = Entry(visitantes_tab)
        self.entrada_entrada_visitante.grid(column=1, row=9, padx=10, pady=5)

        Label(visitantes_tab, text="Saida", bg="white", font=("Arial", 12, "normal")).grid(column=0, row=10, padx=10, pady=5, sticky=E)
        self.entrada_saida_visitante = Entry(visitantes_tab)
        self.entrada_saida_visitante.grid(column=1, row=10, padx=10, pady=5)

        botao_cadastrar = Button(visitantes_tab, text='Cadastrar Visitante', font=("Arial", 10, "normal"), command=self.cadastrar_visitante)
        botao_cadastrar.grid(column=0, row=12, columnspan=2, padx=10, pady=10)

        self.texto_cad_visitantes = Label(visitantes_tab, text='', bg="white")
        self.texto_cad_visitantes.grid(column=0, row=13, columnspan=2, padx=10, pady=10)

        botao_imprimir_relatorio = Button(visitantes_tab, text='Imprimir Relatório', font=("Arial", 10, "normal"), command=self.imprimir_relatorio_visitantes)
        botao_imprimir_relatorio.grid(column=0, row=14, columnspan=2, padx=10, pady=10)

    def cadastrar_visitante(self):
        nome = self.entrada_nome_visitante.get()
        documento = self.entrada_documento_visitante.get()
        telefone = self.entrada_telefone_visitante.get()
        morador_visitado = self.entrada_morador_visitado_visitante.get()
        bloco = self.entrada_bloco_visitante.get()
        apartamento = self.entrada_apartamento_visitante.get()
        veiculo = self.entrada_veiculo_visitante.get()
        placa = self.entrada_placa_visitante.get()
        entrada = self.entrada_entrada_visitante.get()
        saida = self.entrada_saida_visitante.get()

        novo_visitante = Visitante(nome, documento, telefone, morador_visitado, bloco, apartamento, veiculo, placa, entrada, saida)
        novo_visitante.salvar_no_bd()

        self.texto_cad_visitantes.config(text=f"Visitante {nome} cadastrado com sucesso!")

if __name__ == "__main__":
    app = Interface()