from pathlib import Path
Path("runtime").mkdir(exist_ok=True)
with Path("runtime/hook_audit.log").open("a", encoding="utf-8") as stream:
    stream.write("PostToolUse recorded\n")
print("tool call audited")
