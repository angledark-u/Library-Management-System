import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import os
from matplotlib.backends.backend_agg import RendererAgg
import base64
import plotly.express as px
import streamlit as st 
import pandas as pd


df = px.data.iris()
@st.experimental_memo
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

background-position: centre; 
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

st.title('Library Management Analysis')
st.sidebar.title("Click Here")
if st.sidebar.checkbox("STUDENTS ENTRY"):
     def main():
       def add_book_and_student(roll_no,date, name, department, Entry_Time, Exit_Time, Books_Studied, csv_file):
           df = pd.read_csv(csv_file)
           new_data = pd.DataFrame({'Roll No': [roll_no],'Date' : [date],'Name': [name],'Department':[department],'Entry_Time':[Entry_Time],'Exit_Time':[Exit_Time],'Books_Studied':[Books_Studied]})
           df = df.append(new_data, ignore_index=True)  
           df.to_csv(csv_file, index=False)  
        
       st.title("Enter The Details....")
       roll_no = st.text_input("Enter Roll No",key=11)
       date = st.text_input("Enter Date",key=2)
       name = st.text_input("Enter Name",key=3)
       department = st.text_input("Enter the department name",key=4)
       Entry_Time = st.text_input("Enter the Entry Time",key=5)
       Exit_Time = st.text_input("Enter the Exit Time",key=6)
       Books_Studied= st.text_input("Enter the Name of the Book you studied",key=7)
       csv_file = st.text_input("Enter Excel File Name (e.g. data.csv)")
       if roll_no and date and name and department and Entry_Time and Exit_Time and Books_Studied and csv_file:
               if st.button("Add"):
                   add_book_and_student(roll_no,date, name, department, Entry_Time, Exit_Time, Books_Studied, csv_file)
                   st.success("Your Details are Added..")
               else:
                    st.warning("Please provide all the required information.")
                    
     if __name__ == "__main__":
         main()     




if st.sidebar.checkbox("VIEW THE LIST"):
    def main():
        csv_files = {
            "January,2023": "january.csv",
            "February,2023": "february.csv",
            "March,2023": "march.csv",
            "April,2023":"",
            "May,2023":"",
            "June,2023":"",
            "July,2023":"",
            "August,2023":"",
            "September,2023":"",
            "October,2023":"",
            "November,2023":"",
            "December,2023":"",
            }
        month = st.sidebar.selectbox("Select month", list(csv_files.keys()))

    # Display the CSV file for the selected month
        if st.button("CLICK HERE TO SEE DATA"):
            try:
                csv_df = pd.read_csv(csv_files[month])
                st.code("Library list of month of", month)
                st.write(csv_df)
            except FileNotFoundError:
                st.error(f"No Data is found for {month}")


    if __name__ == "__main__":
      main()     



if st.sidebar.checkbox("ANALYSIS"):
   def main():
        csv_files = {
            "January,2023": "january.csv",
            "February,2023": "february.csv",
            "March,2023": "march.csv",
            "April,2023":"",
            "May,2023":"", 
            "June,2023":"",
            "July,2023":"",
            "August,2023":"",
            "September,2023":"",
            "October,2023":"",
            "November,2023":"",
            "December,2023":"",   
        }
        month = st.sidebar.selectbox("Select month", list(csv_files.keys()),key=122) 
        csv_df = pd.read_csv(csv_files[month])
        st.write(csv_df)          
        selected_column = st.selectbox("Select a column",csv_df.columns)

        mode = csv_df[selected_column].mode()[0]
        st.code("Most visited {} is: {}".format(selected_column, mode))
                
        selected_column = st.selectbox("Visualization",csv_df.columns,key=1)
        value_counts = csv_df[selected_column].value_counts()
        value_counts_df = pd.DataFrame({"Value": value_counts.index, "Count": value_counts.values})
        chart = alt.Chart(value_counts_df).mark_bar().encode(
                x="Value",
                y="Count"
                ).properties( 
                width=700,
                height=800,
                
               
                )
        st.altair_chart(chart)    
        
   if __name__ == "__main__":
    main()                
        


        
