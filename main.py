import uvicorn
import os
from dotenv import load_dotenv

from app import models
from app.application import create_application
from app.database.connection import engine, get_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = create_application()

models.Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def start_cron():
    get_db()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")), reload=True)