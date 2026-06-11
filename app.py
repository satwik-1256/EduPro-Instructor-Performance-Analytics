import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use("ggplot")

# PAGE CONFIG
st.set_page_config(
    page_title="EduPro Instructor Analytics Dashboard",
    layout="wide")
st.title("🎓 Instructor Performance & Course Quality Evaluation Dashboard")
st.markdown(
    "Interactive analytics dashboard for evaluating instructor performance, course quality, and enrollment trends.")
st.info("""
🎯 Project Objective
Evaluate instructor performance, course quality, learner engagement, and enrollment trends to identify high-performing educators, improve course effectiveness, and support data-driven decision-making on the EduPro platform.
""")

# LOAD DATA
excel_file = "EduPro Dataset.xlsx"
teachers = pd.read_excel(excel_file, sheet_name="Teachers")
courses = pd.read_excel(excel_file, sheet_name="Courses")
transactions = pd.read_excel(excel_file, sheet_name="Transactions")
users = pd.read_excel(excel_file, sheet_name="Users")

# MERGE DATA
teacher_transactions = transactions.merge(
    teachers,
    on="TeacherID",
    how="left")

# SIDEBAR FILTERS
st.sidebar.header("Dashboard Filters")
selected_expertise = st.sidebar.selectbox(
    "Select Expertise",
    ["All"] + sorted(teachers["Expertise"].unique().tolist()))
selected_gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + sorted(teachers["Gender"].unique().tolist()))
selected_category = st.sidebar.selectbox(
    "Select Course Category",
    ["All"] + sorted(courses["CourseCategory"].unique().tolist()))
selected_level = st.sidebar.selectbox(
    "Select Course Level",
    ["All"] + sorted(courses["CourseLevel"].unique().tolist()))
rating_range = st.sidebar.slider(
    "Teacher Rating Range",
    float(teachers["TeacherRating"].min()),
    float(teachers["TeacherRating"].max()),(
        float(teachers["TeacherRating"].min()),
        float(teachers["TeacherRating"].max())))
filtered_teachers = teachers.copy()
if selected_expertise != "All":
    filtered_teachers = filtered_teachers[
        filtered_teachers["Expertise"] == selected_expertise]
if selected_gender != "All":
    filtered_teachers = filtered_teachers[
        filtered_teachers["Gender"] == selected_gender]
filtered_teachers = filtered_teachers[
    (filtered_teachers["TeacherRating"] >= rating_range[0]) &
    (filtered_teachers["TeacherRating"] <= rating_range[1])]
filtered_courses = courses.copy()
if selected_category != "All":
    filtered_courses = filtered_courses[
        filtered_courses["CourseCategory"] == selected_category]
if selected_level != "All":
    filtered_courses = filtered_courses[
        filtered_courses["CourseLevel"] == selected_level]

# KPI SECTION
st.subheader("📊 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col1.metric(
    "Average Teacher Rating",
    round(filtered_teachers["TeacherRating"].mean(), 2))
col2.metric(
    "Average Course Rating",
    round(filtered_courses["CourseRating"].mean(), 2))
col3.metric(
    "Average Experience",
    round(filtered_teachers["YearsOfExperience"].mean(), 2))
col4.metric(
    "Total Teachers",
    len(filtered_teachers))
col5.metric(
    "Total Courses",
    len(filtered_courses))
col6.metric(
    "Total Transactions",
    len(transactions))

# DASHBOARD SUMMARY
st.subheader("📈 Dashboard Summary")
summary_col1, summary_col2, summary_col3 = st.columns(3)
summary_col1.metric(
    "Highest Teacher Rating",
    round(filtered_teachers["TeacherRating"].max(), 2))
summary_col2.metric(
    "Lowest Teacher Rating",
    round(filtered_teachers["TeacherRating"].min(), 2))
summary_col3.metric(
    "Average Course Price",
    round(filtered_courses["CoursePrice"].mean(), 2))

# TEACHER RATING DISTRIBUTION
st.subheader("Teacher Rating Distribution")
fig1, ax1 = plt.subplots(figsize=(8,4))
sns.histplot(
    filtered_teachers["TeacherRating"],
    bins=10,
    kde=True,
    ax=ax1)
st.pyplot(fig1)

# EXPERIENCE VS RATING
st.subheader("Experience vs Teacher Rating")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.scatterplot(
    data=filtered_teachers,
    x="YearsOfExperience",
    y="TeacherRating",
    ax=ax2)
st.pyplot(fig2)

# AGE DISTRIBUTION
st.subheader("Teacher Age Distribution")
fig3, ax3 = plt.subplots(figsize=(8,4))
sns.histplot(
    filtered_teachers["Age"],
    bins=10,
    kde=True,
    ax=ax3)
st.pyplot(fig3)

# GENDER ANALYSIS
st.subheader("Teacher Rating by Gender")
fig4, ax4 = plt.subplots(figsize=(8,5))
sns.boxplot(
    data=filtered_teachers,
    x="Gender",
    y="TeacherRating",
    ax=ax4)
st.pyplot(fig4)

# EXPERTISE ANALYSIS
st.subheader("Expertise-wise Average Rating")
expertise_rating = (
    filtered_teachers.groupby("Expertise")["TeacherRating"]
    .mean()
    .sort_values(ascending=False))
fig5, ax5 = plt.subplots(figsize=(10,5))
expertise_rating.plot(
    kind="bar",
    ax=ax5)
st.pyplot(fig5)

# COURSE CATEGORY ANALYSIS
st.subheader("Course Category vs Course Rating")
category_rating = (
    filtered_courses.groupby("CourseCategory")["CourseRating"].mean())
fig6, ax6 = plt.subplots(figsize=(10,5))
category_rating.plot(
    kind="bar",
    ax=ax6)
st.pyplot(fig6)

# COURSE LEVEL ANALYSIS
st.subheader("Course Level vs Course Rating")
level_rating = (
    filtered_courses.groupby("CourseLevel")["CourseRating"]
    .mean())
fig7, ax7 = plt.subplots(figsize=(8,5))
level_rating.plot(
    kind="bar",
    ax=ax7)
st.pyplot(fig7)

# COURSE QUALITY HEATMAP
st.subheader("Course Quality Heatmap")
if not filtered_courses.empty:
    heatmap_data = filtered_courses.pivot_table(
        values="CourseRating",
        index="CourseCategory",
        columns="CourseLevel",
        aggfunc="mean")
    fig8, ax8 = plt.subplots(figsize=(10,6))
    sns.heatmap(
        heatmap_data,
        annot=True,
        cmap="YlGnBu",
        ax=ax8)
    st.pyplot(fig8)
else:
    st.warning("No courses available for the selected filters.")

# TOP INSTRUCTOR
st.subheader("🏆 Top 10 Instructors")
top_teachers = (
    teachers.sort_values(
        by="TeacherRating",
        ascending=False).head(10))
st.dataframe(
    top_teachers[[
            "TeacherName",
            "Expertise",
            "TeacherRating",
            "YearsOfExperience"]])

# BOTTOM INSTRUCTORS
st.subheader("📉 Bottom 10 Instructors")
bottom_teachers = (
    teachers.sort_values(
        by="TeacherRating",
        ascending=True).head(10))
st.dataframe(
    bottom_teachers[[
            "TeacherName",
            "Expertise",
            "TeacherRating",
            "YearsOfExperience"]])

# ENROLLMENT ANALYSIS
st.subheader("Teacher Rating vs Enrollment")
teacher_enrollment = (
    teacher_transactions.groupby(
        ["TeacherName", "TeacherRating"])
    .size()
    .reset_index(name="EnrollmentCount"))
fig9, ax9 = plt.subplots(figsize=(8,5))
sns.scatterplot(
    data=teacher_enrollment,
    x="TeacherRating",
    y="EnrollmentCount",
    ax=ax9)
st.pyplot(fig9)

# ENROLLMENT BY EXPERTISE
st.subheader("Enrollment by Expertise")
expertise_enrollment = (
    teacher_transactions.groupby("Expertise")
    .size()
    .sort_values(ascending=False))
fig10, ax10 = plt.subplots(figsize=(10,5))
expertise_enrollment.plot(
    kind="bar",
    ax=ax10)
st.pyplot(fig10)
top_expertise = expertise_enrollment.idxmax()
st.success(
    f"🏆 Highest enrollment is observed in the {top_expertise} expertise domain.")

# COURSE PRICE VS RATING
st.subheader("Course Price vs Rating")
fig11, ax11 = plt.subplots(figsize=(8,5))
sns.scatterplot(
    data=filtered_courses,
    x="CoursePrice",
    y="CourseRating",
    ax=ax11)
st.pyplot(fig11)

# DATASET PREVIEW
st.subheader("Filtered Teachers Dataset Preview")
st.dataframe(filtered_teachers.head(20))

# DOWNLOAD DATASET
csv = filtered_teachers.to_csv(index=False)
st.download_button(
    label="Download Teachers Dataset",
    data=csv,
    file_name="teachers_dataset.csv",
    mime="text/csv")
course_csv = filtered_courses.to_csv(index=False)
st.download_button(
    label="Download Courses Dataset",
    data=course_csv,
    file_name="courses_dataset.csv",
    mime="text/csv")

# FOOTER
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <h4>🎓 EduPro Instructor Performance & Course Quality Analytics Dashboard</h4>
        <p>Developed by <b>Satwik Srivastava</b></p>
        <p>Python | Pandas | Seaborn | Matplotlib | Streamlit</p>
    </div>""",
    unsafe_allow_html=True)