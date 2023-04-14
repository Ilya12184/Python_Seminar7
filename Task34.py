# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.

def rhyme(str):
    str = str.split()
    lst = []
    for word in str:
        sum = 0
        for i in word:
            if i.lower() in 'аеёиоуыэюя':
                sum += 1
        lst.append(sum)
    return len(lst) == lst.count(lst[0])


text = input("Введите фразу: ")
if rhyme(text):
    print('Парам пам-пам')
else:
    print('Пам парам')
