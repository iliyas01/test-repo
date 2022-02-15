from typing import TYPE_CHECKING,List
import sqlalchemy.orm as _orm 
import schemas as _schemas 
import fastapi as _fastapi 
import services as _services 
from fastapi import HTTPException
import uvicorn
if TYPE_CHECKING:
    from sqlalchemy.orm import session
    
app = _fastapi.FastAPI()


@app.post("/api/contacts", response_model=_schemas.Contact)

async def create_contact(contact:_schemas.CreateContact,
                         db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await  _services.create_contact(contact=contact,db=db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    
@app.get('/api/contacts',response_model=List[_schemas.Contact])
async def get_contacts(db : _orm.Session=_fastapi.Depends(_services.get_db)):
    return await _services.get_all_contacts(db=db)

@app.get("/api/contacts/{contact_id}/" ,response_model=_schemas.Contact)
async def get_contact(contact_id:int,db: _orm.Session=_fastapi.Depends(_services.get_db)):
    return await _services.get_contact(contact_id=contact_id,db=db)

@app.delete("/api/contacts/{contact_id}")
async def get_contact(contact_id:int,db: _orm.Session=_fastapi.Depends(_services.get_db)):
    contact =  await _services.get_contact(db=db,contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404,detail="User does not exist")
    await _services.delete_contact(contact,db=db)
    return "Success"

@app.put("/api/contacts/{contact_id}/" ,response_model=_schemas.Contact)
async def update_contact(contact_id:int,
                         contact_data: _schemas.CreateContact,
                         db: _orm.Session=_fastapi.Depends(_services.get_db)):
    contact =  await _services.get_contact(db=db,contact_id=contact_id)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404,detail="User does not exist")
    
    return await _services.update_contact(contact_data=contact_data,contact=contact,db=db)
    