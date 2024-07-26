from sqlalchemy import Column, Integer, String

from .base import Base


class {{ cookiecutter.table_name|capitalize }}(Base):
    __tablename__ = "{{cookiecutter.table_name}}s"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)