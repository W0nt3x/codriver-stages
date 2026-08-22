"""Rebuild index.json from stages/*.json. Runs in CI after every merge."""
import json, pathlib, sys, time

root = pathlib.Path(__file__).resolve().parents[1]
stages = []
for path in sorted((root / "stages").glob("*.json")):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"skip {path.name}: {exc}", file=sys.stderr)
        continue
    if data.get("format") != "codriver-stage":
        print(f"skip {path.name}: not a codriver stage", file=sys.stderr)
        continue
    community = data.get("community", {})
    stages.append({
        "file": path.name,
        "name": data.get("name", path.stem),
        "length_m": data.get("length_m", 0.0),
        "notes": len(data.get("notes", [])),
        "author": community.get("author", ""),
        "shared_utc": community.get("shared_utc", ""),
        "tool_version": community.get("tool_version", ""),
    })
index = {"generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "stages": stages}
(root / "index.json").write_text(json.dumps(index, indent=1) + "\n", encoding="utf-8")
print(f"{len(stages)} stage(s) indexed")
