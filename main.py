from fastapi import FastAPI, Depends, HTTPException
from database import get_db, Tickets
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()


class TicketCreate(BaseModel):
    name:str
    age:int
    use:str
    price:int

@app.post("/tickets/")
async def create_ticket(ticktet: TicketCreate, db:Session=Depends(get_db)):
    new_ticket=Tickets(name=ticktet.name, age=ticktet.age, use=ticktet.use, price=ticktet.price)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.get("/tickets/")
async def all_tickets(db:Session=Depends(get_db)):
    return db.query(Tickets).all()

@app.get("/tickets/{ticket_id}")
async def all_tickets(ticket_id:int,db:Session=Depends(get_db)):
    ticket = db.query(Tickets).filter(Tickets.id==ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Not Found")
    return ticket

@app.get("/tickets/age/{age}")
async def get_tickets_by_age(age: int, db: Session = Depends(get_db)):
    tickets = db.query(Tickets).filter(Tickets.age == age).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="No tickets found for this age group")
    return tickets




