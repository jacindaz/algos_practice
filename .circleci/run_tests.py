import os
import pytest

CURRENT_DIR = os.path.dirname(os.path.realpath('__file__'))


def run_tests():
    tests_file_path = CURRENT_DIR + "/tests"
    print(f"Test directory: {tests_file_path}")
    os.system(f"pytest {tests_file_path}")

run_tests()
