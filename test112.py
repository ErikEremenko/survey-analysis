import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


grades = [8, 9, 10, 11]


#txt_file = open("results.txt", "a")

filename1 = "surveys.csv"

filename2 = "(10) Politische Bildung.csv"

surveys_df = pd.read_csv(filename2)


# for i in grades:
#     txt_file = open("results.txt", "a")
#     txt_file.write("\nStufe"+str(i)+":")
#     survey_df = pd.read_csv("("+str(i)+") "+"Politische Bildung.csv")
#     txt_file.write(str(survey_df.describe()))
#     txt_file.close()

# print(surveys_df.columns)

columns = []
for i in surveys_df.columns:
    columns.append(i)

# print(columns)

# print(columns)

# surveys_df.boxplot(column = [
#     # "time",
#     # "sex",
#     "I int pol",
#     "i think surrounding",
#     "i int elec",
#     "i int gov",
#     "i int news",
#     "th pol act + inf",
#     "th let pol",
#     "elec tom",
# ])
# #surveys_df.plot()
# plt.show()

# for i in grades:
#     print("\nStufe"+str(i)+":")
#     survey_df = pd.read_csv("("+str(i)+") "+"Politische Bildung.csv")
#     survey_df.boxplot(column = [
#         # "time",
#         # "sex",
#         "I int pol",
#         "i think surrounding",
#         "i int elec",
#         "i int gov",
#         "i int news",
#         "th pol act + inf",
#         "th let pol",
#         "elec tom",
#     ])
#     #surveys_df.plot()
#     plt.show()

interest_list = []
for i, j in surveys_df.iterrows():
    print("\nparticipant", i+1, ":")
    individual_responses = []
    for n in range(24):
        # print(j[2+n])
        # skips first 2/5 (irrelevant) columns
        individual_responses.append(j[n+2])
    print(individual_responses)
    interest_list.append(individual_responses)

# print(surveys_df.shape[0])
# print(surveys_df.shape[1])

#print("\nTotal: ", interest_list)

# print(interest_list[0:len(interest_list)])

# print((interest_list[22][1]))
# print((interest_list[22][22]))
# print(surveys_df.iloc[22,25])
# print(surveys_df.shape[1])
# for i in range(5):
#     print(i+2)


# for i in interest_list:
#     for j in len():
#         print(i[j])

# n = 1
# for i in interest_list:
#     print("\nParticipant", n,":")
#     n += 1

#     for j in range(23):
#         print(i[j])

participants_resp_edu = []
scores = []

