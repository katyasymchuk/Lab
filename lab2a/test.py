from random import randint

#i
print('First constant', True)
print('Second constant', False)
print('Third constant', None)

#ii
print(f"\nabs(-5) є рівним {abs(-5)}")
print(f"int(-10.3) є рівним {int(-10.3)}\n")

#iii
for i in range(5):
    print(f"Interation #{i}:", end=' ')
    rand = randint(0, 1)
    if (rand):
        print(i)
    else:
        print(i%2)

#iv
try:
    print("Випадкова помилка", 2 + '1')
except Exception as e:
    print("\n", e, ". Схоже сталася помилка.")
finally:
    print("Я завжди виконаюся.\n")

#v
with open("README.md", "r", encoding='utf8') as file:
    data = file.read(30)
    print (data)
    file.close()

#vi
x = lambda a, b : a ** b
print(f"Це функція лямбди: {x}")
print(f"Виклик функції лямбда {x(5, 6)}")