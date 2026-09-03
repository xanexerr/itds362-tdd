from kitchen import Quantity, Converter



# def test_multiplication():
#      assert Quantity(200).times(3) == Quantity(600)
#      assert Quantity(200).times(2) == Quantity(400)
#      assert grams(1) != ounces(1)
     
def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)
    
def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")