class Quantity:
     def __init__(self, amount, unit="g"):
        self.amount = amount
        self.unit = unit

     def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

     def plus(self, other):
        return Sum(self, other)

     def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.unit == other.unit
        )
     def reduce(self, unit):
          if self.unit == unit:
               return Quantity(self.amount, unit)

          if self.unit == "oz" and unit == "g":
               return Quantity(self.amount * 28.35, "g")

          if self.unit == "g" and unit == "oz":
               return Quantity(self.amount / 28.35, "oz")

          raise ValueError(f"แปลงจาก {self.unit} เป็น {unit} ไม่ได้")
   
     def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
     def __init__(self, left, right):
        self.left = left
        self.right = right

     def reduce(self, unit):
        left = self.left.reduce(unit)
        right = self.right.reduce(unit)

        return Quantity(
            left.amount + right.amount,
            unit
        )
        
class Converter:
    def reduce(self, expression, unit):
        return expression.reduce(unit)
