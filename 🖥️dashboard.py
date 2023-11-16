

import streamlit as st


# General Title
st.title("Job Search Dashboard")

st.markdown("")
st.markdown("")


col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre de candidatures", "4", "+33% en nov.")
col2.metric(" Taux d'entretien", "25 %", "+100% en nov.")
col3.metric("Délai de réponse median", "12 jours", "0 - 16 jours")
col4.metric("Salaire median", "2916 €", "2820€ - 5050€")

st.markdown("")
st.markdown("")


import plotly.express as px
from plotly import graph_objects as go
import numpy as np

# Data for the charts
departments = ["Sales", "Engineering", "Customer Support", "Marketing"]
employee_counts = [100, 75, 50, 25]

line_chart_data = {
    'Mois': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Nombre de candidatures': [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0],
}

scatter_plot_data = {
    "Employee Performance Score": [75, 80, 85, 90, 95],
    "Training Hours Completed": [10, 15, 20, 25, 30]
}

department_salaries = {
    "M": np.random.randint(50000, 150000, size=100),
    "Sales": np.random.randint(50000, 150000, size=100),
    "Marketing": np.random.randint(50000, 150000, size=100),
}


box_plot_data = {
    'Entreprises': ['Mission Locale', 'CAVBS', 'CUCM', 'ONIRIS'],
    'Delai de reponse (jours)': [16, 0, 12, 1],
}

# Create the tabs
tabs = st.tabs(["Funnel Chart", "Line Chart", "Boxplot2", "Histogram", "Scatter Plot", "Boxplot"])

# Tab 1 - Funnel Chart
with tabs[0]:
    st.write("## Funnel Chart")
    fig = go.Figure(go.Funnel(
        y = ["Nombre de candidature", "Nombre de 1er contact", "Proposition d'entretien", "Entretiens réalisés", "Retour sur entretien"],
        x = [4, 4, 1, 1, 0],
        textposition = "inside",
        textinfo = "value+percent initial",
        opacity = 0.65, marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
        "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
        connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}})
        )
    st.plotly_chart(fig)

# Tab 2 - Line Chart
with tabs[1]:
    st.write("## Line Chart")
    fig = px.line(line_chart_data, x='Mois', y='Nombre de candidatures', markers=True)
    st.plotly_chart(fig)

# Tab 3 - Boxplot2
with tabs[2]:
    st.write("## Boxplot2")
    fig = px.box(box_plot_data, y='Delai de reponse (jours)', points="all")
    fig.update_layout(
        yaxis_title='Delai de reponse (jours)',
        boxmode='group'
    )
    st.plotly_chart(fig)
    
    # Tab 4 - Histogram
with tabs[3]:
    st.write("## Histogram")
    fig = px.histogram(box_plot_data, x='Delai de reponse (jours)', nbins=20)
    fig.update_layout(
        xaxis_title='Delai de reponse (jours)',
        yaxis_title='Count'
    )
    st.plotly_chart(fig)

# Tab 5 - Scatter Plot
with tabs[4]:
    st.write("## Scatter Plot")
    fig = px.scatter(scatter_plot_data, x="Training Hours Completed", y="Employee Performance Score", trendline="ols")
    st.plotly_chart(fig)

# Tab 6 - Boxplot
with tabs[5]:
    st.write("## Boxplot")
    fig = px.box(department_salaries, points="all")
    st.plotly_chart(fig)


