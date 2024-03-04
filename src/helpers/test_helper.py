import unittest
from helpers.helper import compress_summary

class TestCompressSummary(unittest.TestCase):
    def test_compress_summary(self):
        original_summary = "This committee meets annually to assess the effectiveness of policies on environmental protection."
        expected_compressed_summary = "This com2it2e2 me2ts an2ual2y to as2es2 the ef2ectivenes2 of policies on environmental protection."
        compressed_summary = compress_summary(original_summary)
        self.assertEqual(compressed_summary, expected_compressed_summary)

if __name__ == '__main__':
    unittest.main()