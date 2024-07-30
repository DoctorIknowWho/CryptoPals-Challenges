# Test class for challenge1.py

import unittest
from challenge1 import hex_to_base64

class TestChallenge1(unittest.TestCase):
    def test_hex_to_base64(self):
        self.assertEqual(hex_to_base64('FACE'), '+s4=')
        self.assertEqual(hex_to_base64('DEADBEEF'), '3q2+7w==')
        self.assertEqual(hex_to_base64(''), '')
        self.assertEqual(hex_to_base64('F'), 'Dw==')
        self.assertEqual(hex_to_base64('12BA34'), 'Ero0')
        self.assertFalse(hex_to_base64('FACE') == '3q2+7w==')
        self.assertEqual(hex_to_base64('Z'), 'Invalid hex string')

    def crpytopals_test(self):
        self.assertEqual(hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'),
                         'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

if __name__ == '__main__':
    unittest.main()


