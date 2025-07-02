# 📚 Chalkboard – Your Smartest Course Planning Companion at UIUC

**Chalkboard** is an all-in-one interactive dashboard designed for UIUC students to **plan smarter**, **choose better professors**, and **build optimal schedules**—with the help of AI. Whether you're trying to find the best GPA-friendly instructor, read what other students are saying, or avoid time conflicts, Chalkboard makes it easy.

🧠 Built for the UIRP Hackathon 2025.

---

## 🌐 Live App

🎯 Experience it here: https://huggingface.co/spaces/sauravnayak/chalkboard-uirp-hackathon

---

## 🚀 Key Features

### 📊 GPA & Professor Insights
- Visualize **average GPAs by instructor** across multiple semesters  
- Compare **difficulty levels**, **RateMyProfessor ratings**, and **total student feedback**  
- Identify the most lenient graders or toughest professors using interactive Altair plots  

### 🤖 AI Reviews & Sentiment Analysis
- Enter a course code and get **AI-generated summaries** of student conversations from [r/UIUC](https://www.reddit.com/r/UIUC)  
- Each review highlights:  
  - ✅ Key pros and cons  
  - 💡 Must-know info  
  - 🎯 A **sentiment score** summarizing overall student perception

### 🗓️ Smart Visual Schedule Planner
- Drag-and-drop calendar lets you **build your week** visually  
- Automatic **time conflict detection**  
- Instantly switch between multiple instructors/sections  
- See additional **instructor insights** and **historical GPA data** for each lecture slot  

### 💬 Unified, Interactive Experience
- Clean tabbed layout for switching between:
  - **Overview**: AI reviews and GPA visualizations  
  - **Planner**: Schedule builder with course search  
  - **Insights**: Multi-course professor comparisons  
- Smooth animations, hover-based text enlargement, and responsive charts  

---

## 📦 Tech Stack

- **Frontend:** Streamlit, Altair, HTML/CSS  
- **AI Integration:** OpenAI API for Reddit review generation  
- **NLP:** NLTK (VADER) for sentiment scoring  
- **Data Handling:** Pandas, CSVs hosted on GitHub  
- **Deployment:** Hugging Face Spaces, Lovable.app

---

## 📊 Data Sources

- UIUC Grade Distribution Reports  
- RateMyProfessor Public API  
- Reddit posts from [r/UIUC](https://www.reddit.com/r/UIUC)

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Saurav51/chalkboard-uirp-hackathon.git
cd chalkboard-uirp-hackathon
pip install -r requirements.txt
streamlit run src/streamlit_app.py
