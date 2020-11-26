import uvicorn
from fastapi import FastAPI

from routes.users import router as users_router


app = FastAPI()


app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
