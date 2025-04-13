from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductRepository:
    def create_product(self, db: Session, product: ProductCreate) -> Product:
        try:
            product_data = product.dict()
            db_product = Product(**product_data)
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
            return db_product
        except Exception as e:
            db.rollback()
            raise Exception(f"Erro ao criar produto: {str(e)}")

    def get_product(self, db: Session, product_id: int) -> Product:
        try:
            return db.query(Product).filter(Product.id == product_id).first()
        except Exception as e:
            raise Exception(f"Erro ao buscar produto: {str(e)}")
