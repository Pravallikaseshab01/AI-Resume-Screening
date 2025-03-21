# import csv
# import random

# # Lists of components to generate additional entries
# technologies = [
#     "Python", "Java", "JavaScript", "TypeScript", "Go", "C#", "C++", "Swift", "Kotlin",
#     "React", "Angular", "Vue.js", "Next.js", "Node.js", "Django", "Flask", "Spring Boot",
#     "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform", "SQL", "MongoDB", "PostgreSQL"
# ]

# experience_levels = ["Entry-Level", "Junior", "Mid-Level", "Senior", "Lead", "Principal"]
# years_of_experience = ["1 year", "2 years", "3 years", "4 years", "5+ years", "6+ years", "10+ years"]

# skills = [
#     "Microservices", "Serverless", "CI/CD", "Cloud Computing", "Scalability", "Machine Learning",
#     "Deep Learning", "Natural Language Processing", "Computer Vision", "Data Visualization",
#     "Web Development", "Mobile Development", "UI/UX Design", "A/B Testing", "Security Practices"
# ]

# education_levels = ["High School Diploma", "Bachelor's Degree", "Master's Degree", "PhD"]
# education_fields = ["Computer Science", "Information Technology", "Software Engineering", "Data Science"]

# certifications = [
#     "AWS Certified Solutions Architect", "Azure Developer Associate", "GCP Professional Cloud Architect",
#     "CompTIA Security+", "Certified Ethical Hacker (CEH)", "Scrum Master", "Kubernetes Administrator (CKA)"
# ]

# locations = [
#     "New York, NY", "San Francisco, CA", "Seattle, WA", "Austin, TX", "Boston, MA", "Remote"
# ]

# job_titles = [
#     "Software Engineer", "Frontend Developer", "Full Stack Developer", "Data Scientist", "ML Engineer",
#     "Data Engineer", "DevOps Engineer", "Cybersecurity Engineer", "Mobile Developer", "Project Manager"
# ]

# work_arrangements = ["On-site", "Remote", "Hybrid"]
# industries = ["Technology", "Finance", "Healthcare", "E-commerce", "Education"]
# company_sizes = ["Startup", "Small", "Medium", "Large", "Enterprise"]

# def generate_resume_entry():
#     title = random.choice(job_titles)
#     tech = random.choice(technologies)
#     experience_level = random.choice(experience_levels)
#     years = random.choice(years_of_experience)
#     skill = random.choice(skills)
#     education = random.choice(education_levels)
#     field_of_study = random.choice(education_fields)
#     location = random.choice(locations)
#     certification = random.choice(certifications) if random.random() > 0.4 else ""
#     work_arrangement = random.choice(work_arrangements)
#     industry = random.choice(industries)
#     company_size = random.choice(company_sizes)

#     # Generate a list of random skills (3 to 5 skills per entry)
#     selected_skills = random.sample(skills, random.randint(3, 5))
#     skills_str = ", ".join(selected_skills)

#     return [
#         f"{experience_level} {title} with expertise in {tech} and {skill}", title,
#         years, education, field_of_study, location, certification, work_arrangement,
#         industry, company_size, skills_str  # Removed 'Applied Date'
#     ]

# # Generate 500 new records
# new_data = [generate_resume_entry() for _ in range(500)]

# # Save to CSV file
# with open("resume_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     # Ensure the "Skills" column is included in the header
#     writer.writerow(["Description", "Job Title", "Experience", "Education Level", "Field of Study",
#                      "Location", "Certification", "Work Arrangement", "Industry", 
#                      "Company Size", "Skills"])  # Removed 'Applied Date' column

#     writer.writerows(new_data)

# print("Generated resume data saved to resume_data.csv")

import pandas as pd

# Define job listings with properly formatted skills
job_data = [
    {
        "Job Title": "Machine Learning Engineer",
        "Location": "New York, NY",
        "Skills": "python, machine learning, deep learning, tensorflow, pandas, numpy"
    },
    {
        "Job Title": "Software Developer",
        "Location": "San Francisco, CA",
        "Skills": "java, spring boot, microservices, rest api, sql, git"
    },
    {
        "Job Title": "Data Analyst",
        "Location": "Austin, TX",
        "Skills": "sql, powerbi, excel, data visualization, python, statistics"
    },
    {
        "Job Title": "Frontend Developer",
        "Location": "Seattle, WA",
        "Skills": "html, css, javascript, react, angular, bootstrap"
    },
    {
        "Job Title": "Cybersecurity Analyst",
        "Location": "Boston, MA",
        "Skills": "cybersecurity, ethical hacking, network security, kali linux"
    },
]

# Convert to DataFrame
df = pd.DataFrame(job_data)

# Save to CSV file
df.to_csv("resume_data.csv", index=False)

print("✅ resume_data.csv successfully created!")
