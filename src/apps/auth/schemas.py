from pydantic import BaseModel


class Credentials(BaseModel):
    email: str
    password: str


class TokenPayload(BaseModel):
    sub: str
    exp: int
