import streamlit as st

st.title("CGPA Calculator")

num_sem = st.number_input("Number of semesters", min_value=1, max_value=14, value=10, step=1)

total_qp = 0.0
total_cr = 0.0

for num in range(1, int(num_sem) + 1):
    col1, col2 = st.columns(2)
    qp = col1.number_input(f"Semester {num} Quality Points", min_value=0.0, step=0.1, key=f"qp{num}")
    cr = col2.number_input(f"Semester {num} Credit Hours", min_value=0.0, step=1.0, key=f"cr{num}")
    total_qp += qp
    total_cr += cr

st.divider()
st.write("Total Quality Points:", round(total_qp, 2))
st.write("Total Credit Hours:", total_cr)

if total_cr > 0:
    cgpa = total_qp / total_cr
    st.success(f"CGPA: {round(cgpa, 2)}")
else:
    st.warning("CGPA is not calculated because Credit Hours is zero")