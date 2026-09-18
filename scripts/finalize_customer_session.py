from pathlib import Path
Path("runtime").mkdir(exist_ok=True)
Path("runtime/session_finished").write_text("finished\n", encoding="utf-8")
print("customer session finalized")
