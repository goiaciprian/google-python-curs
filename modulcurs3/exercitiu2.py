

def citeste_numar_intreg()->int:
  """
    Citeste de la tastatura un numar intreg
  """
  numar = 0;
  try:
    numar = int(input("Introduceti un numar intreg: "));
  except ValueError:
    pass
  return numar;