from scipy.stats import pearsonr, spearmanr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filenames = ["(8) Politische Bildung.csv", "(9) Politische Bildung.csv",
             "(10) Politische Bildung.csv", "(11) Politische Bildung.csv"]

grades = [8, 9, 10, 11]


#txt_file = open("results.txt", "a")

filename1 = "surveys.csv"

filename2 = "(11) Politische Bildung.csv"

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

# response_list = []
# for i, j in surveys_df.iterrows():
#     #print("\nparticipant", i+1, ":")
#     individual_responses = []
#     for n in range(24):
#         # print(j[2+n])
#         # skips first 2/5 (irrelevant) columns
#         individual_responses.append(j[n+5])
#     # print(individual_responses)
#     response_list.append(individual_responses)


def GetResponses(f, c):

    df = pd.read_csv(c)

    if c == "(11) Politische Bildung.csv":

        for c in f:

            response_list = []
            for i, j in df.iterrows():
                #print("\nparticipant", i+1, ":")
                individual_responses = []
                for n in range(24):
                    # print(j[2+n])
                    # skips first 2/5 (irrelevant) columns
                    individual_responses.append(j[n+5])
                # print(individual_responses)
                response_list.append(individual_responses)

    if c != "(11) Politische Bildung.csv":

        for c in f:

            response_list = []
            for i, j in df.iterrows():
                #print("\nparticipant", i+1, ":")
                individual_responses = []
                for n in range(24):
                    # print(j[2+n])
                    # skips first 2/5 (irrelevant) columns
                    individual_responses.append(j[n+2])
                # print(individual_responses)
                response_list.append(individual_responses)

    # print(response_list)
    return(response_list)


def GetInterest(f, c):

    response_list = GetResponses(f, c)

    sums_int = []

    for i in response_list:
        ind_int = []
        # print("p")
        for n in range(8):
            # print(i[n])
            ind_int.append(i[n])

        t = 0
        for e in ind_int:
            t += int(e)
        sums_int.append(t)

    return(sums_int)
    # print(sums_int)

#GetInterest(filenames, "(11) Politische Bildung.csv")


# GetResponses(filenames, "(11) Politische Bildung.csv")

# print(surveys_df.shape[0])
# print(surveys_df.shape[1])

#print("\nTotal: ", response_list)

# print(response_list[0:len(response_list)])

# print((response_list[22][1]))
# print((response_list[22][22]))
# print(surveys_df.iloc[22,25])
# print(surveys_df.shape[1])
# for i in range(5):
#     print(i+2)


# for i in response_list:
#     for j in len():
#         print(i[j])

# n = 1
# for i in response_list:
#     print("\nParticipant", n,":")
#     n += 1
#     for j in range(23):
#         print(i[j])
participants_resp_edu = []
scores = []

# n = 0
# for i in response_list:
#     #print("\nParticipant", str(n+1),":")

#     # with open("ergebnisse.txt", "w") as f:
#     #     f.write("\nParticipant " + str(n+1) + ":")

#     individual_response = []

#     # Q1
#     if "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (response_list[n][8]):
#         individual_response.append(1)
#     if not "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (response_list[n][8]):
#         individual_response.append(-1)

#     # Q2
#     if "Der Bundespräsident" in (response_list[n][9]):
#         individual_response.append(2)
#     if not "Der Bundespräsident" in (response_list[n][9]):
#         individual_response.append(-1)

#     # Q3
#     if "4 Jahre" in (response_list[n][10]):
#         individual_response.append(1)

#     if not "4 Jahre" in (response_list[n][10]):
#         individual_response.append(1)

#     # Q4
#     if "Bundespräsident" in (response_list[n][11]):
#         individual_response.append(1)
#     if "Bundesverfassungsgericht" in (response_list[n][11]):
#         individual_response.append(1)
#     if "Bundeskanzler" in (response_list[n][11]):
#         individual_response.append(1)
#     if "Bundesversammlung" in (response_list[n][11]):
#         individual_response.append(1)
#     if "Bundestag" in (response_list[n][11]):
#         individual_response.append(1)

