from fastapi import Depends
from sqlalchemy.orm import Session

from ..db.sql import get_db
from .{{cookiecutter.table_name}} import {{ cookiecutter.table_name|capitalize }}Service


def get_{{cookiecutter.table_name}}_service(db: Session = Depends(get_db)) -> {{ cookiecutter.table_name|capitalize }}Service:
    return {{ cookiecutter.table_name|capitalize }}Service(db)