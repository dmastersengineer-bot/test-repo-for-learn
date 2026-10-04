# Reverse a string without using built-in functions
s = "azuredevops"
reversed_str = ""

for ch in s:
    reversed_str = ch + reversed_str
    # A+"" = A
    # z+A= zA
    # u+zA= uzA


print(reversed_str)
# one line added here in code1