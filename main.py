from datetime import datetime, date, timezone
from fastapi import FastAPI

app = FastAPI(title="Time Service", version="1.0.0")


@app.get("/time")
def get_server_time():
    """Return the current server time in ISO 8601 format with timezone."""
    now = datetime.now(timezone.utc).astimezone()
    return {"server_time": now.isoformat()}



@app.get("/time/utc")
def get_utc_time():
    """Return the current UTC time in ISO 8601 format (Z)."""
    now_utc = datetime.now(timezone.utc)
    # Ensure trailing 'Z' for UTC representation
    return {"utc_time": now_utc.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")}


@app.get("/date")
def get_local_date():
    """Return today's local date (based on server timezone) in YYYY-MM-DD."""
    local_dt = datetime.now(timezone.utc).astimezone()
    return {"date": local_dt.date().isoformat()}


@app.get("/date/utc")
def get_utc_date():
    """Return today's UTC date in YYYY-MM-DD."""
    return {"utc_date": date.today().isoformat()}


@app.get("/timestamp")
def get_unix_timestamp():
    """Return current Unix timestamp in seconds (int)."""
    epoch_seconds = int(datetime.now(timezone.utc).timestamp())
    return {"timestamp": epoch_seconds}

