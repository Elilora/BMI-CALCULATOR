import streamlit as st

def calculate_bmi( weight:float, height: float) -> float:
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")
    st.image("bmi.jfif", use_column_width = True, width =500)
    st.text("Find out your Body Mass Index (BMI) and take hold of your health with our BMI Calculator")
    
    st.subheader("Biodata")
    st.text_input("Name")
    st.date_input(" Date of Birth")
    st.number_input("Age", 1, 100)
    st.selectbox("Gender", ["Male", "Female", "Other"])
    
    weight = st.number_input("Weight (in kilogram)")
    height = st.number_input("Height (in metres)")
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write(" Your status is Underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.write("Your satus is Normal weight")
        elif bmi > 24.9 and bmi < 30:
            st.write("Your status is Overweight")
        elif bmi> 29.9 and bmi < 35:
            st.write("Your status is Obesity class I")
        elif bmi > 34.9 and bmi < 40:
            st.write("Your status is Obesity class II")
        else:
            st.write("Your status is Obesity class III")
            
    st.sidebar.radio("Which is your favourite pet", ["Cats", "Dogs", "Birds"])
    
    with st.sidebar:
        st.select_slider("What is your shirt sixe: ", ["S","M", "L", "XL", "XXL"])
        st.color_picker("What is your favourite color")
        st.text_area("Feedback")
    

if __name__ == "__main__":
    main()
