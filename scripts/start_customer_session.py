from pathlib import Path
Path("runtime").mkdir(exist_ok=True)
Path("runtime/session_started").write_text("started\n", encoding="utf-8")
print("customer session initialized")
