import unittest

from flatini import blank_in, empty_sections, filled_in, get_value, has_key, has_section, keys_in, parse_ini, section_count, section_names, section_size


class FlatiniTest(unittest.TestCase):
    def test_sections(self) -> None:
        text = "bare=1\n\n[app]\nname = demo\n; comment\n[app]\nport=80\n"
        self.assertEqual(
            parse_ini(text),
            {"": {"bare": "1"}, "app": {"name": "demo", "port": "80"}},
        )

    def test_get_value(self) -> None:
        doc = parse_ini("[app]\nname = demo\n")
        self.assertEqual(get_value(doc, "app", "name"), "demo")
        self.assertEqual(get_value(doc, "app", "missing", "no"), "no")
        self.assertEqual(section_names(parse_ini("bare=1\n[app]\na=b\n")), ["app"])
        self.assertTrue(has_section(doc, "app"))
        self.assertFalse(has_section(doc, "missing"))
        self.assertEqual(section_size(doc, "app"), 1)
        self.assertEqual(section_size(doc, "missing"), 0)
        self.assertTrue(has_key(doc, "app", "name"))
        self.assertFalse(has_key(doc, "app", "missing"))
        self.assertEqual(keys_in(doc, "app"), ["name"])
        self.assertEqual(section_count(doc), 1)
        self.assertEqual(empty_sections({"app": {"name": "demo"}, "bare": {}}), ["bare"])
        self.assertEqual(blank_in({"app": {"name": "demo", "note": ""}}, "app"), ["note"])
        self.assertEqual(filled_in({"app": {"name": "demo", "note": ""}}, "app"), ["name"])

    def test_empty_section_dropped(self) -> None:
        self.assertEqual(parse_ini("[only]\na=b\n"), {"only": {"a": "b"}})


if __name__ == "__main__":
    unittest.main()
