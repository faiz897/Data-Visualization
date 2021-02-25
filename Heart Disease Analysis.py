import pandas as pd
import matplotlib.pyplot as plt

heart_disease = pd.read_csv("13.1 heart-disease.csv")
over_50 = heart_disease[heart_disease["age"] > 50]

plt.style.use("seaborn-whitegrid")
# create the plot from scratch
fig, (ax0, ax1) = plt.subplots(ncols=1,
                               nrows=2,
                               figsize=(10, 10),
                               sharex=True)

# putting the data into ax0
scatter0 = ax0.scatter(x=over_50["age"],
                       y=over_50["chol"],
                       c=over_50["target"],
                       cmap="winter")

# putting the data into ax1
scatter1 = ax1.scatter(x=over_50["age"],
                       y=over_50["thalach"],
                       c=over_50["target"],
                       cmap="winter")

# customize the figure
ax0.set(title="Heart disease and Cholesterol Level",
        ylabel="cholesterol",
        xlim=[50, 80])
ax1.set(title="Heart disease and Max Heart Rate",
        xlabel="Age",
        ylabel="Heart rate",
        xlim=[50, 80],
        ylim=[60, 200])

# add a legend
ax0.legend(*scatter0.legend_elements(), title="Target")
ax1.legend(*scatter1.legend_elements(), title="Target")

# create a horizontal line
ax0.axhline(over_50["chol"].mean(),
            linestyle="--", color="r")
ax1.axhline(over_50["thalach"].mean(),
            linestyle="--", color="r")

# add a figure title
fig.suptitle("Heart Disease Analysis", fontsize=16, fontweight="bold")

plt.show()
fig.savefig("images/heart-disease-analysis.png")