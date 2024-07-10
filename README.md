# Data Processing for Machine Learning

This repository contains a Python script for preprocessing a dataset using various techniques such as handling missing data, encoding categorical variables, splitting the dataset into training and test sets, and feature scaling.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ShayanAlahyari/Data_Processing_For_Machine_Learning.git
    ```

2. Navigate to the repository directory:
    ```bash
    cd Data_Processing_For_Machine_Learning
    ```

3. Install the required dependencies:
    ```bash
    pip install numpy pandas scikit-learn
    ```

## Usage

1. Place your dataset file (`Data.csv`) in the repository directory.
2. Run the preprocessing script:
    ```bash
    python data_processing.py
    ```

## Script Overview

The `data_processing.py` script performs the following steps:

1. **Importing Libraries**:
    - Imports necessary libraries such as `numpy`, `pandas`, and various `sklearn` modules.

2. **Loading the Dataset**:
    - Loads the dataset from `Data.csv`.
    - Creates a matrix of features (`x`) and an output column (`y`).

3. **Handling Missing Data**:
    - Uses `SimpleImputer` to fill missing values in the dataset with the mean value of the respective column.

4. **Encoding Categorical Data**:
    - Uses `OneHotEncoder` to encode categorical features.
    - Uses `LabelEncoder` to encode the output labels.

5. **Splitting the Dataset**:
    - Splits the dataset into training and test sets using `train_test_split`.

6. **Feature Scaling**:
    - Scales the features using `StandardScaler`.

## Dependencies

The script requires the following Python libraries:

- numpy
- pandas
- scikit-learn

You can install these dependencies using `pip`:

```bash
pip install numpy pandas scikit-learn
