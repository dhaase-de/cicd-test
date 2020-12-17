#!/usr/bin/env python3

import unittest


class TestCase(unittest.TestCase):
    def test_imports(self):
        import cv2
        print("test_imports:  OpenCV  {}".format(cv2.__version__))

        import numpy as np
        print("test_imports:  NumPy   {}".format(np.__version__))
        
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
