#IMPORTS
from pydantic import BaseModel, Field
from typing import Annotated

#SCHEMAS
class ProductoSchema(BaseModel):
    id: Annotated[int, Field(gt=0)]
    nombre: Annotated[str, Field(min_length=1)]
    tipo_de_producto: Annotated[str, Field(min_length=1)]
    marca: Annotated[str, Field(min_length=1)]
    precio: Annotated[int, Field(gt=0)]
    imagen: Annotated[str, Field(min_length=1)]


class ProductoUpdateSchema(BaseModel):
    nombre: Annotated[str, Field(min_length=1)]
    tipo_de_producto: Annotated[str, Field(min_length=1)]
    marca: Annotated[str, Field(min_length=1)]
    precio: Annotated[int, Field(gt=0)]
    imagen: Annotated[str, Field(min_length=1)]