n = 0
for i in interest_list:
    print("\nParticipant", str(n+1), ":")

    # with open("ergebnisse.txt", "w") as f:
    #     f.write("\nParticipant " + str(n+1) + ":")

    individual_response = []

    # Q1
    if "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (interest_list[n][8]):
        individual_response.append(1)
    if not "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (interest_list[n][8]):
        individual_response.append(-1)

    # Q2
    if "Der Bundespräsident" in (interest_list[n][9]):
        individual_response.append(2)
    if not "Der Bundespräsident" in (interest_list[n][9]):
        individual_response.append(-1)

    # Q3
    if "4 Jahre" in (interest_list[n][10]):
        individual_response.append(1)

    if not "4 Jahre" in (interest_list[n][10]):
        individual_response.append(1)

    # Q4
    if "Bundespräsident" in (interest_list[n][11]):
        individual_response.append(1)
    if "Bundesverfassungsgericht" in (interest_list[n][11]):
        individual_response.append(1)
    if "Bundeskanzler" in (interest_list[n][11]):
        individual_response.append(1)
    if "Bundesversammlung" in (interest_list[n][11]):
        individual_response.append(1)
    if "Bundestag" in (interest_list[n][11]):
        individual_response.append(1)

    if "Bundesregierung" in (interest_list[n][11]):
        individual_response.append(-1)
    if "Bundesrat" in (interest_list[n][11]):
        individual_response.append(-1)

    # Q5
    if(interest_list[n][12]) == "Sie ernennen die Kabinettsmitglieder des Bundsrates":
        individual_response.append(3)
    if(interest_list[n][12]) != "Sie ernennen die Kabinettsmitglieder des Bundsrates":
        individual_response.append(-1)
    # Q6
    if(interest_list[n][13]) == "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
        individual_response.append(5)
    if(interest_list[n][13]) != "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
        individual_response.append(-1)
    # Q7
    if(interest_list[n][14]) == "Angela Merkel":
        individual_response.append(1)
    if(interest_list[n][14]) != "Angela Merkel":
        individual_response.append(-1)
    # Q8
    if(interest_list[n][15]) == "Die Bundesversammlung":
        individual_response.append(2)
    if(interest_list[n][15]) != "Die Bundesversammlung":
        individual_response.append(-1)
    # Q9
    if(interest_list[n][16]) == "Der Bundestag":
        individual_response.append(2)
    if(interest_list[n][16]) != "Der Bundestag":
        individual_response.append(-1)
    # Q10
    if(interest_list[n][17]) == "Frank-Walter Steinmeier":
        individual_response.append(1)
    if(interest_list[n][17]) != "Frank-Walter Steinmeier":
        individual_response.append(-1)

    # Q11
    if "Ernennt/ Entlässt Richter des Bundesverfassungsgerichts" in (interest_list[n][18]):
        individual_response.append(1)
    if "Ernennt den Bundeskanzler" in (interest_list[n][18]):
        individual_response.append(1)
    if "Fertigt Gesetze aus" in (interest_list[n][18]):
        individual_response.append(1)
    if "Löst den Bundestag auf" in (interest_list[n][18]):
        individual_response.append(1)

    if "Vorschlagen der Bundesminister" in (interest_list[n][18]):
        individual_response.append(-1)

    # #Q12
    if "Höchstes Gericht in Deutschland" in (interest_list[n][19]):
        individual_response.append(1)
    if "Prüft Gesetze auf potentielle Verfassungswidrigkeit" in (interest_list[n][19]):
        individual_response.append(1)
    if "Maßstab bei der Rechtssprechung ist das Grundgesetz" in (interest_list[n][19]):
        individual_response.append(1)

    # Q13
    if "Gegenzeichnung von Gesetzen" in (interest_list[n][20]):
        individual_response.append(1)
    if "Vorsitz der Bundesregierung" in (interest_list[n][20]):
        individual_response.append(1)

    if "Vorsitz des Bundestages" in (interest_list[n][20]):
        individual_response.append(-1)
    if "Ernennen der Bundesminister" in (interest_list[n][20]):
        individual_response.append(-1)

    # Q14
    if "Gesetzesinitative" in (interest_list[n][21]):
        individual_response.append(1)
    if "Entscheidung über Bundeshaushalt" in (interest_list[n][21]):
        individual_response.append(1)
    if "Kontrolle der Regierung" in (interest_list[n][20]):
        individual_response.append(1)
    if "Wahl des Bundeskanzlers" in (interest_list[n][20]):
        individual_response.append(1)

    if "Wahl des Bundespräsidenten" in (interest_list[n][21]):
        individual_response.append(-1)

    # Q15
    if "Gesetzesinitiative" in (interest_list[n][22]):
        individual_response.append(1)
    if "Mitwirken in auswärtigen Angelegenheiten" in (interest_list[n][22]):
        individual_response.append(1)

    if "Abwahl des Bundeskanzlers" in (interest_list[n][22]):
        individual_response.append(-1)

    # Q16
    if(interest_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
        individual_response.append(2)
    if not (interest_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
        individual_response.append(-1)

    n += 1
    participants_resp_edu.append(individual_response)

    ind_score = 0
    for z in individual_response:
        ind_score += z

    scores.append(ind_score)

    print(individual_response)
    print("sum=", ind_score)

    # with open("ergebnisse.txt", "w") as f:

    #     ind_text = ""
    #     for i in individual_response:
    #         ind_text = ind_text + ", " + str(i)
    #       f.write("\n" + ind_text)
    #     print(ind_text)

    #     # f.write("sum="+ str(ind_score))
    #     print("sum="+ str(ind_score))

print("\n", scores)

fig = plt.figure()
plt.boxplot(scores)

plt.ylim([-20, 55])
plt.yticks(range(-20, 55, 5))  # Y ticks every 50.  You can provide any list.
plt.plot([0.5, 1.5], [15, 15], 'k-', lw=1)


fig.suptitle('Klassenstufe 8', fontsize=14)

# plt.show()
