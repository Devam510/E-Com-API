import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/ecommerce")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "5d0254f31c923e14d56914bd09441ae31fad7892fbc562d53497773eb24b698f")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()