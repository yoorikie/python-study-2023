print("Яблок в корзине:")
apples = int(input())


print("Школьников:")
children = int(input())

count = apples // children
left = apples % children
left2 = apples - children * count 


print(f"Каждому школьнику:{count}")
print(f"осталось в корзине:{left2}")
