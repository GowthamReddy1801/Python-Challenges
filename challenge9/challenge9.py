import copy

def build_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 52000, "stock": 12, "supplier": {"rating": 4.6}}
        },
        {
            "item": "Phone",
            "details": {"price": 21000, "stock": 30, "supplier": {"rating": 4.3}}
        }
    ]

def update_inventory(data, roll):
    pos = (roll + 1) % len(data)

    for idx, val in enumerate(data):
        if idx == pos:
            val["details"]["price"] = int(val["details"]["price"] * 0.85)
            val["details"]["stock"] -= 3

def evaluate_changes(base, new):
    diff = 0
    same = 0

    for i in range(len(base)):
        if base[i] != new[i]:
            diff += 1
        else:
            same += 1

    return diff, same

def explain(original, shallow, deep):
    print("\nAnalysis:")

    if original == shallow:
        print("Shallow copy modified original due to shared nested references.")
    else:
        print("Shallow copy did not impact original.")

    if original != deep:
        print("Deep copy stayed independent.")
    else:
        print("Deep copy behaved unexpectedly.")

roll_number = 609

original = build_inventory()
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

update_inventory(shallow_copy, roll_number)
update_inventory(deep_copy, roll_number)

print("Original:", original)
print("\nShallow Copy:", shallow_copy)
print("\nDeep Copy:", deep_copy)

print("\nComparison:")
print("Shallow:", evaluate_changes(original, shallow_copy))
print("Deep:", evaluate_changes(original, deep_copy))

explain(original, shallow_copy, deep_copy)

shallow_result = evaluate_changes(original, shallow_copy)
deep_result = evaluate_changes(original, deep_copy)

print("\nSummary:")
print("Shallow:", shallow_result)
print("Deep:", deep_result)

print("\nFinal Original:", original)
print("\nTuple summary:")
print("Shallow Result (changed_items_count, unchanged_items_count):", shallow_result)
print("Deep Result (changed_items_count, unchanged_items_count):", deep_result)

