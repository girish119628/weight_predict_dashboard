# Predicting Weight Change Based on Lifestyle and Caloric Intake

---

## Introduction
The Weight Prediction Dashboard is designed to predict weight change based on lifestyle factors such as caloric intake, physical activity level, and sleep quality. Users input personal data, and the model provides a weight change prediction, helping users make informed decisions regarding their lifestyle.

---

# Model : WEIGHT CHANGE PREDICTION
- Dataset:[Click Here](https://www.kaggle.com/datasets/abdullah0a/comprehensive-weight-change-prediction)
- This project uses machine learning to predict weight change based on various lifestyle factors, caloric intake, and other personal attributes. The goal is to provide users with a predictive tool that offers insights into how lifestyle choices impact weight change, accessible through an interactive dashboard.

---

# Table of Contents

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Model Selection and Training
- Model Evaluation and Optimization
- Deployment with Streamlit

---

# Data Preprocessing

- **Examine Data Types:** Categorical features (e.g., Gender, Physical Activity Level, Sleep Quality) were converted to numerical values using encoding techniques.
- **Feature Engineering:** Additional features were created, such as caloric intake per unit of weight or activity-weighted calories.
- **Handling Missing Values and Outliers:** Missing values were addressed, and outliers were reviewed to minimize their impact on predictions.
- **Scaling:** Numerical features with varying scales (e.g., BMR, Daily Calories Consumed, Stress Level) were normalized or standardized.

---

# Exploratory Data Analysis (EDA)

- **Visualized Feature Distributions:** Key features were plotted to identify patterns and correlations.
- **Analyzed Relationships:** Correlations between features (e.g., Daily Caloric Surplus/Deficit and Weight Change) were explored.
- **Target Variable Analysis:** The distribution of Weight Change (lbs) was examined to understand its spread and trends across demographics or activity levels.

---

# Model Selection and Training

- **Data Splitting:** An 80-20 train-test split was used.
- **Model Selection:** Various regression algorithms were applied, including:
  - Linear Regression
  - Decision Tree Regression
  - Gradient Boosting Regression
- **Model Training:** Each model was trained on the training set, using mean absolute error (MAE) or mean squared error (MSE) as performance metrics.

---

# Model Evaluation and Optimization

- **Evaluate Models:** Each model was tested on the test set, and performance was compared using MAE and MSE.
- **Hyperparameter Tuning:** Grid search or random search was used to optimize hyperparameters for the best-performing models.
- **Feature Importance:** The most influential features in predicting weight change were identified to provide actionable insights.

---

# Deployment with Streamlit

- **Set up Streamlit:** Streamlit was used to create an interactive web app for predictions.
- **Input Interface:** An input form allows users to enter details (e.g., age, current weight, calories consumed, activity level).
- **Model Loading and Prediction:** The trained model is saved using pickle, and predictions are generated based on user inputs.
- **Deployment:** The app can be run locally using streamlit run <script_name.py> and deployed on platforms like Streamlit Cloud, Heroku, or AWS.

---

## General Information
## Tools and Skills
- **Languages**: Python
- **Libraries**: NumPy, Pandas, Scikit-Learn, etc
- **Other Tools**: Jupyter Notebook, Google Colab, VS Code, Git, GitHub, Streamlit.

---


## Features and Techniques
- **Feature Engineering**: Create new features
- **Modeling Techniques**: Linear Regression, Decision Tree Regression, Gradient Boosting Regression etc.
- **Evaluation Metrics**: R2, Adjusted_R2, MSE, MAE, RMSE etc

---

## Contact Information
For questions or collaboration, feel free to reach out:

**Girish Kumar**
- Email: girish119628@gmail.com
- GitHub: https://github.com/girish119628
