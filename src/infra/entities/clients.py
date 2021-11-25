"""
Author: Thiago de Souza Santos
Create: 25/11/2021
Description: Especificationn entities 
"""

import enum
from sqlalchemy import Column, String, Integer, Enum
from src.infra.config import Base


class PersonType(enum.Enum):
    """ Defining people types """

    fisica = "Fisica"
    juridica = "Juridica"

class Clients(Base):
    """ Clients Entity """

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(PersonType), nullable=False)
    name = Column(String, nullable=False, unique=True)

    def __rep__(self):
        return f"Clients [name={self.name}]"
