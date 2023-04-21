print('Task 10 - Objects')


class mitarbeiter:
    def __init__(self, name='no_name', id=0, hours=0):
        self.name = name
        self.id = id
        self.__hours = hours    

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        if (hours < 0 or hours > 50):
            print("Die Arbeitsstunden müssen im Bereich 0-49 liegen: {}" .format(hours))
        else:
            self.__hours = hours

ma1 = mitarbeiter('Max Mustermann', 98738, 40)
ma2 = mitarbeiter('Bruno Mustermann', 24512, 35)

print("Mitarbeiter {} hat die id {} und arbeitet {} Stunden die Woche." .format(ma1.name, ma1.id, ma1.getHours()))
print("Mitarbeiter {} hat die id {} und arbeitet {} Stunden die Woche." .format(ma2.name, ma2.id, ma2.getHours()))

ma1.setHours(-1)
ma1.setHours(51)
ma1.setHours(35)
print("Mitarbeiter {} hat die id {} und arbeitet {} Stunden die Woche." .format(ma1.name, ma1.id, ma1.getHours()))