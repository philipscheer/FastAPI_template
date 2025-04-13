from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int
    sku: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: str | None = None
    price: float | None = None
    stock: int | None = None

class ProductInDB(ProductBase):
    id: int

    class Config:
        orm_mode = True
