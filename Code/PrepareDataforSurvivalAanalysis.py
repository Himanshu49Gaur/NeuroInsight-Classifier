import numpy as np
from lifelines import CoxPHFitter

print("Preparing data for survival analysis...")

X_surv = X_scaled.copy()
np.random.seed(42)
X_surv['duration'] = np.random.randint(1, 100, size=len(X_surv))  # simulated time-to-event
X_surv['event'] = y.values  # 1 = event occurred (e.g. sepsis), 0 = censored

print("Sample survival data:")
print(X_surv.head())

