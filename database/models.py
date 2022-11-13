from database.conx import Base
from dataclasses import dataclass
from sqlalchemy import DateTime, Column, func, Integer, String
from typing import Optional, Any


@dataclass
class ResponseContent:
	success: bool
	access: Optional[bool] = None
	message: Optional[str] = None
	data: Optional[Any] = None


class WidgetAccess(Base):
	__tablename__ = "widgetAccess"
	
	id = Column(Integer, primary_key=True,index=True)
	apiKey = Column(String)
	domain = Column(String)
	ipAddress = Column(String,nullable=True)
	agent = Column(String)
	dateCreated = Column(DateTime(timezone=True), default=func.now())
