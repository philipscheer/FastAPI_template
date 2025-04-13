from fastapi import FastAPI
from app.api.v1.endpoints import user, product 
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar os endpoints de usuário
app.include_router(user.router, prefix=settings.API_V1_STR)

# Registrar os endpoints de produto
app.include_router(product.router, prefix=f"{settings.API_V1_STR}/products") 
