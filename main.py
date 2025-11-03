from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI(title="Time Service", version="1.0.0")


@app.get("/time")
def get_server_time():
    """Return the current server time in ISO 8601 format with timezone."""
    now = datetime.now(timezone.utc).astimezone()
    return {"server_time": now.isoformat()}


