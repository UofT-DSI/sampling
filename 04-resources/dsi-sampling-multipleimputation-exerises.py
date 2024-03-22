import pandas as pd
import numpy as np
from fancyimpute import IterativeImputer
import statsmodels.api as sm
import pandas as pd
import pandas as pd
from fancyimpute import IterativeImputer
import statsmodels.api as sm
import matplotlib.pyplot as plt
import missingno as msno
from matplotlib.colors import LinearSegmentedColormap


def plot_missing_data_matrix(df):
    """
    Plots a missing data matrix for the given DataFrame.
    
    Parameters:
    - df: pandas DataFrame to visualize missing data patterns.
    """
    # Create a boolean mask, where True indicates missing values
    missing_data_mask = df.isnull()

    # Define custom colors using RGB tuples (values between 0 and 1)
    # Example: light blue for present, light red for missing
    colors = [(108/255, 151/255, 208/255), (193/255, 107/255, 132/255)]  # Light blue for present, light red for missing

    cmap_name = 'custom_soft'
    cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=2)

    # Plotting
    plt.figure(figsize=(15, 8))
    plt.imshow(missing_data_mask.astype(int), aspect='auto', cmap=cm, interpolation='none')

    plt.xticks(np.arange(df.shape[1]), df.columns, rotation='vertical')
    plt.yticks([])  # Hide y ticks as the rows do not correspond to a specific category
    plt.title('Missing Data Pattern in Dataset')
    plt.show()

# Load data (assuming you have a CSV or similar format to load, as Python doesn't have a direct equivalent of R's data("mammalsleep"))
# For demonstration, replace 'your_file_path.csv' with the path to your data file.
mammalsleep = pd.read_csv('./mammalsleep.csv')

# Call the helper function with the DataFrame
plot_missing_data_matrix(mammalsleep)

# Save the species column in a separate variable and remove it from the dataset for imputation
species = mammalsleep['species']
mammalsleep_numeric = mammalsleep.drop('species', axis=1)

# Display summary statistics of the data
print(mammalsleep.describe())

# Imputation with MICE (Multiple Imputation by Chained Equations)
# Note: Adjust the 'm' parameter for the number of imputations and 'random_state' for reproducibility
imputer = IterativeImputer(max_iter=10, random_state=100)
mammalsleep_imputed = imputer.fit_transform(mammalsleep_numeric)
mammalsleep_imputed = pd.DataFrame(mammalsleep_imputed, columns=mammalsleep_numeric.columns)

# Add the species column back to the imputed DataFrame
mammalsleep_imputed['species'] = species

# If you want 'species' as the first column, you can reindex the columns as follows:
cols = ['species'] + [col for col in mammalsleep_imputed if col != 'species']
mammalsleep_imputed = mammalsleep_imputed[cols]

print(mammalsleep_imputed.head())

# Display imputed data summary
print(mammalsleep_imputed.describe())

# Linear regression models on imputed data
# Prepare data for regression model
X = mammalsleep_imputed[['bw', 'brw']]  # Independent variables
X = sm.add_constant(X)  # Adds a constant term to the predictor
y = mammalsleep_imputed['sws']  # Dependent variable

# Fit model
model = sm.OLS(y, X).fit()

# Display model summary
print(model.summary())

# For comparison, model on non-imputed data (dropping missing values)
mammalsleep_dropna = mammalsleep.dropna()
X_non_imputed = mammalsleep_dropna[['bw', 'brw']]
X_non_imputed = sm.add_constant(X_non_imputed)
y_non_imputed = mammalsleep_dropna['sws']

model_non_imputed = sm.OLS(y_non_imputed, X_non_imputed).fit()
print(model_non_imputed.summary())
