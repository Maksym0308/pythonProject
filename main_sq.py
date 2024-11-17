import json
import requests
from lxml import html
import sqlite3
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from postgresql import NEON_PASSWORD

def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    print(response.status_code)
    return response.text

def extract_job_titles(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    titles = tree.xpath('//h3[@class="jobCard_title m-0"]/text()')
    return [title.strip() for title in titles]

def get_job_links(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    links = tree.xpath('//a[contains(@class, "jobCard_link")]/@href')

    full_links = [link for link in links]

    return full_links

def write_json(job_titles, job_links) -> None:
    data ={
        'job_titles': job_titles,
         'job_links' : job_links,
        }


    with open('output.json', 'w', encoding= 'utf-8') as file:
        json.dump(data, file, ensure_ascii=False ,indent= 4)

def write_sql(data: list) -> None:
    filename = 'output.db'
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    sql = '''
        create table if not exists job (
        id integer primary key,
        first_title text,
        first_url text
        )
    '''
    cursor.execute(sql)
    for item in data:
        cursor.execute('''
        insert into job(first_title, first_url)
        values(?, ?)
        ''', (item[0], item[1])
             )
    conn.commit()
    conn.close()

def write_sqlalchemy(data: list) -> None:
    # filename = 'sqlalchemy.db'
    engine = create_engine(f'postgresql://neondb_owner:{NEON_PASSWORD}@ep-square-hill-a5k8jyzi.us-east-2.aws.neon.tech/neondb?sslmode=require')


    Base = declarative_base()

    class Person(Base):
        __tablename__ = 'job'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        url = Column(String)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in data:
        job = Person(
            title = item[0],
            url = item[1]
        )

        session.add(job)

    session.commit()
    session.close()

def main():

    url = "https://www.lejobadequat.com/emplois"

    job_titles = extract_job_titles(url)
    print(job_titles)

    url = "https://www.lejobadequat.com/emplois"
    job_links = get_job_links(url)
    print(job_links)

    write_json(job_titles,job_links)

    data = list(zip(job_titles,job_links))
    write_sql(data)

    data = list(zip(job_titles, job_links))
    write_sqlalchemy(data)


if __name__ == '__main__':
    main()


