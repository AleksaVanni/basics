born_year_Pushkin = 1799
born_day_Pushkin = '6 июня'

bornyear_question = int(input('В каком году родился А.С. Пушкин?: '))

if bornyear_question == born_year_Pushkin:
    bornday_question = input('Введите день рождения А.С. Пушкина: ')
    if bornday_question == born_day_Pushkin:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')