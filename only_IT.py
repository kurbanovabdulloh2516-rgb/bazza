# class Animals:
#     def __init__(self, independent, curious, loyal, playful, calm, cautious, wise, caring, strong, hardworking):
#         self.independent=independent
#         self.curious=curious
#         self.loyal=loyal
#         self.playful=playful
#         self.calm=calm
#         self.cautious=cautious
#         self.wise=wise
#         self.caring=caring
#         self.strong=strong
#         self.hardworking=hardworking
#     def info_cat(self):
#         print(f'кошка очень - {self.independent}')
#         print(f'а ещё - {self.curious}')
#     def info_dog(self):
#         print(f'собака очень - {self.loyal}')
#         print(f'и ещё любит - {self.playful}')
#     def info_giraffe(self):
#         print('жираф он очень - {self.calm}')
#         print(f'и ещё - {self.cautious}')
#     def info_elephant(self):
#         print(f'слон очень - {self.wise}')
#         print(f'и ещё - {self.caring}')
#     def info_horse(self):
#         print(f'лошадь очень - {self.strong}')
#         print(f'и ещё - {self.hardworking}')
# zoo = Animals('независимый', 'любопытный', 'верный', 'игривый', 'спокойный', 'осторожный', 'мудрый', 'заботливый', 'сильная', 'трудлюбивая')
# zoo.info_cat()
# zoo.info_dog()
# zoo.info_giraffe()
# zoo.info_elephant()
# zoo.info_horse()


# class Shark(Animals):
#     def __init__(self, independent, curious, loyal, playful, calm, cautious, wise, caring, strong, hardworking, stupid):
#         super().__init__(independent, curious, loyal, playful, calm, cautious, wise, caring, strong, hardworking)
#         self.stupid=stupid
#     def info(self):
#         print(f'кошка очень - {self.independent} \nа ещё - {self.curious} \nсобака очень - {self.loyal} \nи ещё любит - {self.playful} \nжираф он очень - {self.calm} \nи ещё - {self.cautious} \nи ещё - {self.cautious} \nслон очень - {self.wise} \nи ещё - {self.caring} \nлошадь очень - {self.strong} \nи ещё - {self.hardworking} \nтолько рыба - {self.stupid}')
# zoo = Shark('независимый', 'любопытный', 'верный', 'игривый', 'спокойный', 'осторожный', 'мудрый', 'заботливый', 'сильная', 'трудлюбивая', 'тупой')
# zoo.info()



import turtle

square = turtle.Turtle()
square.shape("turtle")
square.color('red', 'green')
square.begin_fill()
for j in range(3):
    square.left(20)
    for i in range(4):
        square.forward(100)
        square.left(90)

square.end_fill()
turtle.exitonclick()
