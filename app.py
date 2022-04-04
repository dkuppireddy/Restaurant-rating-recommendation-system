import pandas as pd
import streamlit as st
import pickle


def recommend(rest_name):
    restaurant_index = restaurant[restaurant['Restaurant_Name'] == rest_name].index[0]
    distances = similarity[restaurant_index]
    rest_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_restaurants=[]
    for i in rest_list:
        recommended_restaurants.append(restaurant.iloc[i[0]].Restaurant_Name)
    return recommended_restaurants


restaurants_list = pickle.load(open('restaurants.pkl', 'rb'))
restaurant = pd.DataFrame(restaurants_list)
restaurants_names = restaurant['Restaurant_Name'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Restaurant Recommender System')
Selected_restaurant = st.selectbox('Select', restaurants_names)

if st.button('Recommend'):
    recommendations = recommend(Selected_restaurant)
    for i in recommendations:
        st.write(i)