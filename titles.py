import scrap_jobs
#edit
def get_titles():
    df = scrap_jobs.scrap()
    titles_lst = df['Title'].tolist()
    return titles_lst

if __name__ == '__main__':
    print(get_titles())
