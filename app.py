import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="✧")
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, turn mistakes into learning opportunities, and unlock your true potential with this AI-powered app designed to strengthen your growth mindset!")

st.header("Quote of the Day: Embrace a Growth Mindset")
st.write("Success is not the end, failure is not defeat; it is the courage to keep going that truly matters. _Winston Churchill_")
st.header("What challenge are you tackling today?")
user_input = st.text_input("Describe a challenge you’re currently facing:")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward toward your goal!")
else:
     st.warning("Tell us about your challenge to begin your growth journey!")    

st.header("Reflect on Your Learning Journey")  
reflection = st.text_area("write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your refelection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")  
st.header("Celebrate Your Wins!")
acheivement = st.text_input("Share something you've recently accomplished:")
if acheivement:
    st.success(f"Amazing! You achieved: {acheivement}")
else:
  st.info("Every achievement matters, big or small! Share one now.")

st.write("---")    
st.write("Believe in yourself—every step forward is part of your growth journey!")  
st.write("💡 Created with passion by Asiya Irfan 💡")






