from dataclasses import dataclass
from classes.Company import Company

@dataclass
class ReceitaWS_resp:
    company: Company
    status: int

@dataclass
class ReceitaWS_errorResp:
    status: str
    message: str