from modulcurs3 import suma_parametrilor, citeste_numar_intreg, suma_numerelor, suma_numerelor_pare, suma_numerelor_impare


if(__name__ == "__main__"):
  print("Exercitiul 1")
  print(suma_parametrilor(1,2,3,4,5, 'asd', 'asdsa', False))
  print(suma_parametrilor(2, 3, param_1=2))

  print("\nExercitiul 2")
  print(citeste_numar_intreg())

  print("\nExercitiul 3")
  print(f"Suma numerelor pana la 5 {suma_numerelor(5)}")
  print(f"Suma numerelor pare pana la 5 {suma_numerelor_pare(5)}")
  print(f"Suma numerelor impare pana la 5 {suma_numerelor_impare(5)}")
