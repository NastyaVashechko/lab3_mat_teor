import numpy as np

def utility(x):
    return np.sqrt(x)

def inverse_utility(u):
    return u ** 2

p1 = 0.5  
p2 = 0.5  

salary1_option1 = 1000
salary2_option1 = 3000

salary_option2 = 2000

expected_utility_option1 = p1 * utility(salary1_option1) + p2 * utility(salary2_option1)

deterministic_equivalent_option1 = inverse_utility(expected_utility_option1)

expected_salary_option1 = p1 * salary1_option1 + p2 * salary2_option1
risk_premium_option1 = expected_salary_option1 - deterministic_equivalent_option1

utility_option2 = utility(salary_option2)

if expected_utility_option1 > utility_option2:
    print("Рекомендується обрати перший варіант (невизначена зарплатня).")
else:
    print("Рекомендується обрати другий варіант (детермінована зарплатня).")

print(f"Очікувана корисність для першого варіанту: {expected_utility_option1}")
print(f"Детермінований еквівалент для першого варіанту: {deterministic_equivalent_option1}")
print(f"Премія за ризик для першого варіанту: {risk_premium_option1}")
print(f"Корисність для другого варіанту: {utility_option2}")
