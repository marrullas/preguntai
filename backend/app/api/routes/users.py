from fastapi import APIRouter
from fastapi_users import FastAPIUsers
#from fastapi_users.authentication import JWTAuthentication
from fastapi_users.authentication import JWTStrategy
from app.schemas.users import UserDB, UserCreate, UserUpdate
from app.core.config import SECRET_KEY, DATABASE_URL
from app.core.db import get_db


router = APIRouter()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)
#jwt_authentication = JWTAuthentication(secret=SECRET_KEY, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    get_db,
    [get_jwt_strategy],
    UserDB,
    UserCreate,
    UserUpdate,
    UserDB,
)

router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt")
router.include_router(fastapi_users.get_register_router(), prefix="/auth")
router.include_router(fastapi_users.get_users_router(), prefix="/users")
