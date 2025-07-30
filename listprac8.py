keys = []
values = []

n = int(input("Enter the number of elements: "))

print("Enter elements for the keys:")
for i in range(n):
    key = input(f"Key {i+1}: ")
    keys.append(key)

print("Enter elements for the values:")
for i in range(n):
    value = input(f"Value {i+1}: ")
    values.append(value)

mapped_dict = dict(zip(keys, values))

print("\nMapped Dictionary:")
print(mapped_dict)
