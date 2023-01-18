from bs4 import BeautifulSoup
from flask import Flask,request
import requests
import time

# print("Put some skill that you are not familiar with")
# unfamiliar_skill = input('>')
# print(f"Filtering out {unfamiliar_skill}")

url="http://127.0.0.1:3000/job"

def find_jobs():
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
    soup = BeautifulSoup(html_text.content,'html.parser')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = "sim-posted").span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','').replace('\n','').replace('\r','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','').replace('\n','').replace('\r','')
            more_info = job.header.h2.a['href']

            data = {
                "Company Name": company_name,
                "Skills": skills,
                "More Info": more_info
            }
            postJob(data)
            # with open(f'posts/{index}.txt','w') as f:
            #         f.write(f"Company Name {company_name.strip()}\n")
            #         f.write(f"Required Skills:{skills.strip()}\n")
            #         f.write(f"More info:{more_info}\n")
            #         print(' ')

        
def postJob(data):
    response = requests.post(url,json=data)
    print(response)


if __name__ == '__main__':

    while True:
        find_jobs()
       
