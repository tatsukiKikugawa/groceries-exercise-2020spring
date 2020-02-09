# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


#
#PRODUCTS(PART1)
#

pro_count = len(products)
 
print("--------------")
print("THERE ARE " + str(pro_count) + " PRODUVTS.")
print("--------------")
 
 
def sort_by_name(any_product):
    return any_product["name"]
sorted_products = sorted(products, key=sort_by_name)
 
for my_product in sorted_products:  #p referring each item in the list of products.
    #price(my_product["name"])
    #price_usd = my_product["price"]
    price_usd = " ${0:.2f}".format(my_product["price"])
    print(f" + " + my_product["name"] + price_usd)    
#Dictionaries and string formatting from number

#
# Departments (Part2)
#
departments = []
for my_product in products:
    #print(my_product["department"])
    departments.append(my_product["department"])
    #if my_product["department"] not in departments:
    #    departments.append(my_product["department"])


unique_departments = list(set(departments))



department_count = len(unique_departments)

print("--------------")
print("THERE ARE " + str(department_count) + " DEPARTMENTS.")
print("--------------")

unique_departments.sort()

for my_department in unique_departments:
    matching_products_count = [my_product for my_product in products if my_product["department"] == my_department]
    matching_products_count = len(matching_products_count)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"
    print(" + " + my_department.title() + " (" + str(matching_products_count) + " " + label + ")")
#Filtering function