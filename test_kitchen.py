from kitchen import Quantity



def test_multiplication():
     assert Quantity(200).times(3) == Quantity(600)
     assert Quantity(200).times(2) == Quantity(400)