import seaborn as sns
import matplotlib.pyplot as plt

def catplot_felony_prediction(merged_df):
    sns.catplot(x="has_felony_charge", y="predicted_felony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/catplot_felony_pred.png")
    print("Felony charges are associated with higher predicted probabilities.")

def catplot_nonfelony_prediction(merged_df):
    sns.catplot(x="has_felony_charge", y="predicted_nonfelony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/catplot_nonfelony_pred.png")
    print("Difference likely due to model's stronger signal for felony patterns than nonfelony.")

def catplot_felony_actual_vs_pred(merged_df):
    sns.catplot(x="has_felony_charge", y="predicted_felony", hue="actual_felony", kind="bar", data=merged_df)
    plt.savefig("data/part4_plots/catplot_felony_pred_vs_actual.png")
    print("Model gives higher predicted probability to people with current felony charges, even if they didn't reoffend — likely a bias in how felony status is interpreted.")

def countplot_by_race(pred_universe):
    sns.countplot(x="race", data=pred_universe)
    plt.title("Count of Individuals by Race")
    plt.xlabel("Race")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/part4_plots/countplot_by_race.png")
    plt.clf()

def boxplot_age_by_fta(pred_universe):
    sns.boxplot(x="fta", y="age_at_arrest", data=pred_universe)
    plt.title("Age at Arrest by FTA")
    plt.xlabel("FTA")
    plt.ylabel("Age at Arrest")
    plt.tight_layout()
    plt.savefig("data/part4_plots/boxplot_age_by_fta.png")
    plt.clf()
