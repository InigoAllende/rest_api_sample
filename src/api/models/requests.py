import json
import re
from email.utils import parseaddr
from typing import Dict, Optional

from pydantic import BaseModel, validator


class AddUserRequest(BaseModel):
    user_id: str
    email: str
    password: str
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