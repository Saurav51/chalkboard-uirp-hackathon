import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Schoolbell&display=swap');

.chalkboard-wrapper {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
}

.chalkboard-heading {
    font-family: 'Schoolbell', cursive;
    font-size: 48px;
    color: #fff;
    background-color: #2b2b2b;
    padding: 20px 40px;
    border-radius: 12px;
    box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.05), 0 4px 12px rgba(0,0,0,0.4);
    text-shadow: 1px 1px 2px rgba(255,255,255,0.08);
    max-width: 600px;
    width: fit-content;
    text-align: center;
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
</style>

<div class="chalkboard-wrapper">
  <div class="chalkboard-heading"> ✏️ Chalkboard</div>
</div>
""", unsafe_allow_html=True)


# Enhanced Tab Styling and Initialization
st.markdown("""
<style>
/* Custom tab container */
.stTabs [data-baseweb="tab-list"] {
    gap: 25px;
    justify-content: center;
    margin-bottom: 20px;
}

/* Tab text style */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 500;
    color: #444;
    padding: 12px 20px;
    border-radius: 10px 10px 0 0;
    background-color: #f0f2f6;
    transition: all 0.3s ease;
}

/* Tab hover effect */
.stTabs [data-baseweb="tab"]:hover {
    font-size: 19px;
    background-color: #e2ecf9;
    color: #003366;
    transform: scale(1.05);
    cursor: pointer;
}

/* Active tab */
.stTabs [aria-selected="true"] {
    background-color: #FF8b60 !important;
    color: white !important;
    font-weight: bold;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# Create the tabs
tab1, tab2, tab3 = st.tabs(["🔍 Overview", "📆 Planner", "📊 Insights"])

with tab1:
    st.markdown("""
    <style>
        .block-container {
            padding: 2rem;
            max-width: 90%;
        }
        h1, h2, h3, h4 {
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            font-size: 48px;
            color: #FF4500;
            text-align: center;
            margin-bottom: 1rem;
        }
        h2 {
            font-size: 32px;
            color: #003366;
            border-bottom: 2px solid #FF4500;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
        }
        .stTextInput label, .stSelectbox label, .stButton label {
            font-size: 18px;
        }
        .stMarkdown {
            font-size: 18px;
            line-height: 1.6;
        }
        .stButton>button {
            background-color: #FF8b60;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #FFA07A;
        }
    </style>
    """, unsafe_allow_html=True)

    
    course_code = st.selectbox("Choose a course", ["MATH 231", "MATH 257", "CS 124", "STAT 107", "ECON 102", "IS 445"])

    # Load and prepare data
    df = pd.read_csv("https://raw.githubusercontent.com/Saurav51/chalkboard-uirp-hackathon/main/datasets/viz1.csv")
    df['Course'] = df['Subject'] + " " + df['Number'].astype(str)
    df['Instructor'] = df['Primary Instructor']        
    # Hardcode course
    selected_course = "MATH 231"
    filtered_df = df[df['Course'] == course_code]
        
    # Dynamically calculate chart dimensions
    num_instructors = filtered_df.shape[0]
    chart_height = max(300, num_instructors * 45)
    chart_width = 700 if num_instructors > 15 else 500
        
    # GPA bar chart
    gpa_chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X('Overall_GPA:Q', title='Average GPA', scale=alt.Scale(domain=[0, 4])),
        y=alt.Y('Instructor:N', sort='-x', title='Instructor'),
        color=alt.Color('Overall_GPA:Q', scale=alt.Scale(scheme='blues')),
        tooltip=[
            alt.Tooltip('Instructor:N'),
            alt.Tooltip('Overall_GPA:Q', title='GPA'),
            alt.Tooltip('Total_Students:Q', title='Students'),
            alt.Tooltip('A_range:Q', title='A %', format=".1f"),
            alt.Tooltip('B_range:Q', title='B %', format=".1f"),
            alt.Tooltip('C_range:Q', title='C %', format=".1f"),
            alt.Tooltip('D_range:Q', title='D %', format=".1f"),
            alt.Tooltip('F_range:Q', title='F %', format=".1f"),
        ]
    ).properties(
        width=chart_width,
        height=chart_height,
        title=f'GPA by Instructor for {selected_course}'
    )

    st.markdown("""
    #### Curious how your professor's grading compares to others? 
    
    The bar chart below displays the **average GPA by instructor** for the selected course based on historical grade distribution data at UIUC. It helps students make informed decisions by identifying which professors tend to grade more leniently or strictly. Hover over each bar to see detailed statistics on grade percentages and student counts.
    """)
    st.altair_chart(gpa_chart, use_container_width=True)
    
    # client = OpenAI(
    #   base_url="https://openrouter.ai/api/v1",
    #   api_key="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",
    # )
    
    # @st.cache_data(ttl=14400)  # Cache for 12 hour
    # def getUIUCRedditOverview(courseCode):
    #   prompt = f"Can you give me reviews on {courseCode} course based on conversations on this reddit page: https://www.reddit.com/r/UIUC/?"
    #   prompt += "Do not keep it too long. Just a few positive aspects, negative aspects and things that students must know."
    
    #   completion = client.chat.completions.create(
    #     extra_headers={
    #       "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    #       "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    #     },
    #     extra_body={},
    #     model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    #     messages=[
    #       {
    #         "role": "user",
    #         "content": prompt 
    #       }
    #     ]
    #   )
    #   return completion.choices[0].message.content
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("💬 Class Reviews from Reddit")
    # reddit_ai_output = getUIUCRedditOverview(course_code)
    # st.write(reddit_ai_output)   
    

