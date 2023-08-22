from sqlalchemy.orm import Session
from database.db import SessionLocal
from schemas import ContactCreate, ContactRead
from database.models import Contact  


def create_contact(db: Session, contact_data: ContactCreate):
    #  логика для создания контакта в базе данных
    contact = Contact(**contact_data.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_contacts(db: Session):
    # логика для получения всех контактов из базы данных
    return db.query(Contact).all()

def get_contact_by_id(db: Session, contact_id: int):
    # логика для получения контакта по ID из базы данных
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, contact_data: ContactCreate):
    # логика для обновления контакта в базе данных по ID
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in contact_data.dict().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    #  логика для удаления контакта из базы данных по ID
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return {"message": "Contact deleted successfully"}