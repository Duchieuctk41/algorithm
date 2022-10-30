from os import read


cars = [
    {"name": "default", "inventory": 0, "order": 0},
]

def addCar():
    name = ''
    inventory = 0
    name = input('nhap ten xe:')
    inventory = int(input('nhap ton kho:'))

    isHas = False
    for car in cars:
        if car["name"] == name:
            car["inventory"] += inventory
            isHas = True
            break
    if isHas == False:
       cars.append({"name":name,"inventory": inventory,"order": 0})

def sellCar():
    name = input('Nhap ten xe: ')
    order = int(input('Nhap so luong order: '))
    for car in cars:
        if car["name"] == name:
            car["order"] += order

def writeReport(cars):
    content = 'name    |   inventory   |   order'
    for car in cars:
        content += '\n'+car["name"] + "   |   "+ str(car["inventory"]) +"   |   "+ str(car["order"])

    f = open("file.txt", "w")
    f.write(content)
    f.close()

def readReport():
    f = open("file.txt", "r")
    print(f.read())
    f.close()

def run():
    inLoop = True
    while inLoop:
        try:
            print("===================begin index================")
            print("0. Thoat chuong trinh")
            print("1. Import car")
            print("2. Export car")
            print("3. Write report")
            print("4. Read report")
            print("===================end index================")

            choose = int(input())
            if choose == 0:
                inLoop = False
                print("===================bye================")
            elif choose == 1:
                addCar()
                writeReport(cars)
            elif choose == 2:
                sellCar()
                writeReport(cars)
            elif choose == 3:
                writeReport(cars)
            elif choose == 4:
                readReport()

        except ValueError:
            print('Giá trị truyền vào phải là số thực')
    


def main():
    run()

main()
