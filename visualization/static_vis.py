import streamlit as st
import pandas as pd
import numpy as np

#static.,visualization

import matplotlib.pyplot as plt
import seaborn as sns

st.header('Matplotlib and Seaborn visualizations in streamlit')

#Load data.

df = pd.read_csv('./tips.csv')
st.dataframe(df.head())

## quesions,
#1. find number of male and female distribution (pie and bar)

#2. find distrubution of male and female spent (boxplot or kdeplot)

#3. find distribution of average total bill across each day by male and female.

#4. find the relation between total bill and tip on time )(scatter plot)



#question 1.

st.markdown('---')


with st.container():

    st.header('1. find number of male and female distribution (pie and bar)')
    value_counts = df['sex'].value_counts()
    
    col1,col2 = st.columns(2)


    #drawing the pie chart.

    with col1:

        st.subheader("Pie Chart")

        fig,ax = plt.subplots()

        ax.pie(value_counts,autopct='%0.2f%%',labels=['Male','Female'])

        st.pyplot(fig)

    #draw bar plot
   
    with col2:

        st.subheader('Bar Chart')

        fig,ax = plt.subplots()

        ax.bar(value_counts.index,value_counts)

        st.pyplot(fig)



    #expander

    with st.expander('Click here to display value counts'):

        st.dataframe(value_counts)

# streamlit widgets and charts.

data_types = df.dtypes

cat_cols = tuple(data_types[data_types == 'object'].index)

st.markdown('---')


with st.container():

    feature = st.selectbox('Select the feature you want to display bar and pie chart' , 
     
     cat_cols
    )

    st.header('1. find number of male and female distribution (pie and bar)')
    value_counts = df[feature].value_counts()
    
    col1,col2 = st.columns(2)


    #drawing the pie chart.

    with col1:

        st.subheader("Pie Chart")

        fig,ax = plt.subplots()

        ax.pie(value_counts,autopct='%0.2f%%',labels=value_counts.index)

        st.pyplot(fig)

    #draw bar plot
   
    with col2:

        st.subheader('Bar Chart')

        fig,ax = plt.subplots()

        ax.bar(value_counts.index,value_counts)

        st.pyplot(fig)



    #expander

    with st.expander('Click here to display value counts'):

        st.dataframe(value_counts)



#question 2.

with st.container():

    st.markdown('---')

    st.subheader('find distrubution of male and female spent ')

    #box , violin , kdeplot , histogram.

    chart = ('box','violin','kdeplot','histogram')

    chart_selection = st.selectbox('Select the chart type',chart)

    fig,ax = plt.subplots()

    if chart_selection == 'box':

     sns.boxplot(x='sex',y='total_bill',data=df,ax=ax)

    elif chart_selection == 'violin':

        sns.violinplot(x='sex',y='total_bill',data=df,ax=ax)

    elif chart_selection == 'kdeplot':

        sns.kdeplot(x=df['total_bill'],hue=df['sex'],ax=ax,shade=True)

    else:

        sns.histplot(x='total_bill',hue='sex',data=df,ax=ax)


    st.pyplot(fig)


#question 3.

st.markdown('---')

st.subheader('find distribution of average total bill across each day by male and female')

features_to_groupby = ['day','sex']

feature = ['total_bill']

select_cols = feature + features_to_groupby

avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()

avg_total_bill = avg_total_bill.unstack()


#visual
fig,ax = plt.subplots()

avg_total_bill.plot(kind='bar',ax=ax)

ax.set_ylabel('Avg Total Bill')


st.pyplot(fig)

st.dataframe(avg_total_bill)

###

with st.container():
    #1. include all categorical features.
    #2. bar , chart.

    #3. stacked.

    c1,c2,c3 = st.columns(3)

    with c1:

        group_cols = st.multiselect('Select the features' , cat_cols,cat_cols[0])

        features_to_groupby = ['day','sex']

        n_features = len(features_to_groupby)

    
    with c2:

        chart_type = st.selectbox('Select chart type' , ('bar','area','line'))

    with c3:

        stack_option = st.radio('Stacked' , ('Yes','No'))

        if stack_option == 'Yes':
            stacked = True

        else:

            stacked = False



    

    feature = ['total_bill']

    select_cols = feature + features_to_groupby

    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()


    if n_features > 1:

        for i in range(n_features-1):

            avg_total_bill = avg_total_bill.unstack()


    #visual
    fig,ax = plt.subplots()

    avg_total_bill.plot(kind=chart_type,ax=ax)

    ax.set_ylabel('Avg Total Bill')


    st.pyplot(fig)


    with st.expander('Click here to view values'):
        st.dataframe(avg_total_bill)


#find the realtion between totoal_bill and tip on time.

st.markdown('---')

st.subheader('find the realtion between totoal_bill and tip on time.')

fig,ax = plt.subplots()

hue_type = st.selectbox('Select feature to hue' , cat_cols)

sns.scatterplot(x='total_bill',y='tip',hue=hue_type,ax=ax,data=df)

st.pyplot(fig)