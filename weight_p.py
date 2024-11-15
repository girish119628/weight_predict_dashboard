# import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the gender encoder
with open('gen_encode.pkl', 'rb') as f:
    gen_encode = pickle.load(f)
# Load the sleep_encoder
with open('sleep_encode.pkl', 'rb') as f:
    sleep_encode = pickle.load(f)
# Load the model
with open('P_model.pkl', 'rb') as f:
    P_model = pickle.load(f)
# Load the Yeo-Johnson tranformator
with open('transformator.pkl', 'rb') as f:
    pt = pickle.load(f)

# Creating an Input Interface 
st.title('Weight Change Prediction')
age = st.number_input('Age:', min_value=18, max_value=100)
gender = st.selectbox('Gender:', ['M', 'F'])
current_weight = st.number_input('Current Weight (lbs):', min_value=50.0, max_value=300.0, step=0.1)
daily_calories_surplus_deficit = st.number_input('Daily Calories Surplus/Deficit:', min_value=50.0, max_value=2500.0, step=0.1)
daily_calories_consumed = st.number_input('Daily Calories Consumed:', min_value=1500.0, max_value=5000.0, step=0.1)
stress_level = st.slider('Stress Level (1-10):', 1, 10, 5)
sleep_quality = st.selectbox('Sleep Quality:',['Excellent', 'Good', 'Fair', 'Poor'])
duration_weeks = st.number_input('Duration (Weeks):', min_value=1, max_value=52, value=4)
physical_activity_level = st.selectbox('Physical Activity', ['Sedentary', 'Very Active', 'Lightly Active', 'Moderately Active'])
bmr_calories = st.number_input('BMR (calories):', min_value=500.0, max_value=5000.0, step=0.1)    

gen_encode = gen_encode.transform([gender])[0]
sleep_quality_encoded = sleep_encode.transform([sleep_quality])[0]
# Calculating activity weighted calories from the input to feed the model
met_value_map = {'Sedentary' : 1.2, 'Very Active' : 1.9, 'Lightly Active' : 1.375, 'Moderately Active' : 1.55}
activity_weighted_calories = bmr_calories * met_value_map.get(physical_activity_level)

# Preparing the input to feed the model for users
input_data = pd.DataFrame({  
    'Current Weight (lbs)' : [current_weight],
    'Daily Calories Consumed' : [daily_calories_consumed],
    'Daily Caloric Surplus/Deficit' : [daily_calories_surplus_deficit],
    'Duration (weeks)' : [duration_weeks],
    'Sleep Quality' : [sleep_quality_encoded],
    'Stress Level' : [stress_level],
    'Activity Weighted Calories' : [activity_weighted_calories]
})

# Prediction button
if st.button('Predict Weight Change'):
    pred = P_model.predict(input_data)
    # Predict and inverse transform the prediction to the original scale
    prediction = pt.inverse_transform(pred.reshape(-1, 1))
    weight_change = prediction[0][0]
    # Display Predictions
    st.write(f"Predicted Weight Change: {weight_change:.2f} lbs")

    st.title('Advice')
    if weight_change > 2:
        if daily_calories_surplus_deficit > 0:
            st.write("**High Weight Gain**: Consider reducing your daily calorie surplus or increasing physical activity to prevent excessive weight gain.")
        else:
            st.write("**Unexpected Weight Gain**: Despite a calorie deficit, you're still gaining weight. Evaluate your diet and activity level for hidden sources of calories.")
    elif 0 < weight_change <= 2:
        if physical_activity_level in ['Sedentary', 'Lightly Active']:
            st.write("**Slight Weight Gain**: A low level of activity with a slight caloric surplus may be causing this. Increasing activity could help maintain your weight.")
        else:
            st.write("**Minor Weight Gain**: Since you’re active, this small gain may be due to muscle development or water retention.")
    elif -5 < weight_change <= 0:
        if stress_level > 6:
            st.write("**Moderate Weight Loss**: A moderate caloric deficit combined with high stress may lead to this. Consider stress management techniques to support healthy weight management.")
        else:
            st.write("**Healthy Weight Loss**: With a balanced deficit and moderate activity, you're on a sustainable weight loss path.")
    elif weight_change <= -5:
        if daily_calories_surplus_deficit < -500:
            st.write("**Significant Weight Loss**: A high calorie deficit can be effective short-term but may cause muscle loss. Consider reducing the deficit slightly for healthier weight loss.")
        else:
            st.write("**Extreme Weight Loss**: Rapid weight loss can impact muscle mass and energy levels. Aiming for a slower, steady loss may be healthier.")
    else:
        st.write("Your weight appears stable with current habits. Maintain balanced nutrition and moderate activity to keep weight stable.")

    st.success("**Note**: This advice is based on your inputs and predicted weight change. Consult a healthcare provider for more personalized guidance.")
    