import json
import re
from email.utils import parseaddr
from typing import Dict, Optional

from pydantic import BaseModel, validator, constr


class AddUserRequest(BaseModel):
    user_id: constr(min_length=1)
    email: str
    password: constr(min_length=6)
    data: Optional[Dict]

    @validator('email')
    def email_validation(cls, v):
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', v):
            return v
        raise ValueError('Email field has an invalid format')


    @property
    def as_tuple(self):
        return (self.user_id, self.email, self.password, json.dumps(self.data))


class DeleteUserRequest(BaseModel):
    user_id: str
    password: str

    @property
    def as_tuple(self):
        return (self.user_id, self.password)