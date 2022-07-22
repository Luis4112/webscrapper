from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://pt.indeed.com/?r=us"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.findAll("div", class_ = "jobsearch-SerpJobcard")

print(results)

Salary =" "

with open('jobs.csv', 'w', newline= " ", encoding = 'UTF8') as f:
    thewriter = writer(f)
    header =['Title', 'Company', 'Salary'] 
    thewriter.writerow(header) 

for result in results:
    title =  result.find("a", class_ = "job title").text.replace("\n", "")
    company = result.find("span", class_ = "company").text.replace("\n", "")
    salary1 = result.find("span", class_ = "salaryText")
if salary1:
    salary1 = salary1.text.replace('\n', "")
else:
    salary = 'Not mentioned'

jobinfo =[title, company, salary]
thewriter.writerow(jobinfo)



for result in results:
    title =  result.find("a", class_ = "job title")
    company = result.find("span", class_ = "company")
    salary = result.find("span", class_ = "salaryText")
    print("Position: {title.text}")
    print("Company: {company.text}")
if salary:
    print("Salary: {salary.text}",end= '\n'*2)
else:
    print("salary not mentioned",end= '\n'*2)

