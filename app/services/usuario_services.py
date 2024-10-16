from models.usuario import Usuario
from repositories.usuario_repositories import UsuarioRepository 

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome:str, email:str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha= senha)
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")

        except TypeError as error:
            print(f"Erro ao salvar o arquivo {error}")
        except Exception as error:
            print(f"Ocorreu um erro{error}.")

    def listar_todos_usuarios(self):
     return self.repository.listar_todos_usuarios()
