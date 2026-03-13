from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

security = HTTPBearer()

SECRET = "SUPERSECRET"
ALGORITHM = "HS256"

def get_current_user(token=Depends(security)):

    try:
        payload = jwt.decode(token.credentials, SECRET, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")