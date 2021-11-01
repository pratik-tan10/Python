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


binomial_label = Label("Binomial Distribution Confidence Interval Calculator")
binomial_confidence = FloatSlider(description="confidence", value=0.95, min=0.5, max=0.99, step=0.01)
binomial_phat = FloatSlider(description="p hat", value=0.78, min=0.0, max=1.0, step=0.01)
binomial_n_input = BoundedIntText(value=30, min=0, max=100000, step=1, description='n:', disabled=False)
binomial_button = Button(description="Calculate")
binomial_output = Output()
# Button click event handlers ...
def normal_button_on_click(b):
    ci = normal_distribution_ci(normal_confidence.value, normal_x_bar_input.value, normal_sigma_input.value, normal_n_input.value)
    
    normal_output.clear_output()
    with normal_output:
        print(f"The population mean lies between {ci[0]:.2f} and {ci[1]:.2f} with {normal_confidence.value:.0%} confidence")

def binomial_button_on_click(b):
    ci = binomial_distribution_ci(binomial_confidence.value, binomial_phat.value, binomial_n_input.value)
    
    binomial_output.clear_output()
    with binomial_output:
        print(f"The population mean lies between {ci[0]:.1%} and {ci[1]:.1%} with {binomial_confidence.value:.0%} confidence")

