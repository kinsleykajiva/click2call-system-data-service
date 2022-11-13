

from starlette.responses import JSONResponse


accessRejectedContent = {
	"success": False,
	'access': False,
	"message": "Access Rejected"
}



def accessRejected ():
	return JSONResponse(status_code=200, content=accessRejectedContent)
