# 🏛️ Heritage Treasures - UNESCO World Heritage Data Analytics

An interactive web application and data analytics platform for visualizing, exploring, and analyzing **UNESCO World Heritage Sites** globally. Built using HTML5, CSS3, JavaScript, Leaflet GIS, Chart.js, and Flask.

---

## 🌟 Overview

The **Heritage Treasures** platform provides comprehensive data analytics on **1,157+ UNESCO World Heritage Sites** across **167 State Parties**. It helps researchers, UNESCO stakeholders, students, and cultural preservation authorities quickly analyze regional distributions, category breakdowns (Cultural, Natural, Mixed), danger statuses, and historical inscription trends over time.

---

## ✨ Features

- **📊 KPI Metric Cards:** Real-time summary of Total Sites, Cultural Sites, Natural Sites, and Endangered Sites.
- **📈 Interactive Analytics Charts:**
  - Category Distribution (Doughnut Chart)
  - Regional Distribution Across Continents (Bar Chart)
  - Inscription Growth Trends from 1978 to 2024 (Line Chart)
  - Endangered Risk Status Assessment (Pie Chart)
  - Top 10 Countries by Heritage Site Count (Horizontal Bar Chart)
- **🗺️ Interactive Map Explorer:** Leaflet GIS map with custom color-coded map markers for spatial visualization.
- **🔍 Dynamic Directory Engine:** Search by site or country name with instant multi-criteria filtering by Region, Category, and Risk Status.
- **📄 Embedded Project Documentation:** Quick access to problem statements, solution architecture, and data preprocessing steps.

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism theme), JavaScript (ES6+), FontAwesome
- **Data Visualization & GIS:** Chart.js, Leaflet.js
- **Backend Web Server:** Python (Flask) / Standard HTTP Server

---

## 🚀 How to Run Locally

### Option 1: Using Flask (Recommended)
```bash
# 1. Install dependencies
pip install flask pandas

# 2. Run the application
python app.py
```
Open your browser and navigate to: `http://localhost:5000`

### Option 2: Using Python Built-in HTTP Server
```bash
python -m http.server 8000
```
Open your browser and navigate to: `http://localhost:8000`

---

## 📁 Repository Structure

```
Heritage-Treasures-main/
├── Data Analytics Project/             # Academic deliverables & PDF reports
│   ├── Assignment/                     # Team assignments (Avanthi, Madhava Sai, Praveen, Revanth)
│   ├── Brain Storming and Ideation/   # Problem statements & empathy map
│   ├── Requirement Analysis/           # Customer journey map, DFDs, user stories
│   ├── Project Planning Phase/         # Backlog & sprint schedule
│   ├── Project Design Phase/           # Solution architecture
│   ├── Project Development phase/      # Preprocessing steps & Tableau exports
│   ├── Performance Testing/            # Verification reports
│   ├── Project Documentation/          # Comprehensive final report
│   └── Project Demonstration/          # Video demonstration link
├── index.html                          # Interactive Web Dashboard frontend
├── app.py                              # Flask Web Server entry point
└── README.md                           # Project documentation
```

---

## 👥 Team Members

- **Praveen (Team Leader)**
- **Avanthi**
- **Madhava Sai**
- **Revanth**
