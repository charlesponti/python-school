
def some_thing():
    values = [1, 2, 3, 4]
    for val in values:
        yield val

gen1 = some_thing()
gen2 = some_thing()

# Print all values in iterable
for value in gen1:
    print(value)
