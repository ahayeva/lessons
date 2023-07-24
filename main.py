import json
def add_money():
    # add money to acc
    user_id = int(input(":vvedit id korustuvacha: "))
    count = int(input("vvedit kilkist koshtiv"))
    #money = int(input("vvedit kilkist kodshtiv dlya zniattia"))
    for user in users:
        if user_id == user["id"]:
            user["balance"] += count
    print(users)
    #if money >= users["balance"]:
def withdraw_money():
    money = int(input("vvedit kilkist kodshtiv dlya zniattia"))
    for user in users:
        if money >= user["balance"]:
            print("nedostatnio kostiv")
        elif money <= user["balance"]:
            user["balance"] -= money
            print("operacia uspishna")
    print(user)
def transfer_money():
    trans = int(input("vvedit sumu dlia perekazu"))
    user_id = int(input(vvedit id korustuvacha  ))
    for user in users:

if __name__ == "__main__":
    with open("users.json","r", encoding="utf-8") as file:
        users = json.load(file)
        users = users['accounts']
        # print(users)

    add_money()
    withdraw_money()







