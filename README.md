# flatini

Parse a simple INI file: one section level, `key = value`, and `#` or `;` comments.

Keys before the first section live under `""`. A repeated section continues the same dict. The parser does not interpolate and does not support nested sections.

```python
from flatini import parse_ini, get_value, section_names, has_section, section_size

doc = parse_ini("[app]\nname = demo\n")
get_value(doc, "app", "name")  # "demo"
section_names(doc)             # ["app"]
has_section(doc, "app")        # True
```

```bash
python -m unittest test_flatini.py
```

MIT
