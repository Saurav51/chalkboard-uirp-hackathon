import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# --- Load data ---
df = pd.read_csv("datasets/viz1.csv")
df['Course'] = df['Subject'] + " " + df['Number'].astype(str)
df['Instructor'] = df['Primary Instructor']

st.set_page_config(page_title="CHALKBOARD", layout="wide")

st.title("🧠 CHALKBOARD")
st.markdown("### Explore GPA trends and visualize your weekly course schedule.")

# --- GPA Visualization ---
st.subheader("📊 GPA by Instructor")

course_list = sorted(df['Course'].unique())
selected_course = st.selectbox("Select a Course:", course_list)

# Filtered dataframe
filtered_df = df[df['Course'] == selected_course]
num_instructors = filtered_df.shape[0]

chart_height = max(300, num_instructors * 45)
chart_width = 700 if num_instructors > 15 else 500

chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Overall_GPA:Q', title='Average GPA', scale=alt.Scale(domain=[0, 4])),
    y=alt.Y('Instructor:N', sort='-x'),
    color=alt.Color('Overall_GPA:Q', scale=alt.Scale(scheme='blues')),
    tooltip=[
        'Instructor:N', 'Overall_GPA:Q', 'Total_Students:Q',
        alt.Tooltip('A_range:Q', title='A %', format=".1f"),
        alt.Tooltip('B_range:Q', title='B %', format=".1f"),
        alt.Tooltip('C_range:Q', title='C %', format=".1f"),
        alt.Tooltip('D_range:Q', title='D %', format=".1f"),
        alt.Tooltip('F_range:Q', title='F %', format=".1f"),
    ]
).properties(
    height=chart_height,
    width=chart_width,
    title=f"GPA by Instructor for {selected_course}"
)

st.altair_chart(chart, use_container_width=True)

# --- Weekly Calendar View ---
st.subheader("📅 Course Calendar")

# Assuming 'Days', 'Start_Time', 'End_Time' columns exist
# Convert to datetime range (mock date for day-of-week)
day_map = {
    "Monday": "2025-07-07", "Tuesday": "2025-07-08", "Wednesday": "2025-07-09",
    "Thursday": "2025-07-10", "Friday": "2025-07-11"
}

calendar_df = df[df['Course'] == selected_course].copy()
calendar_df["start"] = calendar_df["Days"].map(day_map) + "T" + calendar_df["Start_Time"]
calendar_df["end"] = calendar_df["Days"].map(day_map) + "T" + calendar_df["End_Time"]

fig = px.timeline(
    calendar_df,
    x_start="start",
    x_end="end",
    y="Instructor",
    color="Instructor",
    title="Weekly Course Time Blocks"
)

fig.update_layout(
    xaxis_title="Time of Day",
    yaxis_title="Instructor",
    xaxis=dict(tickformat="%H:%M"),
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Created with ❤️ for the UIUC UIRP Hackathon")
