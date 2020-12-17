#!/usr/bin/env python3

import sys
import unittest

import cv2
import numpy as np


class TestCase(unittest.TestCase):
    def test_versions(self):
        versions = get_versions()
        self.assertIsInstance(versions, dict)


def get_versions():
    versions = {}
    versions["Python"] = ".".join(str(part) for part in sys.version_info[:3])
    versions["OpenCV"] = cv2.__version__
    versions["NumPy"] = np.__version__
    print("VERSIONS: {}".format(versions))
    return versions


if __name__ == "__main__":
    unittest.main()
