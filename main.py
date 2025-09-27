# def dollars():

#     try:

#         choose = int(input('нажмите на 1 что бы записать результат теста \nнажмите на 2 что бы записать результат диктанта \nнажмите на 3 что бы написать балл C/W \nнажмите на 4 что бы записать балл H/W \nнажмите на 5 что бы записать сколько страниц сдал \nнажмите на 6 что бы записатьсколько раз он пришел'))
#         if choose == 1:
#             mark = int(input('напишите результат'))
#             if mark < 0 or mark > 100:
#                 print('Ошибка мах 100 мин 0')
#             elif mark == 100 or 99 or 98 or 97 or 96:
#                 print('150$')
#             elif mark == 95 or 94 or 93:
#                 print('100$')
#             elif mark == 92 or 91 or 90:
#                 print('50$')
#             else:
#                 print('0$')
#         if choose == 2:
#             mark = int(input('напишите результат диктанта только пронцентам'))
#             if mark < 0 or mark > 100:
#                 print('Ошибка мах 100 мин 0')
#             elif mark == 100:
#                 print('150$')
#             elif mark >= 95:
#                 print('100$')
#             elif mark >= 92:
#                 print('50$')
#             else:
#                 print('0$')
#         elif choose == 3:
#             mark = int(input('напишите балл C/W'))
#             if mark < 0 or mark > 4:
#                 print('Ошибка мах 4 мин 0')
#             elif mark == 4:
#                 print('10$')
#             else:
#                 print('0$')
#         elif choose == 4:
#             mark = int(input('напишите балл H/W'))
#             if mark < 0 or mark > 4:
#                 print('Ошибка мах 4 мин 0')
#             elif mark == 4:
#                 print('10$')
#             else:
#                 print('0$')
#         elif choose == 5:
#             mark = int(input('сколько страниц сдал'))
#             if mark < 0 or mark > 10:
#                 print('Ошибка мах 10 мин 0')
#             elif mark == 10:
#                 print('30$')
#             elif mark == 5:
#                 print('20$')
#             elif mark == 3:
#                 print('10$')
#             elif mark == 15:
#                 print('40$')
#             elif mark == 20:
#                 print('50$')
#             elif mark == 30:
#                 print('70$')
#             elif mark == 40:
#                 print('100$')
#             else:
#                 print('0$')
#         elif choose == 6:
#             mark = int(input('сколько раз пришёл'))
#             if mark < 0 or mark > 24:
#                 print('Ошибка мах 24 мин 0')
#             elif mark == 24:
#                 print('50$')  
#             else:
#                 print('0$')
#         else:
#             print('такой команды нет')               
#     except ValueError:
#         print('у вас некоректнный ввод')
# dollars()
# try:

#     name = str(input('введите имя'))
#     surname = str(input('введите фамилию'))
#     name_surname = name + '' + surname
#     login = str(input('введите логин'))

#     print(f'вы зашли на 5 курс {name_surname}')

#     choose = int(input('нажмите на 1 что бы открыть C/W \nнажмите на 2 что бы открыть H/W \nнажмите на 3 что бы открыть progrest test \nнажмите на 4 что бы открыть Dictation \nнажмите на 5 что бы открыть Reading \nнажмите на 6 что бы открыть общий балл' ))
#     if choose == 1:
#         print('30.07.2025 4 балла')
#         print('1.08.2025 4 балла')
#         print('4.08.2025 4 балла')
#         print('6.08.2025 4 балла')
#         print('8.08.2025 4 балла')
#         print('11.08.2025 4 балла')
#         print('13.08.2025 4 балла')
#         print('15.08.2025 4 балла')
#         print('18.08.2025 4 балла')
#         print('20.08.2025 4 балла')
#         print('22.08.2025 4 балла')
#         print('25.08.2025 4 балла')
#     if choose == 2:
#         print('30.07.2025 4 балла')
#         print('1.08.2025 4 балла')
#         print('4.08.2025 2 балла')
#         print('6.08.2025 4 балла')
#         print('8.08.2025 3 балла')
#         print('11.08.2025 4 балла')
#         print('13.08.2025 4 балла')
#         print('15.08.2025 2 балла')
#         print('18.08.2025 4 балла')
#         print('20.08.2025 1 балла')
#         print('22.08.2025 4 балла')
#         print('25.08.2025 3 балла')
#     if choose == 3:
#         print('100%')
#         print('87%')
#         print('90%')
#         print('56%')
#         print('74%')
#     if choose == 4:
#         print('92%')
#         print('72%')
#         print('50%')
#         print('68%')
#         print('82%')
#     if choose == 5:
#         print('сдал 40/40')
#     if choose == 6:
#         print('C/W 43/43 балл')
#         print('H/W 39/43 балл')
#         print('P.T 27/33')
#         print('DIC 24/33')
#         print('R 33/33')
#         print('Transfer 90 балл')
#     else:
#         print('такой команды нет')
# except ValueError:
#     print('у вас не коректный ввод')