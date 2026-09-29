"""Read a flat INI file into nested dicts."""
from __future__ import annotations


def parse_ini(text: str) -> dict[str, dict[str, str]]:
    current = ""
    out: dict[str, dict[str, str]] = {current: {}}
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            if not current:
                raise ValueError(f"第 {line_no} 行节名为空")
            out.setdefault(current, {})
            continue
        if "=" not in line:
            raise ValueError(f"第 {line_no} 行缺少等号")
        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"第 {line_no} 行键为空")
        out[current][key] = value.strip()
    if not out[""]:
        out.pop("")
    return out


def get_value(doc: dict[str, dict[str, str]], section: str, key: str, default: str = "") -> str:
    return doc.get(section, {}).get(key, default)
