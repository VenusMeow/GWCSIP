import json

results = []
previous = []

finished = False
while(finished==False):
    answers = {}

    name = input("What is your name? ")
    answers['name'] = name;
    age = input("What is your age? ")
    answers['age'] = age;
    color = input("What is your favorite color? ")
    answers['color'] = color;
    plang = input("What is your favorite programming language? ")
    answers['plang'] = plang;
    results.append(answers)
    done = input("Are we done? ")
    if (done=="yes" or done=="Yes"):
        finished = True

with open('results.json') as datafile:
    previous = json.load(datafile)

results = previous + results;

with open('results.json','w') as outfile:
    json.dump(results,outfile)
