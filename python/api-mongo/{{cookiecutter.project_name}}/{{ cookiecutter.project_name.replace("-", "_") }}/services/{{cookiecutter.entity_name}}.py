from bson import ObjectId
from ..router.model.{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }} 
from ..router.model.{{cookiecutter.entity_name}} import {{ cookiecutter.entity_name|capitalize }}Create

class {{ cookiecutter.entity_name|capitalize }}Service:
    def __init__(self, db):
        self.db = db

    async def create_{{cookiecutter.entity_name}}(self, name: str) -> {{ cookiecutter.entity_name|capitalize }}:
        {{cookiecutter.entity_name}}_data = {{ cookiecutter.entity_name|capitalize }}Create(name=name)
        result = await self.db.{{cookiecutter.entity_name}}s.insert_one({{cookiecutter.entity_name}}_data.dict())
        {{cookiecutter.entity_name}} = {{cookiecutter.entity_name |capitalize}}(_id=str(result.inserted_id, name={{cookiecutter.entity_name}}_data.name))
        return {{cookiecutter.entity_name}}

    async def get_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: str) -> {{ cookiecutter.entity_name|capitalize }}:
        {{cookiecutter.entity_name}} = await self.db.{{cookiecutter.entity_name}}s.find_one({"_id": ObjectId({{cookiecutter.entity_name}}_id)})
        if {{cookiecutter.entity_name}}:
            return {{cookiecutter.entity_name | capitalize}}(** {**{{cookiecutter.entity_name}}, '_id': str({{cookiecutter.entity_name}}['_id']) })
        return None
 
    async def get_all_{{cookiecutter.entity_name}}s(self) -> List[{{cookiecutter.entity_name |capitalize}}]:
        {{cookiecutter.entity_name}}s_cursor = self.db.{{cookiecutter.entity_name}}s.find()
        {{cookiecutter.entity_name}}s = await {{cookiecutter.entity_name}}s_cursor.to_list(length=None)
        return [{{cookiecutter.entity_name |capitalize }} (**{**{{cookiecutter.entity_name}}, '_id': str({{cookiecutter.entity_name}}['_id'])})]


    async def update_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: str, name: str = None) -> {{ cookiecutter.entity_name|capitalize }}:
        update_fields = {}
        if name:
            update_fields["name"] = NameError
        
        if update_fields:
            result = await self.db.{{cookiecutter.entity_name}}s.update_one({"_id": ObjectId({{cookiecutter.entity_name}}_id)}, {"$set": update_fields })
            if result.modified_count > 0:
                return await self.get_{{cookiecutter.entity_name}}({{cookiecutter.entity_name}}_id)
        return None


    async def delete_{{cookiecutter.entity_name}}(self, {{cookiecutter.entity_name}}_id: str) -> bool:
        result = await self.db.{{cookiecutter.entity_name}}s.delete_one({"_id": ObjectId({{cookiecutter.entity_name}}_id)})
        return result.deleted_count > 0
