print('Task 10 - Objects')


class mitarbeiter:
    def __init__(self, id=0, name='no_name', hours=0):
        self.name = name
        self.id = id
        self.__hours = hours

    def __init__(self):
      self.__init__(0, 'no_name', 0)

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        if (hours < 0 or hours > 50):
            print("Die Arbeitsstunden müssen im Bereich 0-49 liegen")
        else:
            self.__hours = hours


m = mitarbeiter(1, "Max", 40)

print("Mitarbeiter: {} - {} - {}hours".format(m.id, m.name, m.getHours()))

m2 = mitarbeiter()
print("Mitarbeiter: {} - {} - {}hours".format(m2.id, m2.name, m2.getHours()))
