#!/usr/bin/env python3

import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(description="")
    #parser.add_argument(help="")
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    print("===== main.py =====")

    import cv2
    print("OpenCV  {}".format(cv2.__version__))

    import numpy as np
    print("NumPy   {}".format(np.__version__))
    
    print("===================")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR: {} ({})".format(e, type(e).__name__))
        sys.exit(1)

