import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get("https://wuzzuf.net/search/jobs", headers=headers)
    soup = BeautifulSoup(response.content, "lxml")  # تأكد أنك سطبت lxml

    titles = soup.find_all("h2", {'class': 'css-m604qf'})
    titles_lst = [title.a.text.strip() for title in titles]
    links = ['https://wuzzuf.net' + title.a['href'] for title in titles]

    occupations = soup.find_all("div", {'class': 'css-y4udm8'})
    occupations_lst = [occupation.text.strip() for occupation in occupations]

    companies = soup.find_all("a", {'class': 'css-d7j1kk'})
    companies_lst = [company.text.strip() for company in companies]
    
    

    

    # ناخد أقل طول لتفادي الخطأ
    min_length = min(len(titles_lst), len(links), len(occupations_lst), len(companies_lst))

    scraped_data = {
        'Title': titles_lst[:min_length],
        'Link': links[:min_length],
        'Occupation': occupations_lst[:min_length],
        'Company': companies_lst[:min_length]
    }

    df = pd.DataFrame(scraped_data)
    df.to_csv('mljobs.csv', index=False, encoding='utf-8-sig')
    print("Jobs Scraped Successfully")
    return df

if __name__ == '__main__':
    scrap()
