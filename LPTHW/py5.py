name = 'Zed A. shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches = 1
cms = 2.54*inches
pound = 1
kilogram = 0.454*pound

print(f"Let's talk about {name}.")
print(f"He's {round(height*cms)} cm tall.")
print(f"He's {round(weight*kilogram)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

total = age + height + weight
print(f"If I add {age},{height},and {weight} I get {total}.")
