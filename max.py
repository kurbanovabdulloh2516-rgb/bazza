oop = 'обектна оринтеривонная праграммировение'
'инкопсулятсия это зашита данных в классах она имеет 3 формы(1.форма это побличное это когда у отрибута или функции обычное состояние) (2.форма это защишённая она отличается тем что перед нозванием методам или отрибута ставится 1 _  тем самом делая себя защищёным его можно вызват или обратится к ниму в не класса но это не жилательно)(3. форма это приватнная форма она обозначается уже 2 _  перед названием метода или отрибута  в отличи от защищённого его нельзя вызвать или исползывать в не класса не каким оброзом'
'полимарфизм это один из 4 терминов обектно оринтереного прогромирование блогодаря которуму производится действия одного и того же метода в разных классах с разным ответом  '
'наследование это один из 4 принципов обектно оринтеривонная праграммировение блогодоря которому производится наследование отрибуты класса и метода класса дочерним классам от родительсково  '
'опстраксия это один из 4 принципов ооп его некоторые прогромисты все ещё не считает одним из основных принципов ооп он опридиляется по значениям клаассов и опстрактным '
'значения опстракции это обобщённая понятие и значение чего-либо '
# class Car:
#     def __init__(self, motor, brand, color, model):
#         self.motor=motor
#         self.brand=brand
#         self.color=color
#         self.model=model

#     def info(self):
#         print(f'мотор автомобилья  - {self.motor} \nбренд автомобиля - {self.brand} \n свет автомобиля - {self.color} \nмодель автомобиля - {self.model}')

# bmw = Car('V12','bmw', 'белый', 'm5')
# bmw.info()

# # class Player:
#     def __init__(self, skill, dribbling, speed, shood):
#         self.skill=skill
#         self._dribbling=dribbling
#         self.speed=speed
#         self.__shood=shood

#     def info(self):
#         print(f'футбольный скил - {self.skill} \nфутбольный дриблинг - {self._dribbling} \nфутбольный скорасть - {self.speed} \nфутбольный удар - {self.__shood} ')

# football = Player('рональдиньё', 'месси', 'мбаппе', 'РОНАЛЬДО')
# football.info()
# print(football.__shood)
# print(football.speed)
# print(football._dribbling)

# class Bravel:
#     def __init__(self, rare, superare, epic, mythical, legendary):
#         self.__rare=rare
#         self.superare=superare
#         self.epic=epic
#         self.mythical=mythical
#         self._legendary=legendary

#     def info(self):
#             print(f'редкий - {self.__rare} \nсверхредкий - {self.superare} \nэпик - {self.epic} \nмифик - {self.mythical} \nлегендарный - {self._legendary}')
# stars = Bravel('поко и примо', 'карл', 'эдгар', 'мортис', 'леон')
# stars.info()
# # print(stars.__rare)
# print(stars._legendary)

# print('кому вы хотите позвонить')

# class Poeple:
#     def __init__(self, ali, umar, max, muhammadior, abdullokh, zuba, aziz, nub):
#         self.ali=ali
#         self.umar=umar
#         self.max=max
#         self.muhammadior=muhammadior
#         self._abdullokh=abdullokh
#         self.zuba=zuba
#         self.aziz=aziz
#         self.__nub=nub
#     def info(self):
#         print(f'Орлов али - {self.ali} \nСоколов умар - {self.umar} \nРоманов макс - {self.max} \nВласов мухаммадиёр - {self.muhammadior} \nКурбанов Абдуллох - {self._abdullokh} \nКалорёв зуба - {self.zuba} \nПанов нуб - {self.__nub}')
# num = Poeple('0552324453', '0555372837', '0999999999', '0834651234', '0550011011', '0537882732', '0555637486', '0990354727')
# num.info()
# print(num._abdullokh)
# print('Курбанов Абдуллох')
# print(num.__nub)

# class Valuta:
#     def __init__(self, dollars, evro, sum, rub, tenge,):
#         self._dollars=dollars
#         self.evro=evro
#         self.__sum=sum
#         self.rub=rub
#         self.tenge=tenge
#     def info(self):
#         print(f'доллар - {self._dollars} \nевро - {self.evro} \nсум - {self.__sum} \nрубль - {self.rub} \nтенге - {self.tenge}')
# som = Valuta('87.50', '101.64', '0.0070', '1.08', '0.16')
# som.info()
# print('защишено')
# print(som._dollars)
# # print('запришено')
# print(som.__sum)


