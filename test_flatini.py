import unittest

from flatini import parse_ini


class FlatiniTest(unittest.TestCase):
    def test_sections(self) -> None:
        text = "bare=1\n\n[app]\nname = demo\n; comment\n[app]\nport=80\n"
        self.assertEqual(
            parse_ini(text),
            {"": {"bare": "1"}, "app": {"name": "demo", "port": "80"}},
        )

    def test_empty_section_dropped(self) -> None:
        self.assertEqual(parse_ini("[only]\na=b\n"), {"only": {"a": "b"}})


if __name__ == "__main__":
    unittest.main()
