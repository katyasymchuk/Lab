Lab2a: Основи роботи з Python
-

### Pre-requirements:
- встановлюю програми Python 3.8, git, PIP;
- робоче середовище: IntelIJ;

### Progress:

1. Ознайомлююся з оновани мови програмування Python.
2. Створюю Python файл test.py, в якому буду виконувати базові приклади:
    1. Виводжу вбудовані константи: 
        ```
        print('First constant', True)
        print('Second constant', False)
        print('Third constant', None)
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py 
        First constant True
        Second constant False
        Third constant None
        ```
    2. Виводжу результат роботи вбудованих функцій:
        ```
        print(f"abs(-5) є рівним {abs(-5)}")
        print(f"int(-10.3) є рівним {int(-10.3)}")
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py
        abs(-5) є рівним 5
        int(-5.3) є рівним -5
        ```
    3. Познайомлююся з циклами та розгалуженнями. Пишу код який демонструє їх роботу:
        ```
        from random import randint
        
        for  i in range(5):
            print(f"Interation #{i}:", end=' ')
            rand = randint(0, 1)
            if (rand):
                print(i)
            else:
                print(i%2)
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py
        Interation #0: 0
        Interation #1: 1
        Interation #2: 2
        Interation #3: 3
        Interation #4: 4    
        ```
    4. Використовую конструкцію `try->except->finally`:
        ```
        try:
            print("Випадкова помилка", 2 + '1')
        except Exception as e:
            print("\n", e, ". Схоже сталася помилка.")
        finally:
            print("Я завжди виконаюся.")
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py
        unsupported operand type(s) for +: 'int' and 'str' . Схоже сталася помилка.
        Я завжди виконаюся.
        ```
    5. Приклад використання контекст-менеджера:
        ```
        with open("README.md", "r", encoding='utf8') as file:
            data = file.read(30)
            print (data)
            file.close()      
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py
        Lab2a: Основи роботи з Python
        ```
    6. Приклад коду з використанням Лямбди:
        ```
        x = lambda a, b : a ** b
        print(f"Це функція лямбди: {x}")
        print(f"Виклик функції лямбда {x(5, 6)}")     
        ```
        - Результат виконання скрипта:
        ```
        $ python3 test.py
        Це функція лямбди: <function <lambda> at 0x000002AB241949D8>
        Виклик функції лямбда 15625
        ```
3.