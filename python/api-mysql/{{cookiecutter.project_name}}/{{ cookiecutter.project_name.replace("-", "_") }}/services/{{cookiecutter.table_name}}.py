from sqlalchemy.orm import Session

from ..db.sql import get_db
from ..model.{{cookiecutter.table_name}} import {{ cookiecutter.table_name|capitalize }}


class {{ cookiecutter.table_name|capitalize }}Service:
    def __init__(self, db: Session):
        self.db = db

    def create_{{cookiecutter.table_name}}(self, name: str) -> {{ cookiecutter.table_name|capitalize }}:
        {{cookiecutter.table_name}} = {{ cookiecutter.table_name|capitalize }}(name=name)
        self.db.add({{cookiecutter.table_name}})
        self.db.commit()
        self.db.refresh({{cookiecutter.table_name}})
        return {{cookiecutter.table_name}}

    def get_{{cookiecutter.table_name}}(self, {{cookiecutter.table_name}}_id: int) -> {{ cookiecutter.table_name|capitalize }}:
        return self.db.query({{ cookiecutter.table_name|capitalize }}).filter({{ cookiecutter.table_name|capitalize }}.id == {{cookiecutter.table_name}}_id).first()

    def get_all_{{cookiecutter.table_name}}s(self) -> list:
        return self.db.query({{ cookiecutter.table_name|capitalize }}).all()

    def update_{{cookiecutter.table_name}}(self, {{cookiecutter.table_name}}_id: int, name: str = None) -> {{ cookiecutter.table_name|capitalize }}:
        {{cookiecutter.table_name}} = self.db.query({{ cookiecutter.table_name|capitalize }}).filter({{ cookiecutter.table_name|capitalize }}.id == {{cookiecutter.table_name}}_id).first()
        if {{cookiecutter.table_name}}:
            if name:
                {{cookiecutter.table_name}}.name = name
            self.db.commit()
            self.db.refresh({{cookiecutter.table_name}})
        return {{cookiecutter.table_name}}

    def delete_{{cookiecutter.table_name}}(self, {{cookiecutter.table_name}}_id: int) -> None:
        {{cookiecutter.table_name}} = self.db.query({{ cookiecutter.table_name|capitalize }}).filter({{ cookiecutter.table_name|capitalize }}.id == {{cookiecutter.table_name}}_id).first()
        if {{cookiecutter.table_name}}:
            self.db.delete({{cookiecutter.table_name}})
            self.db.commit()
