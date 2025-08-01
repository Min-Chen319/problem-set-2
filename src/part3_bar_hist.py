import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def barplot_fta(pred_universe):
    sns.countplot(x="fta", data=pred_universe)
    plt.title("FTA Counts")
    plt.xlabel("FTA")
    plt.ylabel("Count")
    plt.savefig("data/part3_plots/barplot_fta.png")
    plt.clf()

def barplot_fta_by_sex(pred_universe):
    sns.countplot(x="fta", hue="sex", data=pred_universe)
    plt.title("FTA by Sex")
    plt.xlabel("FTA")
    plt.ylabel("Count")
    plt.savefig("data/part3_plots/barplot_fta_by_sex.png")
    plt.clf()

def histogram_age(pred_universe):
    sns.histplot(pred_universe["age_at_arrest"], bins=30, kde=True)
    plt.title("Histogram of Age at Arrest")
    plt.xlabel("Age at Arrest")
    plt.ylabel("Count")
    plt.savefig("data/part3_plots/histogram_age.png")
    plt.clf()

def histogram_age_binned(pred_universe):
    bins = [18, 21, 30, 40, 100]
    labels = ["18-21", "21-30", "30-40", "40-100"]
    pred_universe["age_binned"] = pd.cut(pred_universe["age_at_arrest"], bins=bins, labels=labels, right=False)
    sns.countplot(data=pred_universe, x="age_binned")
    plt.title("Histogram of Binned Age Groups")
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.savefig("data/part3_plots/histogram_age_binned.png")
    plt.clf()
