Data Preprocessing Script

This repository contains a Python script for preprocessing a dataset using various techniques such as handling missing data, encoding categorical variables, splitting the dataset into training and test sets, and feature scaling.

Table of Contents

Installation
Usage
Script Overview
Dependencies
License
Installation

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/data-preprocessing-script.git
Navigate to the repository directory:

bash
Copy code
cd data-preprocessing-script
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage

Place your dataset file (Data.csv) in the repository directory.
Run the preprocessing script:
bash
Copy code
python preprocess.py
Script Overview

The preprocess.py script performs the following steps:

Importing Libraries:

Imports necessary libraries such as numpy, pandas, and various sklearn modules.
Loading the Dataset:

Loads the dataset from Data.csv.
Creates a matrix of features (x) and an output column (y).
Handling Missing Data:

Uses SimpleImputer to fill missing values in the dataset with the mean value of the respective column.
Encoding Categorical Data:

Uses OneHotEncoder to encode categorical features.
Uses LabelEncoder to encode the output labels.
Splitting the Dataset:

Splits the dataset into training and test sets using train_test_split.
Feature Scaling:

Scales the features using StandardScaler.
Dependencies

The script requires the following Python libraries:

numpy
pandas
scikit-learn
You can install these dependencies using pip:

bash
Copy code
pip install numpy pandas scikit-learn

