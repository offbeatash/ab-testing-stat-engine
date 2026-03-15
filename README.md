# A/B Testing Statistical Decision Engine

A small statistical engine that simulates an A/B experiment and determines whether a product change leads to a **statistically significant improvement**.

This project demonstrates core **inferential statistics concepts used in real-world experimentation systems**.

---

## Problem

Companies frequently run **A/B experiments** to test whether a new feature improves a metric such as:

* Conversion rate
* Click-through rate
* Purchase probability
* Signup rate

However, observed differences may occur due to **random variation**.

This project implements a statistical workflow that answers:

**"Is the observed improvement statistically significant?"**

---

## Example Scenario

| Group                   | Users | Conversion Rate |
| ----------------------- | ----- | --------------- |
| Control (Old Version)   | 1000  | 10%             |
| Treatment (New Version) | 1000  | 13%             |

Observed improvement: **+3.1%**

The system determines whether this difference is **real or random noise**.

---

## Statistical Pipeline

The notebook performs the following steps:

1. Simulate experiment data
2. Compute descriptive statistics
3. Estimate uncertainty using standard error
4. Compute pooled standard error
5. Calculate t-statistic
6. Compute p-value
7. Make statistical decision

---

## Mathematical Formulation

Difference in means:

[
\Delta = \bar{x}*{treatment} - \bar{x}*{control}
]

Pooled standard error:

[
SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
]

t-statistic:

[
t = \frac{\Delta}{SE}
]

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
│
├── data/
│
└── README.md
```

---

## Key Concepts Demonstrated

* Inferential Statistics
* Hypothesis Testing
* A/B Testing
* Standard Error
* t-statistic
* p-value interpretation
* Statistical decision making

---

## Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* SciPy

---

## Future Improvements

* Confidence intervals for conversion rates
* Visualization dashboard
* Automated experiment simulator
* Bayesian A/B testing comparison

---

## Author

Ashish Pise