#     if "Bundesregierung" in (response_list[n][11]):
#         individual_response.append(-1)
#     if "Bundesrat" in (response_list[n][11]):
#         individual_response.append(-1)

#     # Q5
#     if(response_list[n][12]) == "Sie ernennen die Kabinettsmitglieder des Bundsrates":
#         individual_response.append(3)
#     if(response_list[n][12]) != "Sie ernennen die Kabinettsmitglieder des Bundsrates":
#         individual_response.append(-1)
#     # Q6
#     if(response_list[n][13]) == "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
#         individual_response.append(5)
#     if(response_list[n][13]) != "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
#         individual_response.append(-1)
#     # Q7
#     if(response_list[n][14]) == "Angela Merkel":
#         individual_response.append(1)
#     if(response_list[n][14]) != "Angela Merkel":
#         individual_response.append(-1)
#     # Q8
#     if(response_list[n][15]) == "Die Bundesversammlung":
#         individual_response.append(2)
#     if(response_list[n][15]) != "Die Bundesversammlung":
#         individual_response.append(-1)
#     # Q9
#     if(response_list[n][16]) == "Der Bundestag":
#         individual_response.append(2)
#     if(response_list[n][16]) != "Der Bundestag":
#         individual_response.append(-1)
#     # Q10
#     if(response_list[n][17]) == "Frank-Walter Steinmeier":
#         individual_response.append(1)
#     if(response_list[n][17]) != "Frank-Walter Steinmeier":
#         individual_response.append(-1)

#     # Q11
#     if "Ernennt/ Entlässt Richter des Bundesverfassungsgerichts" in (response_list[n][18]):
#         individual_response.append(1)
#     if "Ernennt den Bundeskanzler" in (response_list[n][18]):
#         individual_response.append(1)
#     if "Fertigt Gesetze aus" in (response_list[n][18]):
#         individual_response.append(1)
#     if "Löst den Bundestag auf" in (response_list[n][18]):
#         individual_response.append(1)

#     if "Vorschlagen der Bundesminister" in (response_list[n][18]):
#         individual_response.append(-1)

#     # #Q12
#     if "Höchstes Gericht in Deutschland" in (response_list[n][19]):
#         individual_response.append(1)
#     if "Prüft Gesetze auf potentielle Verfassungswidrigkeit" in (response_list[n][19]):
#         individual_response.append(1)
#     if "Maßstab bei der Rechtssprechung ist das Grundgesetz" in (response_list[n][19]):
#         individual_response.append(1)

#     # Q13
#     if "Gegenzeichnung von Gesetzen" in (response_list[n][20]):
#         individual_response.append(1)
#     if "Vorsitz der Bundesregierung" in (response_list[n][20]):
#         individual_response.append(1)

#     if "Vorsitz des Bundestages" in (response_list[n][20]):
#         individual_response.append(-1)
#     if "Ernennen der Bundesminister" in (response_list[n][20]):
#         individual_response.append(-1)

#     # Q14
#     if "Gesetzesinitative" in (response_list[n][21]):
#         individual_response.append(1)
#     if "Entscheidung über Bundeshaushalt" in (response_list[n][21]):
#         individual_response.append(1)
#     if "Kontrolle der Regierung" in (response_list[n][20]):
#         individual_response.append(1)
#     if "Wahl des Bundeskanzlers" in (response_list[n][20]):
#         individual_response.append(1)

#     if "Wahl des Bundespräsidenten" in (response_list[n][21]):
#         individual_response.append(-1)

#     # Q15
#     if "Gesetzesinitiative" in (response_list[n][22]):
#         individual_response.append(1)
#     if "Mitwirken in auswärtigen Angelegenheiten" in (response_list[n][22]):
#         individual_response.append(1)

#     if "Abwahl des Bundeskanzlers" in (response_list[n][22]):
#         individual_response.append(-1)

#     # Q16
#     if(response_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
#         individual_response.append(8)
#     if not (response_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
#         individual_response.append(-1)

#     n += 1
#     participants_resp_edu.append(individual_response)

#     ind_score = 0
#     for z in individual_response:
#         ind_score += z

