"""Build the reduced, self-contained Agensi candidate using an explicit allowlist."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = ROOT / "distribution" / "agensi-free"
    args.output.mkdir(parents=True, exist_ok=True)
    files = {"SKILL.md": source / "SKILL.md", "LICENSE": ROOT / "LICENSE"}
    content = files["SKILL.md"].read_text()
    license_text = files["LICENSE"].read_text()
    if license_text.strip() not in content:
        raise ValueError("The complete unchanged MIT notice must also be inline")
    if "references/" in content or "examples/" in content:
        raise ValueError("This candidate must not depend on external file paths")
    archive = args.output / "psych-aware-free-0.1.0.zip"
    manifest = {"version": "0.1.0", "files": {}}
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for name, path in sorted(files.items()):
            data = path.read_bytes()
            entry = zipfile.ZipInfo(name, date_time=(2026, 10, 31, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            package.writestr(entry, data)
            manifest["files"][name] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        assert sorted(package.namelist()) == sorted(files)
        for name, path in files.items():
            assert package.read(name) == path.read_bytes()
    manifest["archive"] = {"name": archive.name, "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}
    (args.output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
