from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PluginContractTest(unittest.TestCase):
    def test_plugin_exposes_plugin_first_skill_surface(self) -> None:
        skills = {
            child.name
            for child in (ROOT / "skills").iterdir()
            if child.is_dir() and (child / "SKILL.md").is_file()
        }

        self.assertEqual(
            {"inventory", "scan", "bom", "explain", "triage", "sync"},
            skills,
        )

    def test_readme_documents_plugin_first_adoption(self) -> None:
        readme = (ROOT / "README.md").read_text()

        self.assertIn("preferred developer install path", readme)
        self.assertIn("/openaca:inventory", readme)
        self.assertIn("/openaca:sync", readme)
        self.assertIn("MDM", readme)


if __name__ == "__main__":
    unittest.main()
