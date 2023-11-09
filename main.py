from bookshop import BookShop

def main():
    orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
               [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
               [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
               [4, ("8732", 7, 11.99), ("7733", 11,18.99), ("88112", 5, 39.95)] ]
               
    shop = BookShop()

    totalPrices = shop.method1(orders)

    print(totalPrices)

    minList = shop.method2(totalPrices)
    
    print(minList)

main()

#BIG OL BOOBS