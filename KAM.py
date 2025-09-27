class Foodball:
    def __init__(self, portugal, argintina, brazil, france, england, spain, germany):
        self.portugal=portugal
        self.argintina=argintina
        self.brazil=brazil
        self.frace=france
        self.england=england
        self.spain=spain
        self.germany=germany
    def info(self):
        print(f'рональду - {self.portugal}, \nмесси - {self.argintina}, \nрональдинио - {self.brazil}, \nзидан - {self.frace}, \nрунии - {self.england}, \nинеста - {self.spain}, \nмулллер - {self.germany}')
country = Foodball('португалия', 'аргентиния', 'бразилия', 'франция', 'англия', 'испания', 'гермфния')
country.info()          