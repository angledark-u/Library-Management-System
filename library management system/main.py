import base64
import altair as alt
import pandas as pd
import streamlit as st

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url(https://images.unsplash.com/photo-1532012197267-da84d127e765?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80);
background-size: 50%;
background-position: center;
background-repeat: repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def add_book_and_student(roll_no, date, name, department, Entry_Time, Exit_Time, Books_Studied, csv_file):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Roll No', 'Date', 'Name', 'Department', 'Entry_Time', 'Exit_Time', 'Books_Studied'])

    new_data = pd.DataFrame({'Roll No': [roll_no], 'Date': [date], 'Name': [name],
                             'Department': [department], 'Entry_Time': [Entry_Time],
                             'Exit_Time': [Exit_Time], 'Books_Studied': [Books_Studied]})
    
    if 'Roll No' not in df.columns:
        df = pd.DataFrame(columns=['Roll No', 'Date', 'Name', 'Department', 'Entry_Time', 'Exit_Time', 'Books_Studied'])

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(csv_file, index=False)

def view_list(month, csv_files):
    try:
        csv_df = pd.read_csv(csv_files[month])
        st.code(f"Library list of month of {month}")
        st.write(csv_df)
    except FileNotFoundError:
        st.error(f"No Data is found for {month}")

def analysis(month, csv_files):
    csv_df = pd.read_csv(csv_files[month])
    st.write(csv_df)
    
    selected_column = st.selectbox("Select a column", csv_df.columns)
    mode = csv_df[selected_column].mode()[0]
    st.code(f"Most visited {selected_column} is: {mode}")

    selected_column_viz = st.selectbox("Visualization", csv_df.columns)
    value_counts = csv_df[selected_column_viz].value_counts()
    value_counts_df = pd.DataFrame({"Value": value_counts.index, "Count": value_counts.values})
    chart = alt.Chart(value_counts_df).mark_bar().encode(
        x="Value",
        y="Count"
    ).properties(
        width=700,
        height=800,
    )
    st.altair_chart(chart)

def main():
    st.title('Library Management Analysis')
    st.sidebar.title("Click Here")

    if st.sidebar.checkbox("STUDENTS ENTRY"):
        st.title("Enter The Details....")
        roll_no = st.text_input("Enter Roll No", key=11)
        date = st.text_input("Enter Date", key=2)
        name = st.text_input("Enter Name", key=3)
        department = st.text_input("Enter the department name", key=4)
        Entry_Time = st.text_input("Enter the Entry Time", key=5)
        Exit_Time = st.text_input("Enter the Exit Time", key=6)
        Books_Studied = st.text_input("Enter the Name of the Book you studied", key=7)
        csv_file = st.text_input("Enter Excel File Name (e.g., data.csv)")

        if roll_no and date and name and department and Entry_Time and Exit_Time and Books_Studied and csv_file:
            if st.button("Add"):
                add_book_and_student(roll_no, date, name, department, Entry_Time, Exit_Time, Books_Studied, csv_file)
                st.success("Your Details are Added..")
            else:
                st.warning("Please provide all the required information.")

    if st.sidebar.checkbox("VIEW THE LIST"):
        csv_files = {
            "January,2023": "january.csv",
            "February,2023": "february.csv",
            "March,2023": "march.csv",
            "April,2023": "april.csv",
            "May,2023": "may.csv",
            "June,2023": "june.csv",
            "July,2023": "july.csv",
            "August,2023": "august.csv",
            "September,2023": "september.csv",
            "October,2023": "october.csv",
            "November,2023": "november.csv",
            "December,2023": "december.csv",
        }
        month_view = st.sidebar.selectbox("Select month", list(csv_files.keys()))
        if st.button("CLICK HERE TO SEE DATA"):
            view_list(month_view, csv_files)

    if st.sidebar.checkbox("ANALYSIS"):
        csv_files_analysis = {
            "January,2023": "january.csv",
            "February,2023": "february.csv",
            "March,2023": "march.csv",
            "April,2023": "april.csv",
            "May,2023": "may.csv",
            "June,2023": "june.csv",
            "July,2023": "july.csv",
            "August,2023": "august.csv",
            "September,2023": "september.csv",
            "October,2023": "october.csv",
            "November,2023": "november.csv",
            "December,2023": "december.csv",
        }
        month_analysis = st.sidebar.selectbox("Select month", list(csv_files_analysis.keys()), key=122)
        analysis(month_analysis, csv_files_analysis)


if __name__ == "__main__":
    main()
