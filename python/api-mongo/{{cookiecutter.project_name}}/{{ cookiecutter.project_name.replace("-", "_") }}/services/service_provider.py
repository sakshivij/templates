from fastapi import Depends
from ..db.mongo import get_db
from .{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }}Service


def get_{{cookiecutter.entity_name}}_service(db: Session = Depends(get_db)) -> {{ cookiecutter.entity_name|capitalize }}Service:
    return {{ cookiecutter.entity_name|capitalize }}Service(db)