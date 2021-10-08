import math

def test_simple_math():
  a = 2
  b = 3
  try:
    assert a+b == 5
  except:
    print("Incorrect function")
