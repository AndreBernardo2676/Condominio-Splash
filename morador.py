import mysql.connector

class Morador:
    def __init__(self, nome, bloco, apartamento, telefone, veiculo, placa):
        self.nome = nome
        self.bloco = bloco
        self.apartamento = apartamento
        self.telefone = telefone
        self.veiculo = veiculo
        self.placa = placa

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
        
        comando = "INSERT INTO tab_moradores (nome, bloco, apartamento, telefone, veiculo, placa) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.nome, self.bloco, self.apartamento, self.telefone, self.veiculo, self.placa)
        
        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
        print(f"Morador {self.nome} cadastrado com sucesso!")

    @staticmethod

    def listar_moradores():

        try:
            conexao = Morador.conectar_bd()
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM tab_moradores")
            resultado = cursor.fetchall()

            moradores = []
            for morador in resultado:
                novo_morador = Morador(
                    nome=morador[1],
                    bloco=morador[2],
                    apartamento=morador[3],
                    telefone=morador[4],
                    veiculo=morador[5],
                    placa=morador[6]
                )
                moradores.append(novo_morador)

            cursor.close()
            conexao.close()
            return moradores  
        except mysql.connector.Error as e:
            print(f"Erro ao listar moradores: {e}")
        return []

    
