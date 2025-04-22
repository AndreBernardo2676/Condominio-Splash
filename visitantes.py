import mysql.connector

class Visitante:
    def __init__(self, nome, documento, telefone, morador_visitado, bloco, apartamento, veiculo, placa, entrada, saida):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone
        self.morador_visitado = morador_visitado
        self.bloco = bloco
        self.apartamento = apartamento
        self.veiculo = veiculo
        self.placa = placa
        self.entrada = entrada
        self.saida = saida

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

        comando = "INSERT INTO tab_visitantes (nome, documento, telefone, morador_visitado, bloco, apartamento, veiculo, placa, entrada, saida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (self.nome, self.documento, self.telefone, self.morador_visitado, self.bloco, self.apartamento, self.veiculo, self.placa, self.entrada, self.saida)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
        print(f"Visitante {self.nome} cadastrado com sucesso!")

    @staticmethod
    def listar_visitantes():
        conexao = Visitante.conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tab_visitantes")
        resultado = cursor.fetchall()

        visitantes = []
        for visitante in resultado:
            novo_visitante = Visitante(
                nome=visitante[1],
                documento=visitante[2],
                telefone=visitante[3],
                morador_visitado=visitante[4],
                bloco=visitante[5],
                apartamento=visitante[6],
                veiculo=visitante[7],
                placa=visitante[8],
                entrada=visitante[9],
                saida=visitante[10]
            )
            visitantes.append(novo_visitante)

        cursor.close()
        conexao.close()
        return visitantes
