import csv

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


def run():
    with open('static/data/category.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = Category(name=row[1],
                                slug=row[2])
            category.save()
    with open('static/data/comments.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = Comment(review=row[1],
                               text=row[2],
                               author=row[3],
                               pub_date=row[4])
            category.save()
    with open('static/data/genre.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = Genre(name=row[1],
                             slug=row[2])
            category.save()
    with open('static/data/titles.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = Title(name=row[1],
                             year=row[2],
                             category=row[3])
            category.save()
    with open('static/data/genre_title.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = GenreTitle(title=row[1],
                                  genre=row[2])
            category.save()
    with open('static/data/review.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = Review(title=row[1],
                              text=row[2],
                              author=row[3],
                              score=row[4],
                              pub_date=row[6])
            category.save()
    with open('static/data/users.csv',
              encoding='cp1251',
              newline=''
              ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = User(username=row[1],
                            email=row[2],
                            role=row[3],
                            bio=row[4],
                            first_name=row[5],
                            last_name=row[6])
            category.save()
