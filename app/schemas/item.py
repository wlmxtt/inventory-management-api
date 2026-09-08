from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    nombre: str = Field(..., min_length=2)
    descripcion: Optional[str] = None
    precio: float = Field(..., gt=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2)
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, gt=0)


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True