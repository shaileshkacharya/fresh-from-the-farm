from fastapi import FastAPI

app = FastAPI(
    title="Fresh From The Farm API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "application": "Fresh From The Farm",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
