import os
import pandas as pd
from src import part1_etl as part1
from src import part2_plot_examples as part2
from src import part3_bar_hist as part3
from src import part4_catplot as part4
from src import part5_scatter as part5

def main():
    # Create necessary folders
    os.makedirs("data/part2_plots", exist_ok=True)
    os.makedirs("data/part3_plots", exist_ok=True)
    os.makedirs("data/part4_plots", exist_ok=True)
    os.makedirs("data/part5_plots", exist_ok=True)

    # Part 1: Load and transform data (✔️ 正確接收6個回傳值)
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, merged_df = part1.extract_transform()

    # Part 2: Example scatterplot
    part2.scatterplot(pred_universe)

    # Part 3: Bar and histogram plots
    part3.barplot_fta(pred_universe)
    part3.barplot_fta_by_sex(pred_universe)
    part3.histogram_age(pred_universe)
    part3.histogram_age_binned(pred_universe)

    # Part 4: Categorical plots
    part4.countplot_by_race(pred_universe)
    part4.boxplot_age_by_fta(pred_universe)

    # Part 5: Scatter plots
    part5.felony_vs_nonfelony_scatter(pred_universe)
    part5.calibration_scatter(pred_universe)

if __name__ == "__main__":
    main()
# This line was added by Min-Chen for commit test