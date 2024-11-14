def calculate_discount(price, discount_percent):
    percentage = 0.2
    price = float(input("Enter price "))
    discount_percent = float(input("Enter the discount "))
    discount_percent = (discount_percent/percentage) * price
    final_cost = price - discount_percent
    
    if discount_percent >= percentage:
        return price * discount_percent
    else:
        return price

calculate_discount('price','discount_percent')
print("final_cost")







     
