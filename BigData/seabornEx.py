import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips);
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",
            data=tips);
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips);
sns.relplot(x="total_bill", y="tip", hue="size", data=tips);
sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips);
sns.relplot(x="total_bill", y="tip", size="size", data=tips);
