import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

normal_data = np.random.randn(10, 12)
ax = sns.heatmap(normal_data, center=0)

sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips);
sns.relplot(x="total_bill", y="tip", hue="size", data=tips);
sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips);
sns.relplot(x="total_bill", y="tip", size="size", data=tips);
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips);
df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.figure.autofmt_xdate()
df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
sns.relplot(x="x", y="y", sort=False, kind="line", data=df);
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri);

sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);
sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            dashes=False, markers=True, kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            kind="line", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="region",
            units="subject", estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));
dots = sns.load_dataset("dots").query("align == 'dots'")
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            kind="line", data=dots);
palette = sns.cubehelix_palette(light=.8, n_colors=6)
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            palette=palette,
            kind="line", data=dots);
