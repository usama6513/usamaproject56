# project 2: unit convertor
# build a google unit convertor using python and streamlit:

import streamlit as st
st.markdown(
    """"
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcb, #cfe2f3);
        padding: 30px;
        border-radiud: 15px; 
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton<button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: white
     }
     .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        marging: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        }
        .footer{
        text-align: center;
        maging-top: 50px;
        font-size: 14px;
        color: white
        }
        </style>
    """,
    unsafe_allow_html=True
)

#title and description:
st.markdown("<h1>🚀 Universal Unit Convertor</hi>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight and temperature.")

# sidebar menu
conversion_type=st.sidebar.selectbox("choose conversion type",["length","weight","temperature"])
value=st.number_input("Enter value",value=0.0,min_value=0.0,step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "length":
        with col1:
            from_unit = st.selectbox("From",["Meters","Kilometers","Centimeters","Miles","Inches","Feet","Yards",'Millimeters'])
        with col2:
            to_unit = st.selectbox("To",["Meters","Kilometers","Centimeters","Miles","Inches","Feet","Yards",'Millimeters'])
elif conversion_type == "weight":
        with col1:
            from_unit = st.selectbox("From",["kilograms","Grams","Milligrams","Pounds","Ounces"])
        with col2:
            to_unit = st.selectbox("To",["kilograms","Grams","Milligrams","Pounds","Ounces"])
elif conversion_type == "Temprature":
        with col1:
            from_unit = st.selectbox("From",["celsis","Fahrenheit","Kelvin"])
        with col2:
            to_unit = st.selectbox("To",["Celsius","Fahrenheit","Kelvin"])

# converted function
# converted function
def length_convertor(value, from_unit, to_unit):
    length_units =  {  
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,   
        'Miles': 0.000621371, 'Yards': 1.09631, 'Feet': 3.28, 'Inches':39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
         'Kilograms': 1, 'Grams': 1000, 'Milligrams': 100000, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value -32) *9/5 if to_unit == "Celsius" else value (-32) * 5/9 +273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value -273.15 if to_unit == "Celsius" else (value -273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion
if st.button("🤖Convert"):
    if conversion_type == "length":
         result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "weight":
         result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
         result = temp_convertor(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created with 💖 by Usama Sharif </div>",unsafe_allow_html=True) 
    




    



      
    


