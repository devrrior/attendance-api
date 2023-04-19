from pydantic import BaseModel, EmailStr


class Credentials(BaseModel):
    email: EmailStr
    password: str


class TokenPayload(BaseModel):
    sub: str
    exp: int
