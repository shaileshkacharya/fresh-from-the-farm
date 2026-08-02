from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    hashed_password: str
    full_name: Optional[str] = None
    role: str = Field(default="customer")
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
