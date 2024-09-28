print("Bem vindo a calculadora de gorgetas!")

bill = float(input("Qual o total da conta? R$ "))

tip = int(input("Qual a porcentagem de gortega que gostaria de dar? 10, 12 ou 15: "))

people = int(input("Para quantas pessoas iremos dividir: "))

tip_as_percentage = tip / 100

total_tip_amount = bill * tip_as_percentage

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

print(f"O valor da conta com gorgeta de {tip}% é R${round(bill_per_person, 2)}")

