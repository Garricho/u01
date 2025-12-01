import random

drivers_db = {}
pending_db = {}
approved_db = {}

admin_data = {
    "admin": "12345"
}

class Driver:
    def __init__(self):
        self.id = None
        self.password = None
        self.name = None
        self.surname = None
        self.age = None
        self.car = None
        self.is_approved = False

    def register(self):
        self.name = input("Ismingiz: ")
        self.surname = input("Familiyangiz: ")
        self.age = int(input("Yoshingiz: "))
        have_car = int(input("Mashina bormi? 1=Ha 2=Yoq: "))

        if have_car == 1:
            self.car = input("Mashina rusumi: ")
        else:
            self.car = input("Qanday mashina sotib olmoqchisiz: ")

        self.id = random.randint(10000, 99999)
        self.password = random.randint(1000, 9999)

        pending_db[self.id] = self
        print("\nRo‘yxatdan o‘tdingiz! Admin tasdiqlashi kerak!")
        print(f"ID: {self.id}\nParol: {self.password}")

    def login(self):
        a = int(input("ID kiriting: "))
        b = int(input("Parol kiriting: "))

        if a in approved_db:
            driver = approved_db[a]
            if driver.password == b:
                print(f"Xush kelibsiz, {driver.name}!")
            else:
                print("Xato parol!")
        elif a in pending_db:
            print("Hali admin tasdiqlamagan!")
        else:
            print("Bunday foydalanuvchi yo‘q!")


class Admin:
    def admin_login(self):
        log = input("Admin login: ")
        pas = input("Admin parol: ")

        if log in admin_data and admin_data[log] == pas:
            print("Admin paneliga xush kelibsiz!")
            self.menu()
        else:
            print("Xato ma'lumot!")

    def menu(self):
        while True:
            print("\n1. Kutayotgan haydovchilar")
            print("2. Chiqish")
            choice = input("Tanlang: ")

            if choice == "1":
                self.show_pending()
            else:
                break

    def show_pending(self):
        if not pending_db:
            print("Kutayotgan haydovchi yo‘q!")
            return

        for driver_id, driver in list(pending_db.items()):
            print(f"\n{driver_id} - {driver.name} {driver.surname} | Mashina: {driver.car}")
            approve = input("Tasdiqlansinmi? 1=Ha 2=Yo‘q: ")
            if approve == "1":
                approved_db[driver_id] = driver
                del pending_db[driver_id]
                print("Tasdiqlandi!")
            else:
                print("Rad etildi!")


admin = Admin()
user = Driver()