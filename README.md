# Data Analysis and Clustering

This repository contains Python scripts for data preprocessing, transformation, and clustering analysis with a focus on housing data and general data preprocessing techniques.

## Overview

The scripts implement various data mining techniques including:
- Data smoothing and outlier detection
- Data normalization and transformation
- Data binning (equal-width and equal-frequency)
- K-means clustering
- DBSCAN clustering

## Files

### Clustering Scripts

#### 1. assignment_6.py
K-means clustering implementation with the following features:
- Data standardization using `StandardScaler`
- K-means clustering with predefined cluster count (k=3)
- Performance evaluation metrics:
  - Inertia (Sum of squared distances)
  - Silhouette score
  - Davies-Bouldin index
- Cluster centers visualization

#### 2. sankalpa_a7.py
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) implementation with:
- Data standardization
- Dimensionality reduction using PCA
- DBSCAN clustering with customizable parameters (eps, min_samples)
- Identification of noise points
- Performance evaluation metrics:
  - Silhouette score
  - Davies-Bouldin index
- 2D visualization of clusters using matplotlib

### Data Preprocessing Scripts

#### 3. 3.3.py - Data Smoothing
Implements bin-based data smoothing with:
- Smoothing by averaging values in fixed-size bins
- Outlier detection using standard deviation
- Detailed output showing original data, smoothing process, and detected outliers

#### 4. 3.6.py - Data Normalization
Implements multiple data normalization techniques:
- Min-max normalization (scaling to 0-1 range)
- Z-score normalization (standardization)
- Decimal scaling normalization
- Compare results of different normalization methods

#### 5. 3.9.py - Data Binning
Implements data binning techniques:
- Equal-frequency binning (similar number of items in each bin)
- Equal-width binning (similar range of values in each bin)
- Calculation of bin averages

## Requirements

These scripts require the following Python libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- statistics (Python standard library)

You can install the required packages using:

```bash
pip install pandas numpy scikit-learn matplotlib
```

## Usage

### Clustering Analysis
```python
python assignment_6.py
python sankalpa_a7.py
```

### Data Preprocessing
```python
python 3.3.py  # Data smoothing and outlier detection
python 3.6.py  # Data normalization techniques
python 3.9.py  # Binning methods
```

## Dataset

The clustering scripts are designed to work with a housing dataset (`housing.csv`). The data preprocessing scripts use sample datasets defined within the scripts themselves.

## Examples

### Data Smoothing (3.3.py)
Demonstrates smoothing of age data using bin size of 3, replacing original values with bin averages and identifying outliers.

### Data Normalization (3.6.py)
Shows three normalization techniques applied to numeric data:
- Min-max scaling to [0,1] range
- Z-score normalization (mean=0, standard deviation=1)
- Decimal scaling based on maximum absolute value

### Data Binning (3.9.py)
Illustrates two binning approaches on sales price data:
- Equal-frequency binning (equal number of items per bin)
- Equal-width binning (equal value range per bin)

## Parameter Tuning

### K-means
You can experiment with different values of `k` (number of clusters) in assignment_6.py.

### DBSCAN
The DBSCAN implementation allows for customization of:
- `eps`: The maximum distance between two samples for one to be considered as in the neighborhood of the other
- `min_samples`: The number of samples in a neighborhood for a point to be considered as a core point
- `n_components`: Number of components for PCA dimensionality reduction

### Data Preprocessing
The preprocessing scripts allow for customization of:
- Bin size for data smoothing
- Number of bins for data binning
- Standard deviation threshold for outlier detection

## Results

The clustering scripts output performance metrics that can help evaluate the quality of the resulting clusters. The preprocessing scripts provide detailed output showing the transformation process and results.
