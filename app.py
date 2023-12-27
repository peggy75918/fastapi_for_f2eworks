import uvicorn
from fastapi import FastAPI
from router import homework
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="F2E Student Works",
    description="This API was developed for showing the work of students",
    version="0.0.1",
    terms_of_service="https://localhost:5000",
)
app.include_router(homework.router)

@app.get("/")
def root():
    return {"title":"Hello World"}

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)

origins = [
    'http://localhost:5173',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)