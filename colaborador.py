import mysql.connector

class Colaborador:
    def __init__(self, nome, registro, cargo, cpf, admissao, demissao, telefone, email):
        self.nome = nome
        self.registro = registro
        self.cargo = cargo
        self.cpf = cpf
        self.admissao = admissao
        self.demissao = demissao
        self.telefone = telefone
        self.email = email

    @staticmethod
    def conectar_bd():
        
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="condominio"
        )

    def salvar_no_bd(self):
        
        conexao = self.conectar_bd()
        cursor = conexao.cursor()

        comando = "INSERT INTO tab_colaboradores (nome, registro, cargo, cpf, admissao, demissao, telefone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (self.nome, self.registro, self.cargo, self.cpf, self.admissao, self.demissao, self.telefone, self.email)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
        print(f"Colaborador {self.nome} cadastrado com sucesso!")

    @staticmethod
    def listar_colaboradores():
        conexao = Colaborador.conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tab_colaboradores")
        resultado = cursor.fetchall()

        colaboradores = []
        for colaborador in resultado:
            novo_colaborador = Colaborador(
                nome=colaborador[1],
                registro=colaborador[2],
                cargo=colaborador[3],
                cpf=colaborador[4],
                admissao=colaborador[5],
                demissao=colaborador[6],
                telefone=colaborador[7],
                email=colaborador[8]
            )
            colaboradores.append(novo_colaborador)

        cursor.close()
        conexao.close()
        return colaboradores
