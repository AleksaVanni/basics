print('Игра "Викторина"')

play_again = 'да'
while play_again == 'да':

    print('Ответьте на вопросы:')
    print('*' * 20)

    answer_putin = input('В каком году родился Путив В.В.?: ')
    # правильный ответ 1952
    answer_gagarin = input('В каком году родился Юрий Гагарин?: ')
    # правильный ответ 1934
    answer_mendeleev = input('Год рождения Менделеева Д.И.?: ')
    # правильный ответ 1834
    answer_petrI = input('В каком году родился Петр I?: ')
    # правильный ответ 1672
    answer_esenin = input('Напишите год рождения Сергея Есенина: ')
    # правильный ответ 1895

    print('*' * 20)
    print('Подсчет баллов:')
    print()
    correct = 0
    error = 0
    if answer_putin == '1952':
        correct += 1
    else:
        error += 1
    if answer_gagarin == '1934':
        correct += 1
    else:
        error += 1
    if answer_mendeleev == '1834':
        correct += 1
    else:
        error += 1
    if answer_petrI == '1672':
        correct += 1
    else:
        error += 1
    if answer_esenin == '1895':
        correct += 1
    else:
        error += 1

    print('Количество правильных ответов: ', correct)
    print('Процент правильных ответов', correct * 100 / 5, '%')
    print('Количество ошибок', error)
    print('Процент неправильных ответов', error * 100 / 5, '%')

    play_again = input("Хотите сыграть еще раз? ('да'/'нет'): ")

print('конец викторины')
