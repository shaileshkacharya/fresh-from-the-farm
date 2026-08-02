from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

from app.schemas.auth import UserCreate, UserRead, Token
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token
from app.db.session import get_session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead)
async def register(user_in: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(email=user_in.email, hashed_password=hash_password(user_in.password), full_name=user_in.full_name)
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return user

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    # form_data.username, form_data.password
    stmt_user = await session.execute("SELECT * FROM user WHERE email = :email", {"email": form_data.username})
    row = stmt_user.first()
    user = None
    if row:
        # SQLModel returns Row; convert to User via session.get
        try:
            user = await session.get(User, row[0])
        except Exception:
            user = None
    if not user:
        # Try fetch by email properly
        users = await session.exec("SELECT * FROM user WHERE email = :email", {"email": form_data.username})
        row = users.first()
        if row:
            # When using exec with SQLModel, rows are mapped; but to be robust, fallback:
            user = row
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    if not verify_password(user.hashed_password, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=Token)
async def refresh_token(refresh_token: str):
    payload = None
    try:
        from app.core.security import decode_token
        payload = decode_token(refresh_token)
    except Exception:
        payload = None
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    sub = payload.get("sub")
    access_token = create_access_token(subject=str(sub))
    new_refresh = create_refresh_token(subject=str(sub))
    return Token(access_token=access_token, refresh_token=new_refresh)

@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(lambda: None)):
    # This endpoint should be protected by dependency overrides in the app; for now return placeholder
    return current_user
