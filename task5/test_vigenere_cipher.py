from unittest import TestCase, main
from vigenere_cipher import VigenereCipher


class TestVigenereCypher(TestCase):
    def test_encode(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_character(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertEqual(encoded, "X")

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")

    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertEqual(decoded, "ENCODEDINPYTHON")


if __name__ == "__main__":
    main()
