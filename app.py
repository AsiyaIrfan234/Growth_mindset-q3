import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🔥")

st.markdown("""
    <style>
        body { background-color: #f8f9fa; } /* Light gray background */
        h1, h2, h3 { color: #2c3e50; } /* Dark headings */
        .title { font-size: 36px; font-weight: bold; color: #ff5733; }
        .quote-box {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #ff5733;
            font-style: italic;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='title'>🔥 Growth Mindset Challenge: Web App with Streamlit</h1>", unsafe_allow_html=True)

st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, turn mistakes into learning opportunities, and unlock your true potential with this AI-powered app designed to strengthen your growth mindset!")


st.markdown("""
    <div class='quote-box'>
        <h3>🌟 Quote of the Day</h3>
        <p>Success is not the end, failure is not defeat; it is the courage to keep going that truly matters.</p>
        <p>- Winston Churchill</p>
    </div>
""", unsafe_allow_html=True)

st.header("What challenge are you tackling today?")
user_input = st.text_input("Describe a challenge you’re currently facing:")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward toward your goal!")
else:
    st.warning("Tell us about your challenge to begin your growth journey!")    


st.header("Reflect on Your Learning Journey")  
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")  


st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")
else:
    st.info("Every achievement matters, big or small! Share one now.")

st.write("---")
st.markdown("<div class='footer'>💡 Created with passion by Asiya Irfan 💡</div>", unsafe_allow_html=True)



