from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..services.service_provider import get_{{cookiecutter.table_name}}_service
from ..services.{{cookiecutter.table_name}} import {{ cookiecutter.table_name|capitalize }}Service
from .model.{{cookiecutter.table_name}} import {{ cookiecutter.table_name|capitalize }}, {{ cookiecutter.table_name|capitalize }}Create

router = APIRouter(prefix="/{{cookiecutter.table_name}}s")

@router.post("", response_model={{ cookiecutter.table_name|capitalize }})
def create_{{cookiecutter.table_name}}({{cookiecutter.table_name}}: {{ cookiecutter.table_name|capitalize }}Create, service: {{ cookiecutter.table_name|capitalize }}Service = Depends(get_{{cookiecutter.table_name}}_service)):
    db_{{cookiecutter.table_name}} = service.create_{{cookiecutter.table_name}}(name={{cookiecutter.table_name}}.name)
    return db_{{cookiecutter.table_name}}

@router.get("/{ {{cookiecutter.table_name}}_id}", response_model={{ cookiecutter.table_name|capitalize }})
def get_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id: int, service: {{ cookiecutter.table_name|capitalize }}Service = Depends(get_{{cookiecutter.table_name}}_service)):
    db_{{cookiecutter.table_name}} = service.get_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id={{cookiecutter.table_name}}_id)
    if db_{{cookiecutter.table_name}} is None:
        raise HTTPException(status_code=404, detail="{{ cookiecutter.table_name|capitalize }} not found")
    return db_{{cookiecutter.table_name}}

@router.get("", response_model=list[{{ cookiecutter.table_name|capitalize }}])
def get_all_{{cookiecutter.table_name}}s(service: {{ cookiecutter.table_name|capitalize }}Service = Depends(get_{{cookiecutter.table_name}}_service)):
    return service.get_all_{{cookiecutter.table_name}}s()

@router.put("/{ {{cookiecutter.table_name}}_id}", response_model={{ cookiecutter.table_name|capitalize }})
def update_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id: int, {{cookiecutter.table_name}}: {{ cookiecutter.table_name|capitalize }}Create, service: {{ cookiecutter.table_name|capitalize }}Service = Depends(get_{{cookiecutter.table_name}}_service)):
    db_{{cookiecutter.table_name}} = service.update_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id={{cookiecutter.table_name}}_id, name={{cookiecutter.table_name}}.name)
    if db_{{cookiecutter.table_name}} is None:
        raise HTTPException(status_code=404, detail="{{ cookiecutter.table_name|capitalize }} not found")
    return db_{{cookiecutter.table_name}}

@router.delete("/{ {{cookiecutter.table_name}}_id}")
def delete_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id: int, service: {{ cookiecutter.table_name|capitalize }}Service = Depends(get_{{cookiecutter.table_name}}_service)):
    service.delete_{{cookiecutter.table_name}}({{cookiecutter.table_name}}_id={{cookiecutter.table_name}}_id)
    return {"detail": "{{ cookiecutter.table_name|capitalize }} deleted"}
