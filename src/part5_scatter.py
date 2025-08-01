import seaborn as sns
import matplotlib.pyplot as plt

def felony_vs_nonfelony_scatter(pred_universe):
    sns.set(style="whitegrid")
    sns.lmplot(
        x="prediction_felony",
        y="prediction_nonfelony",
        hue="y_felony",
        data=pred_universe,
        height=6,
        aspect=1.2,
        scatter_kws={'alpha':0.5}
    )
    plt.title("Prediction Felony vs. Prediction Non-Felony by Actual Felony")
    plt.savefig("data/part5_plots/felony_vs_nonfelony.png")
    print("Q: What can you say about the group of dots on the right side of the plot?")
    print("A: Those dots likely indicate individuals predicted to be high risk for both felony and non-felony outcomes, especially when current charge is felony.")

def calibration_scatter(pred_universe):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="prediction_felony",
        y="y_felony",
        data=pred_universe,
        alpha=0.5
    )
    plt.title("Felony Prediction vs. Actual Rearrest Outcome")
    plt.xlabel("Prediction for Felony Rearrest")
    plt.ylabel("Actual Rearrest (Felony)")
    plt.tight_layout()
    plt.savefig("data/part5_plots/calibration_plot.png")
    plt.close()
    print("Q: Is the model calibrated?")
    print("A: If the points trend upward along the diagonal, the model is more likely calibrated. If not, the predictions may be poorly calibrated.")
