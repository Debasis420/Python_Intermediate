#1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


#2 CONVERT FROM °C TO °F TEMP. USING CONDITIONAL DICTIONARY

# eval() converts correctly formatted string to dict but we have give the input value below:
# weather_c = eval(input()) 
weather_c =  {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}
# dictionary comprehension
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

#3. How to Iterate over a Pandas DataFrame