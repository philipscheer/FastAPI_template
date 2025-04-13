import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.session import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

client = TestClient(app)

# Mock para o banco de dados
@pytest.fixture
def db_session():
    # Aqui você pode configurar um banco de dados em memória ou mockado
    # para os testes. Por exemplo, usando SQLite em memória.
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.db.base import Base

    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Substituir a dependência do banco de dados
app.dependency_overrides[get_db] = db_session

def test_create_product(db_session: Session):
    product_data = {"name": "Test Product", "sku": "TEST123", "price": 100.0, "stock": 10}
    response = client.post("/v1/products/", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["sku"] == product_data["sku"]

def test_get_product(db_session: Session):
    # Criar um produto diretamente no banco de dados
    product = Product(name="Test Product", sku="TEST123", price=100.0, stock=10)
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    response = client.get(f"/v1/products/{product.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product.id
    assert data["name"] == product.name

def test_update_product(db_session: Session):
    # Criar um produto diretamente no banco de dados
    product = Product(name="Test Product", sku="TEST123", price=100.0, stock=10)
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    update_data = {"name": "Updated Product", "price": 150.0}
    response = client.put(f"/v1/products/{product.id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["price"] == update_data["price"]

def test_delete_product(db_session: Session):
    # Criar um produto diretamente no banco de dados
    product = Product(name="Test Product", sku="TEST123", price=100.0, stock=10)
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    response = client.delete(f"/v1/products/{product.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Product deleted successfully"

    # Verificar se o produto foi realmente deletado
    response = client.get(f"/v1/products/{product.id}")
    assert response.status_code == 404