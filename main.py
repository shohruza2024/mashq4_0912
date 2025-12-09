#1-misol
words = ["hello", "say", "hi", "welcome"]
result = list(map(lambda w: f"{w[0]}-{len(w)-1}", words))
print(result)

#2-misol
royxat = ["Ali Valiyev", "Bobur Yo'ldoyev", "Stive Jobs", "Bill Gates"]
result = list(map(lambda x: f"{x.split()[0]} {x.split()[1][0]}.", royxat))
print(result)

#3-misol
royxat = ["Ali", "Bobur", "Stive", "Santyago"]
result = list(map(lambda x: x + str(len(x)), royxat))
print(result)

#4-misol
sozlar = ["HELLO", "say", "hi", "Welcome"]
result = list(map(lambda s: s[:-1] + s[-1].upper(), sozlar))
print(result)

#5-misol
sozlar = ["apple", "banana", "cherry", "avocado", "grape", "strawberry"]
result = list(filter(lambda s: len(s) > 5 and "a" in s, sozlar))
print(result)
