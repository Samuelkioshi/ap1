from pydantic import BaseModel

class ProdutosSchema(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int

class UserSchema(BaseModel):
    id: int
    usuario: str
    password: str
