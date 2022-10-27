

from dataclasses import dataclass


@dataclass
class Todo:
    title:str
    completed:bool
    id:int=0
    userId:int=0


