from unittest import TestCase
from pylint.lint import Run


class LintTest(TestCase):

    def test_app(self):
        with self.assertRaises(SystemExit) as lint_check:
            Run(['--errors-only', 'grio'])
        self.assertEqual(lint_check.exception.code, 0)
