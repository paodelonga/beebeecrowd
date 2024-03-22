nota_a = float(input())
nota_b = float(input())
nota_c = float(input())

peso_a = 2
peso_b = 3
peso_c = 5
peso_total = peso_a + peso_b + peso_c

avg = ((peso_a * nota_a) + (peso_b * nota_b) + (peso_c * nota_c)) / peso_total

print(f"MEDIA = {avg:.1f}")
