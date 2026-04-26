import random
import copy
import numpy as np
import pandas as pd
import math
def create_dataset():
    total = 12
    records = []
    for i in range(total):
        records.append({
            "id": i + 1,
            "marks": random.randint(45, 100),
            "attendance": random.randint(65, 100),
            "scores": [random.randint(12, 28), random.randint(12, 28)]
        })
    return records

def transform_data(data, roll):
    divisor = max(1, roll % 3) 
    for idx, item in enumerate(data):
        if idx % divisor == 0:
            marks = item["marks"]
            item["marks"] = int(marks + math.sqrt(marks))
            item["scores"][0] += 5
            item["scores"][1] += 4
            item["attendance"] -= 2

def compute_metrics(data):
    values = [x["marks"] for x in data]
    avg = np.mean(values)
    med = np.median(values)
    deviation = np.std(values)
    basic_avg = sum(values) / len(values)
    return avg, med, deviation, basic_avg

def calculate_shift(base, changed):
    base_avg = np.mean([x["marks"] for x in base])
    changed_avg = np.mean([x["marks"] for x in changed])
    return abs(base_avg - changed_avg)

def evaluate_status(shift, limit, base, shallow):
    if base != shallow:
        return "Copy Failure Detected"
    elif shift < limit:
        return "Stable Data"
    elif shift < limit * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll_number = 609
original = create_dataset()
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
transform_data(shallow_copy, roll_number)
transform_data(deep_copy, roll_number)
df_original = pd.DataFrame(original)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)
avg, med, std, basic_avg = compute_metrics(original)
shift = calculate_shift(original, deep_copy)
limit = 6
status = evaluate_status(shift, limit, original, shallow_copy)

print("\nOriginal:\n", df_original)
print("\nShallow:\n", df_shallow)
print("\nDeep:\n", df_deep)
print("\nShift:", shift)
print("\nTuple (avg, shift, std):")
print((avg, shift, std))
print("\nManual Average:", basic_avg)
print("\nStatus:", status)
