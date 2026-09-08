from pydantic import BaseModel
from typing import Optional

# Base común para atributos de producto
class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    stock: int = 0

# Esquema para crear un producto (lo que envía el cliente)
class ProductCreate(ProductBase):
    pass

# Esquema para actualizar un producto
class ProductUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

# Esquema para responder al cliente (lo que devuelve la API)
class ProductResponse(ProductBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True