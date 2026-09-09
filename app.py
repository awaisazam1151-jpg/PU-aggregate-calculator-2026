import streamlit as st

# Title of the web app
st.title("🎓 Admission Aggregate Calculator")
st.write("Enter your marks below to calculate your final percentage aggregate.")

# Input fields for user marks
st.subheader("1. Matriculation (25% Weightage)")
matric_obt = st.number_input("Matric Obtained Marks", value=950.0)
matric_tot = st.number_input("Matric Total Marks", value=1100.0)

st.subheader("2. Inter / 11th Class (50% Weightage)")
inter_obt = st.number_input("Inter Obtained Marks", value=450.0)
inter_tot = st.number_input("Inter Total Marks", value=520.0)

st.subheader("3. Entry Test (25% Weightage)")
test_obt = st.number_input("Entry Test Obtained Marks", value=320.0)
test_tot = st.number_input("Entry Test Total Marks", value=400.0)

# Calculate button
if st.button("Calculate Aggregate"):
    m_pct = (matric_obt / matric_tot) * 100
    i_pct = (inter_obt / inter_tot) * 100
    t_pct = (test_obt / test_tot) * 100
    
    m_weight = m_pct * 0.25
    i_weight = i_pct * 0.50
    t_weight = t_pct * 0.25
    
    total = m_weight + i_weight + t_weight
    
    # Display results
    st.success(f"🎯 Total Aggregate: {total:.2f}%")
    st.info(f"Breakdown:\n- Matric: {m_weight:.2f}%\n- Inter: {i_weight:.2f}%\n- Entry Test: {t_weight:.2f}%")
