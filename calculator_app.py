import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

st.set_page_config(page_title="Calculator", layout="centered")
st.title("Calculator Application")

with st.container():
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        num1 = st.number_input("Enter first number", key="num1")
    
    with col2:
        operation = st.selectbox(
            "Operation",
            ["Add", "Subtract", "Multiply", "Divide"],
            key="op"
        )
    
    with col3:
        num2 = st.number_input("Enter second number", key="num2")

result = None
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)

if result is not None:
    st.markdown("---")
    st.subheader(f"Result: **{result}**")