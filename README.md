# A/B Testing Statistical Decision Engine

A small statistical engine that evaluates whether a product change leads to a **statistically significant improvement** using A/B testing.

This project demonstrates **inferential statistics concepts used in real-world experimentation systems**.

---

## Problem

Companies frequently run **A/B experiments** to test whether a new feature improves a metric such as:

* Conversion rate
* Click-through rate
* Signup rate
* Purchase probability

Observed differences may occur due to **random variation**.
This engine determines whether the improvement is **statistically significant**.

---

## Example Scenario

| Group                   | Users | Conversion Rate |
| ----------------------- | ----- | --------------- |
| Control (Old Version)   | 1000  | ~10%            |
| Treatment (New Version) | 1000  | ~13%            |

Observed improvement: **+3.1%**

The statistical engine evaluates whether this improvement is **real or due to noise**.

---

## Statistical Pipeline

The system performs:

1. Experiment simulation
2. Mean conversion calculation
3. Standard deviation estimation
4. Standard error computation
5. Two-sample t-test
6. p-value calculation
7. Confidence interval estimation
8. Statistical decision

Decision rule:

```
If p-value < 0.05 → Reject H0
Else → Fail to reject H0
```

---

## Project Structure

```
ab-testing-stat-engine
│
├── notebooks/
│   └── ab_testing.ipynb
│
├── src/
│   └── ab_test_engine.py
│
├── data/
│
└── README.md
```

### src/

Contains the reusable statistical engine:

```
run_ab_test()
simulate_experiment()
```

### notebooks/

Demonstrates how to run the experiment and visualize results.

---

## Example Output

```
A/B TEST SUMMARY
----------------------
Control conversion rate: 0.100
Treatment conversion rate: 0.131

Difference: 0.031

t-statistic: 2.170
p-value: 0.0301

Control CI: (0.081, 0.118)
Treatment CI: (0.110, 0.151)

Decision: Reject H0 (Significant difference)
```

---

## Visualization

The notebook also visualizes conversion rates with **95% confidence intervals**.

---

## Tech Stack

* Python
* NumPy
* SciPy
* Matplotlib
* Jupyter

---

## Concepts Demonstrated

* A/B Testing
* Hypothesis Testing
* t-statistic
* p-value
* Confidence Intervals
* Inferential Statistics

---

## Author

Ashish Pise