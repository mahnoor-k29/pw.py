# password generator
import re
import streamlit as st
st.set_page_config(page_tittle="Password Generator", page_icon="🔑" , layout="centered")
# custom css
st.markdown(
    """
<style>
    .main{text_align:center;}
    .stTextInput{width:60% !important; margin:auto;}
    .stButton button{width:50% ; background-color:#4cAf50; color:white;font_size:18px;}
    .stButton button:hover {background-color:#45a049;}
</style>
""",
    unsafe_allow_html=True)

# page tittle and sescription
st.tittle("🔐Password Strenght Generator")
st.write("Enter your Password below to check its security level ")

# function to check password strenght
def check_password_strenght(password):
    score = 0
    feedback = []
    if len(password) >= 8:
         score += 1   # increa score by 1
    else:
         feedback.append("❌password must be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password)and re.search(r"[a-z]",password):
         score += 1
    else:
         feedback.append("❌password must contain **both uppercase and lowercase letters**.")
    if re.search(r"/d",password):
         score += 1
    else:
         feedback.append("❌password must contain ** at least [0-9]**.")

# special character
    if re.search(r"[!@#$%^&*]",password):
         score += 1
    else:
         feedback.append("❌password must contain **special characters**.")

# display password strenght 
    if score==4:
     st.success("🔑**strong password** - Your password is secure . ")
    elif score ==3:
     st.info("**moderate password** - consider improving security by adding more features")
    else:
     st.error("❌**very weak password** - consider improving security by adding more features")

# feedback 

    if feedback:
         with st.expander("**improve your password**"):
             for item in feedback :
                 st.write(item)
password=st.text_input("Enter yout password",  type="password" ,help="Enter your password is strong " )

# button working
if st.button("Check strenght"):
    if password:
        check_password_strenght(password)
    else:
        st.warning("Please enter your password first!")  #show warning if password id incorrect 



     
     
