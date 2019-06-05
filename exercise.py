items = [
{'id': "38fj8d900", 'city': 'Hamilton', 'events': [{'date': '2017-01-01', 'attendees': 100}, {'date': '2016-12-31', 'attendees': 60}]},
{'id': "39fo837y7", 'city': 'Toronto', 'events': [{'date': '2017-03-30', 'attendees': 3000}, {'date': '2017-07-07', 'attendees': 2500}, {'date': '2017-02-04', 'attendees': 900}]},
{'id': "58uj8d800", 'city': 'Montreal', 'events': [{'date': '2017-08-10', 'attendees': 250}]},
{'id': "48hn8d900", 'city': 'Kingston', 'events': [{ 'date': '2015-04-16', 'attendees': 45}]}
]

# Hamilton
# ------------
# Date: 2017-01-01, 100 people 
# Date: 2016-12-31, 60 people 

# Toronto
# ------------
# Date: 2017-03-30, 3000 people 
# Date: 2017-07-07, 2500 people 
# Date: 2017-02-04, 900 people 

# [
#     {'city':'Hamilton', 'dates':[{'2017-01-01': 100},{' 2016-12-3':60}]},
#     {},
# ]
# our = []
# for item in items:
#     my_dict = {}
#     city_name = item['city']
#     my_dict['town'] = city_name
#     details = []
#     for event in item['events']:
#         my_dict_2 = {}
#         key = event['date']
#         my_dict_2[key] = event['attendees']
#         details.append(my_dict_2)
#     my_dict['dates'] = details
#     our.append(my_dict)
# print(our)

for item in items:
    print(item['city'])
    print('-----------------------')
    for event in item['events']:
        print('Date: ', event['date'], ', ', event['attendees'], ' people', sep='')
    print()


