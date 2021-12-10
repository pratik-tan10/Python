import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

normal_data = np.random.randn(10, 12)
ax = sns.heatmap(normal_data, center=0)

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)

ax = sns.heatmap(flights, annot=True, fmt="d")
ax = sns.heatmap(flights, linewidths=.5)

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
