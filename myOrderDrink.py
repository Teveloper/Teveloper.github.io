drink_list = ["커피", "홍차", "녹차"]
drink_price_list = [5000, 4000, 3000]
error_message = [
    "주문을 알아 듣지 못했습니다.",
    "최소 한 잔 이상을 주문해야 합니다.",
    "예측할 수 없는 오류 발생",
]

def askingOrder():
    typeOfDrink = input("커피, 홍차, 녹차가 있습니다. 마실 음료수를 입력하세요 : ")
        
    if not typeOfDrink in drink_list:
        return False, typeOfDrink

    return True, typeOfDrink

def askingNumberOfCups():
    numberOfCups = int(input("몇 잔 주문하시겠어요?"))
    
    return numberOfCups

def drinkOrderAndCalculate (typeOfDrink, numberOfCups):
    if not typeOfDrink in drink_list:
        print("예측할 수 없는 오류 발생")
        return False, 0
        
    index = drink_list.index(typeOfDrink)
    totalPrice = drink_price_list[index] * int(numberOfCups)
    
    return True, totalPrice

result, typeOfDrink = askingOrder()
error_message_type = 0

if result == True:
    numberOfCups = askingNumberOfCups()
    
    error_message_type = 1
    if numberOfCups > 0:
        result, totalPrice = drinkOrderAndCalculate(typeOfDrink, numberOfCups)
        
        error_message_type = 2
        if result == True:
            error_message_type = -1
            print("감사합니다. {}를 {}잔 드리겠습니다. 금액은 {} 원입니다.".format(typeOfDrink, numberOfCups, totalPrice))

if error_message_type != -1:
    print(error_message[error_message_type])
