from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Login:
    def __init__(self):
        self.loginw = Tk()
        self.loginw.title("Login")
        width, height = 500, 600
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="#D2B48C")

        self.username = StringVar()
        self.password = StringVar()

        self.criar_interface()
        self.loginw.mainloop()

    def __login_del__(self):
        """Confirma saída do sistema."""
        if messagebox.askyesno("SAIR", "Deseja realmente sair do sistema?"):
            self.loginw.destroy()
            exit(0)

    def criar_interface(self):
        """Cria os elementos gráficos do login."""
        self.loginframe = LabelFrame(self.loginw, bg="#D2B48C", height=400, width=300)
        self.loginframe.place(x=103, y=95)

        Label(self.loginframe, fg="white", bg="#D2B48C", anchor="center", text="Login", font="Roboto 40 bold").place(x=75, y=25)
        
        ttk.Entry(self.loginframe, width=20, textvariable=self.username, font="Roboto 14").place(x=35, y=145, height=40)
        ttk.Entry(self.loginframe, width=20, textvariable=self.password, font="Roboto 14", show="*").place(x=35, y=185, height=40)
        
        Button(self.loginframe, width=20, text="ENTRAR", bg="#008B8B", fg="white", bd="0", font="Roboto 14", command=self.verificar_login).place(x=35, y=290)

    @staticmethod
    def conectar_bd():
        """Cria e retorna a conexão com o banco de dados."""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="condominio"
            )
        except mysql.connector.Error as erro:
            messagebox.showerror("ERRO", f"Erro ao conectar ao banco: {erro}")
            return None

    def verificar_login(self):
        """Valida login e redireciona para a interface principal."""
        usuario = self.username.get()
        senha = self.password.get()

        conexao = self.conectar_bd()
        if conexao is None:
            return  # Não conseguiu conectar ao banco

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome=%s AND senha=%s", (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Bem-vindo!", f"Login realizado com sucesso, {usuario}!")
            self.loginw.destroy()
            from interface import Interface  # Importação dentro do método para evitar dependências circulares
            Interface()  # Inicializa a interface principal após login bem-sucedido
        else:
            messagebox.showerror("ATENÇÃO", "Usuário ou senha incorretos!")

        cursor.close()
        conexao.close()

if __name__ == "__main__":
    Login()  # Começamos o programa diretamente pelo Login
