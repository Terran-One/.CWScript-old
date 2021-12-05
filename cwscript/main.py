import os
from parser import parse

test_file_path = os.path.join(os.path.dirname(__file__), "test_contract.cws")
text = open(test_file_path).read()

parse(text)
