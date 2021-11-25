from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas import Token, UserLogin

from .. import database, models, utils, oauth2

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )
    auth_error = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
    )

    if not user:
        raise auth_error

    if not utils.verify(user_credentials.password, user.password):
        raise auth_error

    access_token = oauth2.create_access_token({"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
