# coding: utf-8

'''Create instance of search class'''
from search import Search
s = Search(index_name='netflix')

'''Index data'''
s.index_data()

'''Obtain user input'''
keywords = input("Enter search keywords: ")

'''Search using user input'''
response = s.find(keywords)

'''Prepare search result'''
results = s.process_result(response)

'''Display result'''
for res in results:
    print('Title: ', res['title'])
    print('Director: ', res['director'])
    print('Rating: ', res['rating'])
    print('Description: ', res['description'])
    print('Duration: ', res['duration'])
    print('Cast: ', res['cast'])
    print()
