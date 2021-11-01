# Imports ...
from ipywidgets import Label, FloatSlider, FloatText, BoundedIntText, Button, Output, VBox, HBox

import scipy.stats as stats
import numpy as np

# Helpder functions to calculate the confidence intervals ...
def normal_distribution_ci(confidence, x_bar, sigma, n):
    z_score = stats.norm.interval(confidence)[1]
    sigma_over_root_n = sigma / np.sqrt(n)
    ci = [x_bar - z_score * sigma_over_root_n, x_bar + z_score * sigma_over_root_n]
    return ci

def binomial_distribution_ci(confidence, p_hat, n):
    z_score = stats.norm.interval(confidence)[1]
    rhs = z_score * np.sqrt(p_hat*(1-p_hat))/n
    ci = [p_hat - rhs, p_hat + rhs]
    return ci
# IPython widget controls for confidence intervals of normal and binomial distributions ...
normal_label = Label("Normal Distribution Confidence Interval Calculator")
normal_confidence = FloatSlider(description="confidence", value=0.95, min=0.5, max=0.99, step=0.01)
normal_x_bar_input = FloatText(value=75.7, min=0, max=100000, step=0.01, description='x bar:', disabled=False)
normal_sigma_input = FloatText(value=7.3, min=0, max=100000, step=1, description='sigma:', disabled=False)
normal_n_input = BoundedIntText(value=30, min=0, max=100000, step=1, description='n:', disabled=False)
normal_button = Button(description="Calculate")
normal_output = Output()

