# flatini

Parse a simple INI file: one section level, `key = value`, and `#` or `;` comments.

Keys before the first section live under `""`. A repeated section continues the same dict. The parser does not interpolate and does not support nested sections.

```python
from flatini import parse_ini, get_value

doc = parse_ini("[app]\nname = demo\n")
get_value(doc, "app", "name")  # "demo"
```

```bash
python -m unittest test_flatini.py
```

MIT
