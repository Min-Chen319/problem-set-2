import seaborn as sns
import matplotlib.pyplot as plt

def scatterplot(pred_universe):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="age_at_arrest",
        y="prediction_felony",
        hue="sex",
        data=pred_universe
    )
    plt.title("Age at Arrest vs. Felony Prediction by Sex")
    plt.xlabel("Age at Arrest")
    plt.ylabel("Prediction for Felony")
    plt.tight_layout()
    plt.savefig("data/part2_plots/scatterplot.png")
    plt.close()
