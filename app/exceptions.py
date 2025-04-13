class UserNotFoundError(Exception):
    """Exceção para quando um usuário não é encontrado."""
    def __init__(self, user_id: int):
        self.message = f"Usuário com ID {user_id} não foi encontrado."
        super().__init__(self.message)

class DatabaseError(Exception):
    """Exceção para erros relacionados ao banco de dados."""
    def __init__(self, detail: str):
        self.message = f"Erro no banco de dados: {detail}"
        super().__init__(self.message)
