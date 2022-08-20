from datetime import date, datetime
from pydantic import BaseModel, Field
from typing import Optional

class RolUserModel(BaseModel):
    encryptedToken: Optional[str] = ''
    role:  Optional[str] = ''
    expirationDate:  Optional[datetime] = date.today()