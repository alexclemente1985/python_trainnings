from dataclasses import dataclass

@dataclass
class Company:
    cnpj: str
    nome: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    municipio: str
    uf: str
    cep: str
    telefone: str
    email: str


