#To display within the notebook
%matplotlib inline

#plot 0 - 9
plt.plot(range(10))

plt.plot(range(10), 'r--', markersize = 10, label = 'inc')
plt.legend()

plt.plot(range(1)[::-1], 'b*:', label = 'dec')
plt.plot([4.5]*10, 'gx-', label = 'fix')
plt.plot(range(10), 'ko-', label = 'ver')
plt.legend();
