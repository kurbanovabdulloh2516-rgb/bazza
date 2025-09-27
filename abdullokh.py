# # print(123)
# name = int(input('ведите цыфру '))
# print( name)

# print(type(name))


# num = int(input('ведите цыфру'))
# name = str(input('ведите имя'))
# num2 = float(input('ведите дробную чеслу'))
# tf = bool(input('ведите правда или лож'))

# print('здравствуйте завершите регистацюю')
# name = str(input('ведите имя '))
# surname = str(input('ведите фаитлию '))
# phonenum = int(input('ведите номер '))
# email = str(input('ведите имейл '))
# print('вы успешно завершили регистрацию ')


# age  = int (input("ВВедите возраст  "))
# if age < 18:
#     print('Вы не проходите ')

# else:
#     print('вы проходите')



     
# try:

#     dollars = float(input('введите сумму в долларах'))
#     if dollars <= 0:
#         print('у вас отрицательное сумма')

#     else:
#         som = 87.50
#         som = dollars * som
#         print(f'сумма в сом , {som:.2f}')

# except ValueError:
#     print('не правильно ввод данных')

# try: 
#     num = int(input('введите сумму заказа '))

#     if num < 1000:
#         num2 = 200
#     elif num <= 0:
#         print('у вас отрицательное сумма товара')
#     elif num < 5000:
#         num2 = 100
#     else:
#         num2 = 0
#         print(f'стоимость доставки:{num2} рублей')
# except ValueError:
#     print('не коректный ввод данных')

# try:
#     num1 = int(input('введите первое число'))
#     num2 = int(input('введите второе число'))
#     num3 = int(input('введите третье число'))
#     num4 = (num1+num2+num3) /3
#     print('средние значение ', num4)
# except ValueError:
#     print('у вас не коректный ввод данных')

# try:
#     print(12/0)

# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# try:
#     num1 = int(input('введите первое число'))
#     num2 = int(input('введите второе число'))
#     value = input('выбирайте + - * /')
#     if value == '+':
#         print(num1+num2)
#     if value == '-':
#         print(num1-num2)
#     if value == '*':
#         print(num1*num2)
#     if value == '/':
#         print(num1/num2)
# except ValueError:
#     print('у вас не коректный ввод')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# def bank():
#     try:
#         balance = 5000
#         depozit = 0

#         choose = int(input('нажмите 1 что бы пополнить баланс \nнажниме 2 чтобы просмотреть баланс \nнажмите 3 чтобы открыть депозит \nнажмите 4 чтобы заказать карту \nнажмите 5 чтобы добавить ребенка \nнажмите  6 чтобы пройти регистрацию \nнажмите 7 чтобы перевести денги \nнажмите на 8 чтобы взять кредит'))
#         if choose == 1:
#             money = int(input('Введите сумму пополнения '))
#             print(f'ваш баланс теперь {money+balance}')
#         elif choose == 2:
#             print(f'ваш баланс {balance}')
#         elif choose == 3:
#             print(f'вы открыли депозит, ваш баланс {depozit}')
#         elif choose == 4:
#             num = str(input('введите номер'))
#             order = str(input('введите адрес'))
#             print('вы успешно заказали карту')
#         elif choose == 5:
#             son = str(input('введите данные ребенка'))
#             num = str(input('введите номер телефон ребенка'))
#             print('вы успешно добавили ребенка')
#         elif choose == 6:
#             name = str(input('введите имя'))
#             surname = str(input('введите фамилию'))
#             email = str(input('введите имейл'))
#             password = int(input('введите пороль'))
#             password2 = int(input('повторите пороль'))
#             if password == password2:
#                 print('зегистрация прошла успешно')
#             else:
#                 print('пороли не совпали')
#         elif choose == 7:
#             num1 = str(input('введите номер телефона')) 
#             money1 = int(input('введите сумму перевода'))
#             print(f'ваш баланс теперь {balance-money1}')  

#             balance = 5000
#         if choose == 8:
#             print(f'Ваш кредит состовляет 23% от текущего баланса это {balance/100*23} сом')
#             credit = int(input('выберите 1 если вы берёте кридит и 2 если нет '))
#             if credit == 1:
#                 print(f"вы получили кредит теперь ваш баланс {balance/100*23 + balance} сом ")
#             elif credit == 2:
#                 print('Вы отказались от кредита')
#             else:
#                 print('у вас не коректный ввод')
#         else:
#             print('Такой команды нет')     
 

#     except ValueError:
#         print('у вас не коректный ввод')
# bank()

# foods = 'лагман уйгурский , шаверма куринная, оливье, красный бархат, piko '   
# print(foods)

# foods = ['лагман уйгурский ','шаверма куриная','оливье',' красный бархат',' piko']
# print(foods[2])
# foods.append('shashlyk')
# print(foods)

# foods.clear()
# print(foods)

# foods.copy()
# print(foods)

# foods.pop(4)
# print(foods)

# foods.reverse()
# print(foods)

# num = [10,20,30,40,50,65,93,18,12,11]