with tab2:
    components.iframe("https://illini-schedule-planner.lovable.app", height=600, width=1200, scrolling=True)

with tab3:
    st.subheader("GPA comparsion across Professors")

    st.markdown("""
        This visualization helps you:
        
        - **Compare average GPAs** awarded by different professors teaching the same course, helping you estimate your potential grade based on past trends
        - **Make strategic course choices** by factoring in historical GPA distributions alongside RateMyProfessor insights and difficulty ratings
        - **Plan your semester wisely** by identifying professors whose grading aligns with your academic goals
        - **Distinguish instructors** easily with color-coded bars that highlight grading differences within and across courses
        
    """)

    df = pd.read_csv("https://raw.githubusercontent.com/Saurav51/chalkboard-uirp-hackathon/main/datasets/fa25_profs_gpa_rmp.csv")
    bar_size=40
    height=400
    extra_padding=1.2

    courses = ["MATH231", "MATH257", "CS124", "STAT107", "ECON102", "IS445"]
    selected_courses = st.multiselect("Select one or more courses", courses)
    df = df[df["course_code"].isin(selected_courses)]

    df['instr_idx']  = df.groupby('course_code').cumcount()
    df['group_size'] = df.groupby('course_code').course_code.transform('count')
    df['x_offset']   = (df['instr_idx'] - (df['group_size'] - 1) / 2) * bar_size

    max_cluster = df['group_size'].max()
    # how many pixels between the *centers* of adjacent course‐clusters?
    step = max_cluster * bar_size * extra_padding

    hover = alt.selection_single(on='mouseover', nearest=True, empty='none')

    chart = alt.Chart(df).mark_bar(size=bar_size).encode(
              x=alt.X(
                'course_code:O',
                axis=alt.Axis(labelAngle=-45, title='Course'),
                sort=None,
                scale=alt.Scale(
                  paddingInner=0.45,       # no extra gap between bars in the same cluster
                  paddingOuter=0.25      # **THIS** pushes all clusters in by half a band
                )
              ),
              xOffset=alt.XOffset('x_offset:Q'),
              y=alt.Y('weighted_gpa:Q', axis=alt.Axis(title='Weighted GPA')),
              color=alt.Color('primary_instructor:N', title='Professor'),
              opacity=alt.condition(hover, alt.value(1.0), alt.value(0.6)),
              tooltip=[
                alt.Tooltip('course_code:N', title='Course'),
                alt.Tooltip('course_title:N', title='Title'),
                alt.Tooltip('primary_instructor:N', title='Professor'),
                alt.Tooltip('weighted_gpa:Q', title='Weighted GPA', format='.2f'),
                alt.Tooltip('rating:Q', title='RMP Rating', format='.2f'),
                alt.Tooltip('level_of_difficulty:Q', title='Difficulty', format='.1f'),
                alt.Tooltip('would_take_again:Q', title='Would Take Again', format='.2f'),
                alt.Tooltip('total_ratings:Q', title='Total Ratings', format='d'),
              ]
            ).add_selection(hover).properties(
              height=height,
              title='Weighted GPA by Course and Professor'
            ).configure_title(fontSize=18, anchor='middle')

    st.altair_chart(chart, use_container_width=True)
