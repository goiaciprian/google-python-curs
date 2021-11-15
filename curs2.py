import copy

lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print(f"Lista initiala {lista_initiala}")

lista_ordinata_crescator = sorted(lista_initiala)

print(f"Lista ordonata crescator {lista_ordinata_crescator}")

lista_ordonata_descrecator = sorted(lista_initiala, reverse=True)

print(f"Lista ordonata descrescator {lista_ordonata_descrecator}")

print(f"Lista cu numere pare {lista_ordinata_crescator[1::2]}")
print(f"Lista cu numere impare {lista_ordinata_crescator[::2]}")

print(f"Multiplu 3 {[x for x in lista_ordinata_crescator if x % 3 == 0]}")