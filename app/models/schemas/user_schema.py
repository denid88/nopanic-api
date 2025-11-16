import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy import Column, String, Boolean, DateTime

class UserSchema(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    otp = Column(String, nullable=True)
    otp_expires_at = Column(DateTime, nullable=True)
    google_id = Column(String, nullable=True)
    apple_id = Column(String, nullable=True)
    is_email_verified = Column(Boolean, default=False)
    reset_password_token = Column(String, nullable=True)
    reset_password_token_expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())