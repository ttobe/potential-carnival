import matplotlib.pyplot as plt

# RMSE values
rmse_values = [0.3561638925672421, 0.3537631034086701, 0.361455]

# Model names
model_names = ['Linear Regression', 'RandomForestRegressor', 'XGBRegressor']

# Create a figure and axes
fig, ax = plt.subplots()

# Set the bar width
bar_width = 0.3

# Create the bar plot
bars = ax.bar(model_names, rmse_values, width=bar_width, color=['blue', 'green', 'orange'])

# Add the values on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 4), ha='center', va='bottom')

# Set the y-axis label
ax.set_ylabel('RMSE')
ax.set_ylim(0,1 ,0.1)
# Set the title
ax.set_title('RMSE Comparison')

# Display the plot
plt.show()
