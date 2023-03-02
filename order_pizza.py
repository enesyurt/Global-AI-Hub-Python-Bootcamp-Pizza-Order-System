# Gerekli kütüphaneleri import edelim.
import csv
import datetime
     
# Pizza classını superclass olarak tanımlayalım.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
     
# Pizza classının pizza çeşitlerine göre subclasslarını tanımlayalım.
class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic pizza", 10.0)

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita pizza", 12.0)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish pizza", 15.0)

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain pizza", 8.0)
     
# Decorator classını tüm sos çeşitlerine sueprclass olacak şekilde tanımlayalım. 
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
    
    def get_description(self):
        return self.pizza.get_description()
    
    def get_cost(self):
        return self.pizza.get_cost()
     
# Her sos tipi için subclassları tanımlayalım.
class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2.0
        self.description = "Olives"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 1.5
        self.description = "Mushrooms"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 3.0
        self.description = "Goat cheese"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2.5
        self.description = "Meat"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 1.0
        self.description = "Onions"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 1.5
        self.description = "Corn"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost
    
# Pizza sipariş sistemi için main fonksiyonu tanımlayalım.
def main():
    # Menu.txt dosyasından menüyü okuyalım ve ekrana bastıralım.
    with open("Menu.txt", "r") as f:
        print(f.read())

    # Kullanıcıdan pizza seçmesi için girdi alalım.
    pizza_type = input("Please choose a pizza base (enter the number): ")
    pizza_type = int(pizza_type)

    # Seçilen pizza tipine göre instance oluşturalım.
    if pizza_type == 1:
        pizza = Classic()
    elif pizza_type == 2:
        pizza = Margherita()
    elif pizza_type == 3:
        pizza = TurkPizza()
    elif pizza_type == 4:
        pizza = PlainPizza()
    else:
        print("Invalid choice.")
        return

    # Kullanıcıdan sos tipi seçmesi için girdi alalım.
    sauce_type = input("Please choose a sauce (enter the number): ")
    sauce_type = int(sauce_type)

    # Seçilen sosu pizzaya ekleyelim.
    if sauce_type == 11:
        pizza = Olives(pizza)
    elif sauce_type == 12:
        pizza = Mushrooms(pizza)
    elif sauce_type == 13:
        pizza = GoatCheese(pizza)
    elif sauce_type == 14:
        pizza = Meat(pizza)
    elif sauce_type == 15:
        pizza = Onions(pizza)
    elif sauce_type == 16:
        pizza = Corn(pizza)
    else:
        print("Invalid choice.")
        return

    # Seçilen pizzanın toplam maliyetini alalım.
    total_cost = pizza.get_cost()

    # Dictionaryde depolamak üzere kullanıcıdan bilgilerini girdi olarak alalım.
    user_info = {}
    user_info["name"] = input("Enter your name: ")
    user_info["id"] = input("Enter your ID number: ")
    user_info["credit_card_number"] = input("Enter your credit card number: ")
    user_info["credit_card_password"] = input("Enter your credit card password: ")
    user_info["description"] = pizza.get_description()

    # Siparişi veritabanına kaydedelim.
    with open("Orders_Database.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([user_info["name"], user_info["id"], user_info["credit_card_number"],
                        user_info["credit_card_password"], user_info["description"], datetime.datetime.now()])

    # Sipariş fişini bastıralım.
    print("Thank you for your order! Here is your receipt:")
    print(f"Name: {user_info['name']}")
    print(f"ID Number: {user_info['id']}")
    print(f"Credit Card Number: {user_info['credit_card_number']}")
    print(f"Description of Order: {user_info['description']}")
    print(f"Total Cost: {total_cost}")
     
# main fonksiyonu çalıştıralım.
if __name__ == "__main__":
    main()
     