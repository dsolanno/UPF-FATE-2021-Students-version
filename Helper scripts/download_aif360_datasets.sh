#!/bin/sh

# You can modify this variable according to your Python version
PythonPath = /usr/local/lib/python3.7

echo $PythonPath


# Adult dataset
cd "${PythonPath}/site-packages/aif360/data/raw/adult"
wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test
wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names


# German dataset
cd "${PythonPath}/site-packages/aif360/data/raw/german"
wget https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.doc

# Compas dataset
cd "${PythonPath}/site-packages/aif360/data/raw/compas"
wget https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv