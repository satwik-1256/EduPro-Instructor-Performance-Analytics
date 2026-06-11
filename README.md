# 🎓 EduPro Instructor Performance & Course Quality Analytics Dashboard

## 📌 Project Overview

This project analyzes instructor performance, course quality, and learner engagement on the EduPro online learning platform. The objective is to identify factors influencing course success, evaluate instructor effectiveness, and generate actionable insights for improving educational outcomes.

The project combines Exploratory Data Analysis (EDA), statistical analysis, and an interactive Streamlit dashboard to support data-driven decision-making.

---

## 🎯 Project Objectives

* Evaluate instructor performance across different expertise domains.
* Analyze the relationship between teaching experience and ratings.
* Assess course quality using learner ratings.
* Identify top-performing and low-performing instructors.
* Measure the impact of instructor quality on enrollment trends.
* Provide interactive analytics for educational stakeholders.

---

## 📊 Dataset Information

The dataset consists of four interconnected sheets:

### Teachers

* TeacherID
* TeacherName
* Age
* Gender
* Expertise
* YearsOfExperience
* TeacherRating

### Courses

* CourseID
* CourseName
* CourseCategory
* CourseType
* CourseLevel
* CoursePrice
* CourseDuration
* CourseRating

### Transactions

* TransactionID
* UserID
* CourseID
* TransactionDate
* Amount
* PaymentMethod
* TeacherID

### Users

* UserID
* UserName
* Age
* Gender
* Email

---

## 🔍 Key Analytical Questions

* What is the overall distribution of instructor ratings?
* Do instructors with more experience receive higher ratings?
* Is there a relationship between Teacher Rating and Course Rating?
* Which expertise areas consistently deliver high-quality courses?
* Are highly rated instructors associated with higher enrollments?

---

## 📈 Dashboard Features

### KPI Dashboard

* Average Teacher Rating
* Average Course Rating
* Average Teaching Experience
* Total Teachers
* Total Courses
* Total Transactions

### Interactive Filters

* Expertise Filter
* Gender Filter

### Visual Analytics

* Teacher Rating Distribution
* Experience vs Teacher Rating Analysis
* Teacher Age Distribution
* Gender-wise Performance Analysis
* Expertise-wise Average Ratings
* Course Category Analysis
* Course Level Analysis
* Course Quality Heatmap
* Enrollment vs Teacher Rating Analysis
* Enrollment by Expertise
* Course Price vs Rating Analysis

### Instructor Insights

* Top 10 Instructors
* Bottom 10 Instructors

### Additional Features

* Dataset Preview
* CSV Download Option

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* OpenPyXL
* Jupyter Notebook

---

## 📁 Repository Structure

```text
EduPro-Instructor-Performance-Analytics
│
├── app.py
├── requirements.txt
├── EduPro_Analysis.ipynb
├── Research_Paper.pdf
├── Dashboard_Screenshots
└── README.md
```

## 🚀 Streamlit Dashboard

Run locally using:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Key Insights

* Instructor ratings show a positive relationship with course ratings.
* Experienced instructors generally achieve higher learner satisfaction.
* Certain expertise domains consistently outperform others.
* Higher-rated instructors attract greater enrollment volumes.
* Course quality significantly influences learner engagement.

---

## 📷 Dashboard Preview

Add screenshots of your dashboard here after uploading them to GitHub.

---

## 👨‍💻 Author

**Satwik Srivastava**

* Data Analyst Intern
* Unified Mentor

---

## 📄 License

This project is developed for educational, research, and portfolio purposes.
