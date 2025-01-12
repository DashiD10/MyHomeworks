student = input("Введите имя студента")
assessment = input("Введите оценку студента")
print(assessment.isdigit())
if int(assessment) >= 1 and int(assessment) <= 3:
    print("Начальный уровень")
elif int(assessment) >= 4 and int(assessment) <= 6:
    print("Средний уровень")
elif int(assessment) >= 7 and int(assessment) <= 9:
    print("Достаточный уровень")
elif int(assessment) >= 10 and int(assessment) <= 12:
    print("Высокий уровень")
else:
    print("Введены некорректные данные")
