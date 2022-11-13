from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from database.conx import SessionLocal
from database.models import ResponseContent, WidgetAccess
from utils.utils import accessRejectedContent

load_dotenv()

router = APIRouter(
	prefix="/api/v1/widget",
	tags=[],
	responses={404: accessRejectedContent, 400: accessRejectedContent},
)


# Dependency
def get_db ():
	print('get connc')
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@router.post("/save-connection",response_model=ResponseContent)
async def save_client_connection (request: Request, db: Session = Depends(get_db)):
	try:
		
		body_json = await request.json()
		apiKey = body_json['apiKey']
		domain = body_json['domain']
		ipAddress = body_json['ipAddress']
		agent = body_json['agent']
		
		model = WidgetAccess(apiKey=apiKey, domain=domain, ipAddress=ipAddress, agent=agent)
		db.add(model)
		db.commit()
		
		return ResponseContent(success=True,
							   message="Completed")
	except Exception as e:
		print(e)
		raise HTTPException(status_code=400, detail="Error")
	
	return ResponseContent(success=False,
							   message="Access Rejected")
