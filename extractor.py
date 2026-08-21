resume = input("Enter you resume: ")
resume = resume.lower()
Required_skill= []
Required_technology = []
Required_language = []
role = []
skills = ["machine learning", "ai/ml", "deep learning", "computer vision"]
technologies = ["pytorch", "cnn", "tensorflow"]
languages = ["C++", "python", "java", "javascript"]
for skill in skills:
  if skill in resume:
    Required_skill.append(skill)
for technology in technologies:
  if technology in resume:
    Required_technology.append(technology)
for language in languages:
  if language in resume:
    Required_language.append(language)

print(f"Skills: {Required_skills}")
print(f"technologies: {Required_technologies}")
print(f"languages: {Required_languages}")

if "ai/ml" or "machine learning" in Required_skill:
  role = "machine learning engineer"
elif "computer vision" or "cnn" in Required_skill:
  role = "compuer vision engineer"
else:
  role = "software developer"
print(f"Suggested role: {role})


  
  



