# Badminton Player Performance Analysis

An analysis of 100 top-ranked BWF badminton players across all five categories. The project covers data collection and cleaning, exploratory analysis, an interactive Streamlit dashboard, and two machine learning models.

## Project Files

| File | What it is |
|---|---|
| `Badminton_Dataset_CLEANED.csv` | The cleaned dataset (100 players) |
| `dashboard_badminton.py` | Interactive Streamlit dashboard |
| `pranv_major_project__code_.ipynb` | Data loading, cleaning, and exploratory analysis |
| `badminton__model.ipynb` | Linear Regression model predicting Win Rate % |
| `Badminton_Project__Report.docx` | Full project report |

## Dataset

- **100 players** across five categories: Men's Singles (30), Women's Singles (25), Men's Doubles (15), Women's Doubles (15), and Mixed Doubles (15).
- **27 variables** covering BWF ranking and points, age, height, playing style, handedness, career titles, win and loss records, and skill scores such as smash speed, smash success, and rally win rate.
- **Note:** Agility Score, Net Play Score, and Stamina Index are estimated values, not measured statistics. They were based on each player's ranking, category, and playing style.

## Setup

Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy streamlit plotly
```

## Running the Project

**Dashboard:** Keep `Badminton_Dataset_CLEANED.csv` in the same folder as the script, then run:

```bash
streamlit run dashboard_badminton.py
```

**Notebooks:** Open them in Jupyter, with the CSV in the same folder. The main notebook loads the file from a fixed path on the original computer. Change it to `pd.read_csv("Badminton_Dataset_CLEANED.csv")` before running.

## Methods

1. **Cleaning:** Removed extra spaces from column names, converted numeric columns, and dropped rows missing key values.
2. **Exploratory analysis:** Summary statistics, distributions, correlations, and comparisons by playing style, handedness, category, and year turned pro.
3. **Linear Regression:** Predicts Win Rate % from 15 features (physical, skill, and ranking variables). The data was split 80% training and 20% testing, with `random_state=42`.
4. **Random Forest Classifier:** Predicts playing style from performance scores.

## Results

**Linear Regression (Win Rate %)**

| Metric | Value |
|---|---|
| Training R² | 0.9914 |
| Test R² | 0.9816 |
| Test MAE | 0.594 |
| Test RMSE | 0.796 |

**Random Forest (Playing Style):** 40% accuracy. Smash Speed was the most useful feature, followed by Net Play Score.

## Key Findings

- Win Rate % is very closely linked to Rally Win Rate % (correlation 0.99) and Unforced Error % (correlation −0.95).
- Smash speed is the most useful feature for telling playing styles apart, which fits the expectation that power players hit faster.
- Playing style is harder to predict than win rate, because styles overlap. For example, All-round and Speed players can look similar.

## Limitations

- Several skill scores are estimated, so findings that depend on them reflect the estimation method as much as real play.
- Rally Win Rate % and Win Rate % measure nearly the same thing, so the high R² mostly reflects that overlap rather than a strong predictive result.
- The dataset has only 100 players, and the test set has 20, so results can change a lot with small data changes.
- The playing style column has six labels, including "Creative" (one player). The models and report cover five styles.

## Author

[Pranav Ram]
