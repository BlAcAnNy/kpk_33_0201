from electronics_store import Smartphone, Laptop, TV

print('*' *25)
smartphone = Smartphone.import_from_file('smartphone.src')
[print(el) for el in smartphone]

print('*' *25)
laptop = Laptop.import_from_file('laptop.src')
[print(el) for el in laptop]

print('*' *25)
tv = TV.import_from_file('tv.src')
[print(el) for el in tv]