
def hisobla(a, b, belgi):
    if belgi == "+":
        return a + b
    elif belgi == "-":
        return a - b
    elif belgi == "*":
        return a * b
    elif belgi == "/":
        if b == 0:
            return "0 ga bo'lish mumkin emas"
        return a / b
    else:
        return "Noto'g'ri amal tanlandi!"

def main():
    print("~~Mini Calculator~~")

    while True:
        try:
            son1 = float(input("1-sonni kiriting:"))
            son2 = float(input("2-sonni kiriting: "))
            belgi = input("Amalni tanlang (+, -, *, /): ")

            natija = hisobla(son1, son2, belgi)
            print(f"Natija: {natija:g}")


        except ValueError:
            print("Iltimos, faqat son kiriting!")

        davom = input("Yana hisoblashni xohlaysizmi? (ha/yo'q): ").lower()
        if davom != "ha":
            print("Dastur yakunlandi.")
            break


if __name__ == "__main__":
    main()
