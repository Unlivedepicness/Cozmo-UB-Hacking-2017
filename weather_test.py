from weather import *

weather = Weather()

loc = 'starcraft'

location = weather.lookup_by_location(loc)
condition = location.condition()

print("currently " + condition['text'])

forecasts = location.forecast()

print("today in " + loc + " the weather is")
print(forecasts[0].text())
print("with a high of " + forecasts[0].high())
print("and a low of " + forecasts[0].low())

print("tomorrow the weather is")
print(forecasts[1].text())
print("with a high of " + forecasts[1].high())
print("and a low of " + forecasts[1].low())