from datetime import datetime, timedelta
import secrets
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from app.core.database import get_db
from app.core.security import hash_password, create_access_token, verify_password
from app.models.dtos.auth.login_request import LoginRequest
from app.models.dtos.auth.register_request import RegisterRequest
from app.models.dtos.auth.token_response import TokenResponse
from app.models.schemas.user_schema import UserSchema

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
"/login",
    summary="Login",
    description="Login user by email",
    response_model=TokenResponse
)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserSchema).filter(UserSchema.email == credentials.email).first()
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found or inactive"
        )
    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невірний email або пароль"
        )

    token = TokenResponse(
        access_token=create_access_token(email=user.email)
    )
    return token

@router.post(
"/register",
    response_model=TokenResponse,
    summary="Sign up",
    description="Registration user by email",
    status_code=201
)
async def register(user: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(UserSchema).filter(UserSchema.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Користувач з таким email вже існує"
        )

    otp_code = secrets.randbelow(1000000)
    otp_code_str = str(otp_code).zfill(6)

    otp_expires_at = datetime.now() + timedelta(minutes=10)

    token = TokenResponse(
        access_token=create_access_token(email=user.email)
    )

    new_user = UserSchema(
        email=user.email,
        password=hash_password(user.password),
        otp=otp_code_str,
        otp_expires_at=otp_expires_at
    )
    db.add(new_user)
    db.commit()

    return token
