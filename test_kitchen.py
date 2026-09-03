from kitchen import Quantity, Sum, Converter


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def test_simple_addition():
    total = grams(200).plus(grams(300))

    converter = Converter()

    assert converter.reduce(total, "g") == grams(500)


def test_plus_returns_sum():
    total = grams(200).plus(grams(300))

    assert isinstance(total, Sum)


def test_sum_can_reduce():
    total = Sum(grams(200), grams(300))

    assert total.reduce("g") == grams(500)


def test_addition_with_ounces():
    total = grams(200).plus(ounces(1))

    converter = Converter()

    assert converter.reduce(total, "g") == grams(228.35)


def test_addition_can_be_multiplied():
    total = grams(200).plus(ounces(1))
    doubled = total.times(2)

    converter = Converter()

    assert converter.reduce(doubled, "g") == grams(456.7)