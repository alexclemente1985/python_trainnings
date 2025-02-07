from dataclasses import dataclass

@dataclass
class DbResults:
    type: str
    msg: str = None