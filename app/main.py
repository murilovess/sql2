from services.usuario_services import usuarioService
from repositories.usuario_repositories import usuarioRepository
from config.connection import Session

def main():
    session = Session()
    reporitory = usuarioRepository(session)
    service = usuarioService(reporitory)

    service.criar_usuario("Luis", "Email@", "3334")

    print("\nListando todos os usuários.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
         print(f"{usuario.nome} - {usuario.email}")

if __name__ == "__name__":
     main()