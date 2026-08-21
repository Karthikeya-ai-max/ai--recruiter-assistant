resume = input("Enter you resume: ")
Required_skill= []
Required_technology = []
Required_language = []
role = []
skills = ["Machine learning", "AI/ML", "Deep learning", "Computer vision"]
technologies = ["Pytorch", "CNN", "Tensorflow"]
languages = ["C++", "Python", "Java", "Javascript"]
for skill in skills:
  if skill in resume:
    Required_skill.append(skill)
for technology in technologies:
  if technology in resume:
    Required_technology.append(technology)
for language in languages:
  if language in resume:
    Required_language.append(language)

print(f"Skills: {Required_skill}")
print(f"technologies: {Required_technology}")
print(f"languages: {Required_language}")

if "AI/ML" in Required_skill or "Machine learning" in Required_skill:
  role = "machine learning engineer"
elif "Computer vision" in Required_skill or "CNN" in Required_skill:
  role = "Compuer vision engineer"
else:
  role = "software developer"
print(f"Suggested role: {role}")


  
  



