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
