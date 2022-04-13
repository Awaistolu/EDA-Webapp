import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp title

st.markdown(''' 
# **Exploratory Data Analysis Web Application** 
''')

# how to upload a file from pc

with st.sidebar.header('Upload your Dataset (.csv)'):
       upload_file = st.sidebar.file_uploader('upload your file',type=['csv'])
       df = sns.load_dataset('titanic')
       st.sidebar.markdown("[Example csv file](https://raw.githubusercontent.com/dataprofessor/data/master/BostonHousing_train.csv)")

  # profiling report for pandas

if upload_file is not None:
      @st.cache
      def load_csv():
            csv = pd.read_csv(upload_file)
            return csv
      df = load_csv()
      pr = ProfileReport(df,explorative=True)
      st.header('**Input DF**')
      st.write(df)
      st.write('---')
      st.header('**Profiling report with pandas**')
      st_profile_report(pr)
else: 
   st.info('Awaiting for csv file')
   if st.button('press to use example data'):
              
          # example dataset
       
         @st.cache
         def load_data():
            ex_data = pd.DataFrame(np.random.rand(100,5),columns=['col1','col2','col3','col4','col5'])

            return ex_data
         df = load_data()
         pr = ProfileReport(df,explorative=True)
         st.header('**Input DF**')
         st.write(df)
         st.write('---')
         st.header('**Profiling report with pandas**')
         st_profile_report(pr)

