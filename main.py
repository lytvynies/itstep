import datetime
current_year = datetime.datetime.now()

from scipy.constants import speed_of_light

light_speed_in_vacuum = speed_of_light

quote = "\"Можливо все, неможливе просто потребує більше часу.\"\n Ден Браун"

oceans = ['Pacific', 'Atlantic', 'Infian', 'Southern', 'Arctic']

active = False

naming = ("i", "t", "s", "t", "e", "p")

# school = {"Neo": {"subjects": ["Python"]}, "Trinity", "Morpheus", "Mouse", "Tank"}
# school["subjects"]

print(current_year.strftime("%Y"))
print(light_speed_in_vacuum)
print(quote)
print(oceans)
print(active == False)
print(naming)
# print(school)