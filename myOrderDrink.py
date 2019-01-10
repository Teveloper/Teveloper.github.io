def askingOrder():
    typeOfDrink = input("커피, 홍차, 녹차가 있습니다. 마실 음료수를 입력하세요 : ")
        
    if typeOfDrink == "커피" or typeOfDrink == "홍차" or typeOfDrink == "녹차":
        askingNumberOfCups(typeOfDrink)
    else:
        print("주문을 알아듣지 못했습니다.")
        askingOrder()

def askingNumberOfCups(typeOfDrink):
    numberOfCups = input("몇 잔 주문하시겠어요?")

    try:
        print("감사합니다. ", typeOfDrink, "를 ", int(numberOfCups), "잔 드리겠습니다.")
        drinkOrderAndCalculate(typeOfDrink, numberOfCups)
    except ValueError:
        print("정수가 아닙니다.")
        askingNumberOfCups(typeOfDrink)

def drinkOrderAndCalculate (typeOfDrink, numberOfCups):
    priceCoffee = 5000
    priceGreenTea = 4000
    priceRedTea = 3000
    
    if typeOfDrink == "커피":
        totalPrice = int(priceCoffee) * int(numberOfCups)
    elif typeOfDrink == "홍차":
        totalPrice = int(priceGreenTea) * int(numberOfCups)
    elif typeOfDrink == "녹차":
        totalPrice = int(priceRedTea) * int(numberOfCups)
    else:
        print("예측할 수 없는 오류 발생")
    
    print(typeOfDrink, numberOfCups, "잔 드리겠습니다. 금액은 ", totalPrice, "원입니다.")

askingOrder()
