from dataclasses import dataclass

@dataclass
class Customer:
    id_customer: int
    name: str
    phone: str
    city: str
