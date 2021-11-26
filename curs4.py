# l = [2, 3]
# l_2 = list()

# l_2.append(1)
# l_2.append(2)
# l_2.extend([4, 5, 6])

# print(l_2);

class Coordinate(object):
  """
    O coordonata compusa din valorile x, y
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"<{self.x}, {self.y}> "

  def distance(self, other)->int:
    """Returneaza distanta euclidiana dintre cele 2 coordonate """
    x_diff_sq = (self.x - other.x) ** 2
    y_diff_sq = (self.y - other.y) ** 2
    return (x_diff_sq + y_diff_sq) ** 0.5

origin, c1 = Coordinate(0, 0), Coordinate(1, 1)
c2 = Coordinate(0, 4)

print(origin)
print(c1)

print(origin.distance(c1))
print(origin.distance(c2))

  
