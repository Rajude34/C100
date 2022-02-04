class Car(object):
    def __init__(self, model, color, age, company, topspeed):
        self.model = model
        self.color = color
        self.age = age
        self.company = company
        self.topspeed = topspeed

    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerated")

Mclaren = Car("Mclaren spider", "orange", 2, "Mclaren", 320)

MG = Car("Hector","Black", 1, "MG", 320)

print(Mclaren.color)
print(Mclaren.start())

print(MG.age)