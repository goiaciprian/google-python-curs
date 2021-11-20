

def suma_numerelor(n: int)-> int:
  """
    Returneaza suma numerelor de la 1 la n.
  """
  if(n == 0):
    return 0
  return n + (suma_numerelor(n-1))

def suma_numerelor_pare(n: int)-> int:
  """
    Returneaza suma numerelor pare de la 1 la n.
  """
  if(n == 0):
    return 0
  if(n % 2 == 0):
    return n + (suma_numerelor_pare(n-1))
  return suma_numerelor_pare(n-1)

def suma_numerelor_impare(n: int)-> int:
  """
    Returneaza suma numerelor impare de la 1 la n.
  """
  if(n == 0):
    return 0
  if(n % 2 != 0):
    return n + (suma_numerelor_impare(n-1))
  return suma_numerelor_impare(n-1)