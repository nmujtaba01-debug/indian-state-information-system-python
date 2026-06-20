states = [
    {'name':'West Bengal', 'capital':'Kolkata', 'population':91276115},
    {'name':'Rajasthan', 'capital':'Jaipur', 'population':68548437},
    {'name':'Assam', 'capital':'Dispur', 'population':31205576},
    {'name':'Sikkim', 'capital':'Gangtok', 'population':610577}
]

print("INDIAN STATE INFORMATION SYSTEM")
print("--------------------------------")

# Displaying all the state names
for state in states:
    print('State:', state['name'])

# Search for a state
for state in states:
    if state['name'] == 'Assam':
        print('\nCapital of Assam:', state['capital'])

# Analyzing the highest and lowest population states
highest_population = states[0]['population']
highest_population_state = states[0]['name']

lowest_population = states[0]['population']
lowest_population_state = states[0]['name']

for state in states:
    if state['population'] > highest_population:
        highest_population = state['population']
        highest_population_state = state['name']

    if state['population'] < lowest_population:
        lowest_population = state['population']
        lowest_population_state = state['name']

print('\nHighest Population State:')
print(highest_population_state, '-', highest_population)

print('\nLowest Population State:')
print(lowest_population_state, '-', lowest_population)

# Calculating total population
total_population = 0

for state in states:
    total_population += state['population']

print('\nTotal Population:', total_population)

# Calculating average population
average_population = total_population / len(states)

print('Average Population:', round(average_population, 2))