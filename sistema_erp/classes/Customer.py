from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    phone: str
    city: str
    id_customer: int = None