Configuration Guide
===================

PreppyData offers a range of configuration options to customize your data preprocessing experience. This guide explains the available options, default settings, and how you can tailor the preprocessing steps to fit your needs.

Configuration Options
---------------------

1. **Data Encoding Methods**
   - Transform categorical data into numerical format suitable for analysis.
   - **Options:**
     - **One-Hot Encoding**: Converts categories into binary columns.
     - **Label Encoding**: Assigns a unique integer to each category.

2. **Outlier Detection Techniques**
   - Identify and handle outliers in your dataset.
   - **Options:**
     - **Z-Score**: Detects outliers based on standard deviations from the mean.
     - **Interquartile Range (IQR)**: Uses quartiles to find anomalies.
     - **Local Outlier Factor (LOF)**: Identifies anomalies based on local density.

3. **Missing Value Handling**
   - Address missing data to improve dataset completeness.
   - **Options:**
     - **Mean Imputation**: Replaces missing values with the mean of the column.
     - **Median Imputation**: Uses the median to fill missing values.
     - **Deletion**: Removes rows or columns with missing values.

4. **Feature Selection Strategies**
   - Select relevant features to enhance model performance.
   - **Options:**
     - **Correlation-Based Selection**: Chooses features based on correlation with the target variable.
     - **LASSO Regression**: Uses regularization to select important features.

Default Settings
----------------

- **Automatic Application**: If you do not select any options, PreppyData will automatically apply default preprocessing methods.
- **Default Encoding**: One-Hot Encoding.
- **Default Outlier Detection**: IQR method.
- **Default Missing Value Handling**: Mean Imputation.
- **Default Feature Selection**: Correlation-Based Selection.

Customization Methods
---------------------

How to Customize Preprocessing Steps
-------------------------------------

1. **Access the Options Menu**:
   - After uploading your dataset, navigate to the preprocessing options section.

2. **Select Desired Options**:
   - **Data Encoding**: Choose between One-Hot Encoding and Label Encoding by checking the corresponding box.
   - **Outlier Detection**: Select your preferred method(s) by checking the appropriate boxes.
   - **Missing Value Handling**: Pick a strategy that suits your data.
   - **Feature Selection**: Choose between Correlation-Based Selection and LASSO Regression.

3. **Apply Changes**:
   - Click on the "Apply" button to execute the preprocessing steps with your selected configurations.

4. **Review and Download**:
   - Once processing is complete, review the results.
   - Download the processed data for your analysis.

Tips for Effective Configuration
--------------------------------

- **Understand Your Data**: Review your dataset to determine which preprocessing methods are most appropriate.
- **Experiment with Options**: Try different combinations of settings to see which yields the best results for your specific use case.
- **Use Default Settings When Unsure**: If you're uncertain about which options to choose, rely on the default settings to ensure basic preprocessing is applied.