# num.sort()
# print(num)

# try:

#     print('здраствуйте вы в ресторане kurbanoff')
#     choose = int(input('нажмите на 1 чтобы заказать суп \nнажмите на 2 чтобы заказать бургер \nнажмите на 3 чтобы заказать шаверму \nнажмите на 4 чтобы заказать шашлык \nнажмите на 5 чтобы заказать самсу \nнажмите на 6 чтобы заказать дисерт \nнажмите на 7 чтобы заказать напитки'))
#     if choose == 1:
#         menu = int(input('нажмите на 1 чтобы заказать пельмени 270 сом \nнажмите на 2 чтобы заказать борш 230 сом \nнажмите на 3 чтобы заказать 220 сом'))
#         if menu == 1:
#             print('ваши пельмени будет черес 15 минут')
#         elif menu == 2:
#             print('ваш борш будет через 12 минут')
#         elif menu == 3:
#             print('ваш лагман будет через 17 минут')
#     elif choose == 2:
#         menu1 = int(input('нажмите на 1 чтоба заказать мини бургер 90 сом \nнажмите на 2 что бы заказать куринный бургер 150 сом\nнажмите на 3 чтобы заказать гавяжий бургер 170 сом'))
#         if menu1 == 1:
#             print('ваши мини бургер будет черес 5 минут')
#         elif menu1 == 2:
#             print('ваш куринный бургер будет через 7 минут')
#         elif menu1 == 3:
#             print('ваш гавяжий бургер  будет через 7 минут')
#     elif choose == 3:
#         menu2= int(input('нажмите на 1 чтоба заказать куринную шаверму 210 сом сом \nнажмите на 2 что бы заказать запичённую шаверму 230 сом\nнажмите на 3 чтобы заказать гавяжую шаверму 200 сом'))
#         if menu2 == 1:
#             print('ваши куринную шаверму будет черес 10 минут')
#         elif menu2 == 2:
#             print('ваш запичённую шаверму будет через 8 минут')
#         elif menu2 == 3:
#             print('ваш гавяжую шаверму  будет через 6 минут')
#     if choose == 4:
#         menu3 = int(input('нажмите на 1 чтобы куринный шашлык 170 сом сом \nнажмите на 2 чтобы заказать гавяжий шашлык 130 сом сом \nнажмите на 3 чтобы заказать кебаб 70 сом сом'))
#         if menu3 == 1:
#             print('ваши курринный шашлык будет черес 20 минут')
#         elif menu3 == 2:
#             print('ваш гавяжий шашлык будет через 20 минут')
#         elif menu3 == 3:
#             print('ваш кебаб будет через 20 минут')
#     elif choose == 5:
#         menu4 = int(input('нажмите на 1 чтоба заказать самсу куринный 50 сом \nнажмите на 2 что бы заказать каплю самсу 70 сом\nнажмите на 3 чтобы заказать бальшую самсу 150 сом'))
#         if menu4 == 1:
#             print('ваш самса куринный будет черес 5 минут')
#         elif menu4 == 2:
#             print('ваш каплю самсу будет через 5 минут')
#         elif menu4 == 3:
#             print('ваш бальшую самсу будет через 5 минут')
#     elif choose == 6:
#         menu5 = int(input('нажмите на 1 чтоба заказать красный бархыт 70 сом\nнажмите на 2 что бы заказать напалион \nнажмите на 3 чтобы заказать медовик'))
#         if menu5 == 1:
#             print('ваш красный бархыт готов')
#         elif menu5 == 2:
#             print('ваш напалион готов')
#         elif menu5 == 3:
#             print('ваш медовик готов')
#     elif choose == 7:
#         menu6 = int(input('нажмите на 1 чтобы заказать пепси 0,5л 60 сом 1л 80 сом \nнажмите на 2 чтобы заказать фанту 0,5л 55 сом 1л 85 сом \nнажмите на 3 чтобы заказать колу 0,5л 65 сом 1л 90 сом'))
#         if menu6 == 1:
#             print('ваш напиток готов')
#         elif menu6 == 2:
#             print('ваш напиток готов')
#         elif menu6 == 3:
#             print('ваш напиток готов')
#         else:
#             print('накой не существует')
# except ValueError:
#     print('у вас некоректный ввод')
    


# def register():
#     try:
#         name = str(input('введите имя'))
#         surname = str(input('введите фамилию')) 
#         password_1 = int(input('введите пороль'))
#         password_2 = int(input('повторите пороль'))
#         if password_1 == password_2:
#             print('регистрация прошла успешно')
#         else:
#             print('повторите пороль')
#     except ValueError:
#         print('у вас некоректный ввод')

# register()

# for i in range(1,11):
#     print(i)


# word = 'python'
# for i in word:
#     print(i)



player = ['ronaldo', 'neymar', 'mbappe', 'nouer', 'maldini', 'nesta', 'cafu', 'butscens', 'zizu', 'kevin', 'ronaldinho', 'messi', 'pep']
print(player)



# from main import dollars