from sqlalchemy.orm import Session

from ..db.sql import get_db
from ..model.{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }}


class {{ cookiecutter.entity_name|capitalize }}Service:
    def __init__(self, db: Session):
        self.db = db

    def create_{{cookiecutter.entity_name}}(self, name: str) -> {{ cookiecutter.entity_name|capitalize }}:
        {{cookiecutter.entity_name}} = {{ cookiecutter.entity_name|capitalize }}(name=name)
        self.db.add({{cookiecutter.entity_name}})
        self.db.commit()
        self.db.refresh({{cookiecutter.entity_name}})
        return {{cookiecutter.entity_name}}

    def get_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: int) -> {{ cookiecutter.entity_name|capitalize }}:
        return self.db.query({{ cookiecutter.entity_name|capitalize }}).filter({{ cookiecutter.entity_name|capitalize }}.id == {{cookiecutter.entity_name}}_id).first()

    def get_all_{{cookiecutter.entity_name}}s(self) -> list:
        return self.db.query({{ cookiecutter.entity_name|capitalize }}).all()

    def update_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: int, name: str = None) -> {{ cookiecutter.entity_name|capitalize }}:
        {{cookiecutter.entity_name}} = self.db.query({{ cookiecutter.entity_name|capitalize }}).filter({{ cookiecutter.entity_name|capitalize }}.id == {{cookiecutter.entity_name}}_id).first()
        if {{cookiecutter.entity_name}}:
            if name:
                {{cookiecutter.entity_name}}.name = name
            self.db.commit()
            self.db.refresh({{cookiecutter.entity_name}})
        return {{cookiecutter.entity_name}}

    def delete_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: int) -> None:
        {{cookiecutter.entity_name}} = self.db.query({{ cookiecutter.entity_name|capitalize }}).filter({{ cookiecutter.entity_name|capitalize }}.id == {{cookiecutter.entity_name}}_id).first()
        if {{cookiecutter.entity_name}}:
            self.db.delete({{cookiecutter.entity_name}})
            self.db.commit()
