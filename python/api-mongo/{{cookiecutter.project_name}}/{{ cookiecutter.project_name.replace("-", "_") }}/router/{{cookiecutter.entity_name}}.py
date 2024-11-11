from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..services.service_provider import get_{{cookiecutter.entity_name}}_service
from ..services.{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }}Service
from .model.{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }}, {{ cookiecutter.entity_name|capitalize }}Create

router = APIRouter(prefix="/{{cookiecutter.entity_name}}s")

@router.post("", response_model={{ cookiecutter.entity_name|capitalize }})
def create_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}: {{ cookiecutter.entity_name|capitalize }}Create, service: {{ cookiecutter.entity_name|capitalize }}Service = Depends(get_{{cookiecutter.entity_name}}_service)):
    db_{{cookiecutter.entity_name}} = service.create_{{cookiecutter.entity_name}}(name={{cookiecutter.entity_name}}.name)
    return db_{{cookiecutter.entity_name}}

@router.get("/{ {{cookiecutter.entity_name}}_id}", response_model={{ cookiecutter.entity_name|capitalize }})
def get_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id: int, service: {{ cookiecutter.entity_name|capitalize }}Service = Depends(get_{{cookiecutter.entity_name}}_service)):
    db_{{cookiecutter.entity_name}} = service.get_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id={{cookiecutter.entity_name}}_id)
    if db_{{cookiecutter.entity_name}} is None:
        raise HTTPException(status_code=404, detail="{{ cookiecutter.entity_name|capitalize }} not found")
    return db_{{cookiecutter.entity_name}}

@router.get("", response_model=list[{{ cookiecutter.entity_name|capitalize }}])
def get_all_{{cookiecutter.entity_name}}s(service: {{ cookiecutter.entity_name|capitalize }}Service = Depends(get_{{cookiecutter.entity_name}}_service)):
    return service.get_all_{{cookiecutter.entity_name}}s()

@router.put("/{ {{cookiecutter.entity_name}}_id}", response_model={{ cookiecutter.entity_name|capitalize }})
def update_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id: int, {{cookiecutter.entity_name}}: {{ cookiecutter.entity_name|capitalize }}Create, service: {{ cookiecutter.entity_name|capitalize }}Service = Depends(get_{{cookiecutter.entity_name}}_service)):
    db_{{cookiecutter.entity_name}} = service.update_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id={{cookiecutter.entity_name}}_id, name={{cookiecutter.entity_name}}.name)
    if db_{{cookiecutter.entity_name}} is None:
        raise HTTPException(status_code=404, detail="{{ cookiecutter.entity_name|capitalize }} not found")
    return db_{{cookiecutter.entity_name}}

@router.delete("/{ {{cookiecutter.entity_name}}_id}")
def delete_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id: int, service: {{ cookiecutter.entity_name|capitalize }}Service = Depends(get_{{cookiecutter.entity_name}}_service)):
    service.delete_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id={{cookiecutter.entity_name}}_id)
    return {"detail": "{{ cookiecutter.entity_name|capitalize }} deleted"}
