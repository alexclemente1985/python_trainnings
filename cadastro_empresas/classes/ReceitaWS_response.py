from dataclasses import dataclass
from classes.Company import Company

@dataclass
class ReceitaWS_resp:
    company: Company
    status_ok: bool

@dataclass
class ReceitaWS_errorResp:
    message: str
    status_ok: bool