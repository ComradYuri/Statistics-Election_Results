import numpy as np
from matplotlib import pyplot as plt

survey_responses = [
    'Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
    'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan',
    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos',
    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos'
    ]
# total votes for Ceballos in sample
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

percentage_ceballos = round(100 * total_ceballos/len(survey_responses), 2)
print(percentage_ceballos)

# the '.' at the end ensures that you are dividing each element in a by a float. If you do not include the period,
# Python will assume you want integer division (an integer divided by an integer). Naturally, integer division returns
# an integer. For quotients less than 1 (for example, 7 divided by 18), this is problematic. Python will return a 0 (as
# opposed to a decimal, like 0.388), which can result in erroneous calculations.
possible_surveys = np.random.binomial(33, 0.54, size=10000)/33.
# print 10000 the chance Ceballos won. 33 is sample size. 0.54 is population vote for Ceballos. 10000 is population size
print(possible_surveys)

plt.hist(possible_surveys, range=(0, 1), bins=20)

plt.show()

plt.close()

# maximum possible surveys is a town of 10000 inhabitants
possible_surveys_length = float(len(possible_surveys))
print(possible_surveys_length)
# incorrect election result of all surveys
incorrect_surveys_length = len(possible_surveys[possible_surveys < .5])
print(incorrect_surveys_length)
# percentage change that a survey is wrong
percentage_incorrect = incorrect_surveys_length/possible_surveys_length
print(percentage_incorrect)


# same scenario repeated but with a sample size of 7000.
# in this case there is a zero percent change that the wrong winner is predicted
large_survey = np.random.binomial(7000, 0.54, size=10000)/7000.
incorrect_large_survey_length = len(large_survey[large_survey < 0.5])

percentage_large_incorrect = incorrect_large_survey_length/7000
print(percentage_large_incorrect)
