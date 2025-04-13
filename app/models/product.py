from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base

class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)  # Controle de estoque
    sku = Column(String, unique=True, index=True, nullable=False)  # Código único do produto
