from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = ROOT / "aligned_reader" / "index.html"


class ReaderHtmlTests(unittest.TestCase):
    def test_reader_saves_and_restores_latest_paragraph_position(self):
        html = INDEX_HTML.read_text(encoding="utf-8")

        self.assertIn("readerProgressKey", html)
        self.assertIn("function saveProgress", html)
        self.assertIn("function loadSavedProgress", html)
        self.assertIn("localStorage.setItem(readerProgressKey", html)
        self.assertIn("localStorage.getItem(readerProgressKey", html)
        self.assertIn("savedProgress.paragraphId", html)
        self.assertIn("loadChapter(savedProgress.chapterIndex", html)
