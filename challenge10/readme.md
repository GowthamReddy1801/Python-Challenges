# Student Data Drift Analysis

## Overview
This project demonstrates how shallow copy and deep copy behave differently when applied to structured student data.

## Core Idea
- Shallow copy shares nested references with the original dataset.
- Deep copy creates a fully independent dataset.
- Changes applied to shallow copy may impact the original.

## Steps
1. Generate random student dataset.
2. Create shallow and deep copies.
3. Apply transformation logic using roll number.
4. Convert datasets into DataFrames.
5. Compute statistical metrics.
6. Measure drift between datasets.
7. Classify the level of change.

## Observations
- Shallow copy can unintentionally modify original data.
- Deep copy ensures data isolation.
- Drift value indicates how much data distribution changed.

## Output
- Displays all datasets in table format.
- Shows statistical values (mean, median, standard deviation).
- Provides drift measurement and classification.

## Roll Number Used
609
