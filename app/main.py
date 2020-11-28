import uvicorn
from fastapi import FastAPI

from routes.users import router as users_router
from routes.budgets import router as budgets_router


app = FastAPI()


app.include_router(users_router, prefix='/users')
app.include_router(budgets_router, prefix='/budgets')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
