from pydantic import BaseModel, Field
from typing import Optional

class RolUserModel(BaseModel):
    encryptedToken: Optional[str] = ''
    role:  Optional[str] = ''