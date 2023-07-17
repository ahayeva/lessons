import json
def helloworld():
    print ('helloworld')
def filterLetter(letter,data):
    filtered_arr =[]
    for item in data:
        title = item['title']
        if title[0].upper() == letter:
          filtered_arr.append(item)
    return filtered_arr

if __name__ == "__main__":
    with open("products(1).json", "r", encoding="utf-8") as file:
        products = json.load(file)
        print(filterLetter("F", products))
