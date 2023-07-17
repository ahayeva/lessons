import json
def CesarCode(txt,key= 3):
    with open("products(1).json","r") as file:
        product_data = json.load(file)
        code_in_number = []
        for letter in txt:
            for l in product_data:
                if product_data[f"{l}"] == letter.lower():
                    code_in_number.append(int(l)+int(key))
                    print(code_in_number)
                    code_word= ''
                    for num in code_in_number:
                        if num <= 26:
                         code_word += product_data[f"{num}"]
                    else:
                        code_word +=product_data[f"{num - 26}"]
                        return code_word.capitalize()
if __name__ == "__main__":
   enter_txt ="python"
   print(enter_txt)


