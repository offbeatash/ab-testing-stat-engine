import numpy as np
from scipy import stats

def run_ab_test(control, treatment, alpha=0.05):

    n1 = len(control)
    n2 = len(treatment)

    mean1 = np.mean(control)
    mean2 = np.mean(treatment)

    std1 = np.std(control, ddof=1)
    std2 = np.std(treatment, ddof=1)

    se1 = std1 / np.sqrt(n1)
    se2 = std2 / np.sqrt(n2)

    pooled_se = np.sqrt((std1**2 / n1) + (std2**2 / n2))

    diff = mean2 - mean1
    t_stat = diff / pooled_se

    df = n1 + n2 - 2
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

    z = stats.norm.ppf(0.975)

    control_ci = (mean1 - z * se1, mean1 + z * se1)
    treatment_ci = (mean2 - z * se2, mean2 + z * se2)

    decision = "Reject H0 (Significant difference)" if p_value < alpha else "Fail to reject H0"

    return {
        "control_mean": mean1,
        "treatment_mean": mean2,
        "difference": diff,
        "t_statistic": t_stat,
        "p_value": p_value,
        "control_ci": control_ci,
        "treatment_ci": treatment_ci,
        "decision": decision
    }

def simulate_experiment(n_users, control_rate, treatment_rate, seed=42):
    import numpy as np
    np.random.seed(seed)

    control = np.random.binomial(1, control_rate, n_users)
    treatment = np.random.binomial(1, treatment_rate, n_users)

    return control, treatment