num1 = int(input("Informe o valor A: "))
num2 = int(input("Informe o valor B: "))

print("Valor A, B antes da troca")
print(f"A = {num1}, B = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Valor A, B depois da troca")
print(f"A = {num1}, B = {num2}")