#     scores.append(ind_score)

# print(individual_response)
#print("sum=", ind_score)

# with open("ergebnisse.txt", "w") as f:

#     ind_text = ""
#     for i in individual_response:
#         ind_text = ind_text + ", " + str(i)
#       f.write("\n" + ind_text)
#     print(ind_text)

#     # f.write("sum="+ str(ind_score))
#     print("sum="+ str(ind_score))

#print("\n", scores)


def GetGroupScores(f, c):

    response_list = GetResponses(f, c)

    participants_resp_edu = []
    scores = []

    n = 0
    for i in response_list:

        individual_response = []

        # Q1
        if "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (response_list[n][8]):
            individual_response.append(1)
        if not "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft" in (response_list[n][8]):
            individual_response.append(-1)

        # Q2
        if "Der Bundespräsident" in (response_list[n][9]):
            individual_response.append(2)
        if not "Der Bundespräsident" in (response_list[n][9]):
            individual_response.append(-1)

        # Q3
        if "4 Jahre" in (response_list[n][10]):
            individual_response.append(1)

        if not "4 Jahre" in (response_list[n][10]):
            individual_response.append(1)

        # Q4
        if "Bundespräsident" in (response_list[n][11]):
            individual_response.append(1)
        if "Bundesverfassungsgericht" in (response_list[n][11]):
            individual_response.append(1)
        if "Bundeskanzler" in (response_list[n][11]):
            individual_response.append(1)
        if "Bundesversammlung" in (response_list[n][11]):
            individual_response.append(1)
        if "Bundestag" in (response_list[n][11]):
            individual_response.append(1)

        if "Bundesregierung" in (response_list[n][11]):
            individual_response.append(-1)
        if "Bundesrat" in (response_list[n][11]):
            individual_response.append(-1)

        # Q5
        if(response_list[n][12]) == "Sie ernennen die Kabinettsmitglieder des Bundsrates":
            individual_response.append(3)
        if(response_list[n][12]) != "Sie ernennen die Kabinettsmitglieder des Bundsrates":
            individual_response.append(-1)
        # Q6
        if(response_list[n][13]) == "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
            individual_response.append(5)
        if(response_list[n][13]) != "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
            individual_response.append(-1)
        # Q7
        if(response_list[n][14]) == "Angela Merkel":
            individual_response.append(1)
        if(response_list[n][14]) != "Angela Merkel":
            individual_response.append(-1)
        # Q8
        if(response_list[n][15]) == "Die Bundesversammlung":
            individual_response.append(2)
        if(response_list[n][15]) != "Die Bundesversammlung":
            individual_response.append(-1)
        # Q9
        if(response_list[n][16]) == "Der Bundestag":
            individual_response.append(2)
        if(response_list[n][16]) != "Der Bundestag":
            individual_response.append(-1)
        # Q10
        if(response_list[n][17]) == "Frank-Walter Steinmeier":
            individual_response.append(1)
        if(response_list[n][17]) != "Frank-Walter Steinmeier":
            individual_response.append(-1)

        # Q11
        if "Ernennt/ Entlässt Richter des Bundesverfassungsgerichts" in (response_list[n][18]):
            individual_response.append(1)
        if "Ernennt den Bundeskanzler" in (response_list[n][18]):
            individual_response.append(1)
        if "Fertigt Gesetze aus" in (response_list[n][18]):
            individual_response.append(1)
        if "Löst den Bundestag auf" in (response_list[n][18]):
            individual_response.append(1)

        if "Vorschlagen der Bundesminister" in (response_list[n][18]):
            individual_response.append(-1)

        # #Q12
        if "Höchstes Gericht in Deutschland" in (response_list[n][19]):
            individual_response.append(1)
        if "Prüft Gesetze auf potentielle Verfassungswidrigkeit" in (response_list[n][19]):
            individual_response.append(1)
        if "Maßstab bei der Rechtssprechung ist das Grundgesetz" in (response_list[n][19]):
            individual_response.append(1)

        # Q13
        if "Gegenzeichnung von Gesetzen" in (response_list[n][20]):
            individual_response.append(1)
        if "Vorsitz der Bundesregierung" in (response_list[n][20]):
            individual_response.append(1)

        if "Vorsitz des Bundestages" in (response_list[n][20]):
            individual_response.append(-1)
        if "Ernennen der Bundesminister" in (response_list[n][20]):
            individual_response.append(-1)

        # Q14
        if "Gesetzesinitative" in (response_list[n][21]):
            individual_response.append(1)
        if "Entscheidung über Bundeshaushalt" in (response_list[n][21]):
            individual_response.append(1)
        if "Kontrolle der Regierung" in (response_list[n][20]):
            individual_response.append(1)
        if "Wahl des Bundeskanzlers" in (response_list[n][20]):
            individual_response.append(1)

        if "Wahl des Bundespräsidenten" in (response_list[n][21]):
            individual_response.append(-1)

        # Q15
        if "Gesetzesinitiative" in (response_list[n][22]):
            individual_response.append(1)
        if "Mitwirken in auswärtigen Angelegenheiten" in (response_list[n][22]):
            individual_response.append(1)

        if "Abwahl des Bundeskanzlers" in (response_list[n][22]):
            individual_response.append(-1)

        # Q16
        if(response_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
            individual_response.append(2)
        if not (response_list[n][23]) == "Kanzler,- Kollegial,- Ressortprinzip":
            individual_response.append(-1)

        n += 1
        participants_resp_edu.append(individual_response)

        ind_score = 0
        for z in individual_response:
            ind_score += z

        scores.append(ind_score)
    return(scores)


fig = plt.figure()
plt.boxplot(scores)

plt.ylim([-20, 55])
plt.yticks(range(-20, 55, 5))  # Y ticks every 50.  You can provide any list.
plt.plot([0.5, 1.5], [15, 15], 'k-', lw=1)


fig.suptitle('Klassenstufe 8', fontsize=14)

# plt.show()


# calculate the Pearson's correlation between two variables


# calculate Pearson's correlation


# corr, _ = pearsonr(GetInterest(filenames, "(8) Politische Bildung.csv"),
#                    GetGroupScores(filenames, "(8) Politische Bildung.csv"))
# print('Pearsons correlation: %.3f' % corr)

# corr, _ = pearsonr(GetInterest(filenames, "(9) Politische Bildung.csv"),
#                    GetGroupScores(filenames, "(9) Politische Bildung.csv"))
# print('Pearsons correlation: %.3f' % corr)

# corr, _ = pearsonr(GetInterest(filenames, "(10) Politische Bildung.csv"),
#                    GetGroupScores(filenames, "(10) Politische Bildung.csv"))
# print('Pearsons correlation: %.3f' % corr)


# corr, _ = pearsonr(GetInterest(filenames, "(11) Politische Bildung.csv"),
#                    GetGroupScores(filenames, "(11) Politische Bildung.csv"))
# print('Pearsons correlation: %.3f' % corr)


# corr, _ = spearmanr(GetInterest(filenames, "(8) Politische Bildung.csv"),
#                     GetGroupScores(filenames, "(8) Politische Bildung.csv"))
# print('Spearmans correlation: %.3f' % corr)

# corr, _ = spearmanr(GetInterest(filenames, "(9) Politische Bildung.csv"),
#                     GetGroupScores(filenames, "(9) Politische Bildung.csv"))
# print('Spearmans correlation: %.3f' % corr)

# corr, _ = spearmanr(GetInterest(filenames, "(10) Politische Bildung.csv"),
#                     GetGroupScores(filenames, "(10) Politische Bildung.csv"))
# print('Spearmans correlation: %.3f' % corr)

corr, _ = spearmanr(GetInterest(filenames, "(11) Politische Bildung.csv"),
                    GetGroupScores(filenames, "(11) Politische Bildung.csv"))
print('Spearmans correlation: %.3f' % corr)


# print(len(scores))
# print(len(GetResponses(filenames, "(11) Politische Bildung.csv")))

# print(GetResponses(filenames, "(9) Politische Bildung.csv"))

# print(GetGroupScores(filenames, "(11) Politische Bildung.csv"))
