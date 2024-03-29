part_one = str(input())
part_sec = str(input())

part_one_value = float(part_one.split(' ')[2]) * float(part_one.split(' ')[1])
part_sec_value = float(part_sec.split(' ')[2]) * float(part_sec.split(' ')[1])

total_value = part_one_value + part_sec_value

print(f"VALOR A PAGAR: R$ {total_value:.2f}")
