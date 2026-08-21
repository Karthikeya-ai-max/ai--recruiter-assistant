resume = input("Enter you resume: ")
resume = resume.lower()
Required_skill= []
Required_technology = []
Required_language = []
skills = ["machine learning", "artificial intelligence", "deep learning", "computer vision"]
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


  
  



