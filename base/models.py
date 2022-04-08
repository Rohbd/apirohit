from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import  SQLModel, Field




class BaseModel(SQLModel,table=True):

    id : UUID = Field(primary_key = True, uuid = uuid4)

    created_at : datetime.datetime | None = Field(None)

    modified_at : datetime.datetime | None = Field(None)

