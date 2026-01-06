from fastapi import FastAPI
from app.routers import zone_router


app = FastAPI(title="YouExpress Logistics API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to YouExpress Logistics API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(zone_router.router)

