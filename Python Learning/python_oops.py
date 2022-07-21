


# class webseries:
#     show_name = 'suites'
#     show_length = '189'
# web_series_obj = webseries()
# print(web_series_obj.show_name)
# print(web_series_obj.show_length)


class webseries:
    def __init__(self,name,season,episode):
        self.name = name
        self.season = season
        self.episode = episode
        print('i am hit')

web_1 = webseries("games of throns",1 ,1)
web_2 = webseries("hatim",1,2)
print(web_1.name,web_2.name)        