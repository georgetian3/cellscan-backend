from pydantic import BaseModel

class Client(BaseModel):
    latest_version: str | None