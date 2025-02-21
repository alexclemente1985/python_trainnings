from dataclasses import dataclass

@dataclass
class DBResults:
    type: str
    msg: str = None