# class Hero:
#     def __init__(self, super_speed, super_kick, invisibility, doest_feel_the_blow, lightning, flying, elastic, stop_time,smart,ant):
#         self.super_speed=super_speed
#         self.super_kick=super_kick
#         self.invisibility=invisibility
#         self.doest_feel_the_blow=doest_feel_the_blow
#         self.lightning=lightning
#         self.flying=flying
#         self.elastic=elastic
#         self.stop_time=stop_time
#         self.smart=smart
#         self.ant=ant
#     def info_flash(self):
#         print(f'у флеша суперспособность - {self.super_speed}')
#         print(f'и ещё имеется - {self.stop_time}')
#     def info_khalk(self):
#         print(f'у халка суперспособность - {self.super_kick}')
#         print(f'и ещё - {self.doest_feel_the_blow}')
#     def info_Tor(self):
#         print(f'у тора суперспособность - {self.lightning}')
#         print(f'и ещё - {self.flying}')
#     def info_ant(self):
#         print(f'у муравея суперспособность - {self.ant}')
#         print(f'и ещё - {self.smart}')
#     def info_abdullokh(self):
#         print(f'у абдуллоха суперспособность - {self.invisibility}')
#         print(f'и ещё - {self.elastic} ')

# marvel = Hero('супер скорасть', 'супер удар', 'невидемость', 'не чуствает удар', 'молнии', 'летать', 'еластик', 'останавляет время', 'умный', 'уменшение или увилечение')
# marvel.info_flash()
# marvel.info_ant()
# marvel.info_abdullokh()
# marvel.info_khalk()
# marvel.info_Tor()





# name = 'abdulloh'
#   name = 'muhammaddior'
# print(name)

# class Bank:
#     def __init__(self, balance, deposit, order_card, add_child, register):
#         self.balance=50000
#         self.deposit=deposit
#         self.order_card=order_card
#         self.add_child=add_child
#         self.register=register
#     def info_balance(self):
#         print(f'Ваш баланс текуйший момент составляет - {self.balance}')
#     def info_deposit(self):
#         print(f'ваш депозит составляет 20% от баланса - {self.balance}/100*20')    
#     def info_order_card(self):
#         print(f'вы заказали карту,ваша доставка будет черес - {self.order_card}')
#     def info_add_child(self):
#         try:
#             choose = int(input('нажмите на 1 что бы добавить ребёнка'))
#             if choose ==1:
#                     name = str(input('введите имя ребёнка'))
#                     surname = str(input('введите фамилию'))
#                     num = int(input('введите телефон ребёнка'))
#                     print('вы добавили ребёнка')
#         except ValueError:
#             print('у вас не коректный ввод')            
#     def info_register(self):
#         try:
#             print('пройдите регистрация')
#             num = str(input('введите имя'))
#             num1 = str(input('введите фамилию'))
#             password = int(input('введите пороль'))
#             password2 = int(input('повторите пороль'))
#             if password == password2:
#                 print('зегистрация прошла успешно')
#             else:
#                 print('пороли не совпали')
#         except ValueError:
#              print('у вас не коректный ввод')
# max = Bank('баланс', 'депозит', '15 дней', 'добавить ребёнка', 'пройдите регистрацию')
# max.info_balance()
# max.info_deposit()
# max.info_order_card()
# max.info_add_child()
# max.info_register()

class Car:
    def __init__(self, motor, brand, color, model):
        self.motor=motor
        self.brand=brand
        self.color=color
        self.model=model
    def info(self):
        print(f'мотор автомобилья  - {self.motor} \nбренд автомобиля - {self.brand} \nсвет автомобиля - {self.color} \nмодель автомобиля - {self.model}')

bmw = Car('V12','bmw', 'белый', 'm5')
bmw.info()


class BMW(Car):
    def __init__(self, motor, brand, color, model,v12):
        super().__init__(motor, brand, color, model)
        self.v12=v12
    def info(self):
        print(f'мотор автомобилья  - {self.motor} \nбренд автомобиля - {self.brand} \nсвет автомобиля - {self.color} \nмодель автомобиля - {self.model} \nособаннасть моднеля - {self.v12}')

bmw = BMW('V6','bmw', 'белый', 'm5', 'v12')
bmw.info()
