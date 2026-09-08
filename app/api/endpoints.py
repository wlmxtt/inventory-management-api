from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.database import get_db
from app.models.item import ItemModel
from app.models.user import UserModel
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["Items"])


# Endpoint PÚBLICO (cualquiera puede ver los items)
@router.get("/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(ItemModel).all()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado"
        )
    return item


# Endpoints PROTEGIDOS (requieren estar autenticado)
@router.post(
    "/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED
)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    nuevo_item = ItemModel(**item.model_dump())
    db.add(nuevo_item)
    db.commit()
    db.refresh(nuevo_item)
    return nuevo_item


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item_data: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    item_query = db.query(ItemModel).filter(ItemModel.id == item_id)
    item = item_query.first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado"
        )

    datos_actualizados = item_data.model_dump(exclude_unset=True)
    item_query.update(datos_actualizados)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    item_query = db.query(ItemModel).filter(ItemModel.id == item_id)
    item = item_query.first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado"
        )

    item_query.delete(synchronize_session=False)
    db.commit()
    return None