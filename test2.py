import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


grades = [8, 9, 10, 11]



#txt_file = open("results.txt", "a")

filename1 = "surveys.csv"

filename2 = "(8) Politische Bildung.csv"

#print(pd.read_csv(filename1))

surveys_df = pd.read_csv(filename2)

# for i in surveys_df.columns:
#     (print(surveys_df[i].describe()))


# for i in grades:
#     txt_file = open("results.txt", "a")
#     txt_file.write("\nStufe"+str(i)+":")
#     survey_df = pd.read_csv("("+str(i)+") "+"Politische Bildung.csv")
#     txt_file.write(str(survey_df.describe()))
#     txt_file.close()

#print(surveys_df.columns)

columns = []
for i in surveys_df.columns:
   columns.append(i) 
   
print(columns)
   
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

# interest_list = []
# for i, j in surveys_df.iterrows():
#     print("participant", i+1, ":")
#     individual_responses =  []
#     for n in range(8):
#         #print(j[2+n])
#         individual_responses.append(j[2+n])
#     print(individual_responses)
#     interest_list.append(individual_responses)

# print("\nTotal: ", interest_list)

participants_resp_edu = []

for i in range (len(surveys_df)-2):
   individual_response =  []
   
   print("Participant", i, ":")
   
   #Q1
   if(surveys_df.iloc[i+2,10]) == "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft":
      individual_response.append(1)
   #Q2
   if(surveys_df.iloc[i+2,11]) == "Der Bundespräsident":
      individual_response.append(2)
   #Q3
   if(surveys_df.iloc[i+2,12]) == "4 Jahre":
      individual_response.append(1)
   #Q4      

   if(surveys_df.iloc[i+2,13]) == "Bundespräsident":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,13]) == "Bundesverfassungsgericht":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,13]) == "Bundeskanzler":
      individual_response.append(1)  
   if(surveys_df.iloc[i+2,13]) == "Bundesversammlung":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,13]) == "Bundestag":
      individual_response.append(1)      
      
   #Q5           
   if(surveys_df.iloc[i+2,14]) == "Sie ernennen die Kabinettsmitglieder des Bundsrates":
      individual_response.append(3)
   #Q6   
   if(surveys_df.iloc[i+2,15]) == "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
      individual_response.append(5)
   #Q7      
   if(surveys_df.iloc[i+2,16]) == "Angela Merkel":
      individual_response.append(1)
   #Q8      
   if(surveys_df.iloc[i+2,17]) == "Die Bundesversammlung":
      individual_response.append(2)   
   #Q9   
   if(surveys_df.iloc[i+2,18]) == "Der Bundestag":
      individual_response.append(2)   
   #Q10
   if(surveys_df.iloc[i+2,19]) == "Frank-Walter Steinmeier":
      individual_response.append(1)
      
   #Q11
   if(surveys_df.iloc[i+2,20]) == "Ernennt/ Entlässt Richter des Bundesverfassungsgerichts":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,20]) == "Ernennt den Bundeskanzler":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,20]) == "Fertigt Gesetze aus":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,20]) == "Löst den Bundestag auf":
      individual_response.append(1)      
      
   #Q12
   if(surveys_df.iloc[i+2,21]) == "Höchstes Gericht in Deutschland":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,21]) == "Prüft Gesetze auf potentielle Verfassungswidrigkeit":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,21]) == "Maßstab bei der Rechtssprechung ist das Grundgesetz":
      individual_response.append(1)      
      
   #Q13
   if(surveys_df.iloc[i+2,22]) == "Gegenzeichnung von Gesetzen":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,22]) == "Vorsitz der Bundesregierung":
      individual_response.append(1)
   
   #Q14
   if(surveys_df.iloc[i+2,23]) == "Gesetzesinitative":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,23]) == "Entscheidung über Bundeshaushalt":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,23]) == "Kontrolle der Regierung":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,23]) == "Wahl des Bundeskanzlers":
      individual_response.append(1)
   
   #Q15      
   if(surveys_df.iloc[i+2,24]) == "Gesetzesinitiative":
      individual_response.append(1)
   if(surveys_df.iloc[i+2,24]) == "Mitwirken in auswärtigen Angelegenheiten":
      individual_response.append(1)    
   
   #Q16
   if(surveys_df.iloc[i+2,25]) == "Kanzler,- Kollegial,- Ressortprinzip":
      individual_response.append(8)       
      
      
      
   # #Q1
   # if(surveys_df.iloc[i+2,10]) != "Jeder volljährige Bürger mit einer deutschen Staatsbürgerschaft":
   #    individual_response.append(0)
   # #Q2
   # if(surveys_df.iloc[i+2,11]) != "Der Bundespräsident":
   #    individual_response.append(0)
   # #Q3
   # if(surveys_df.iloc[i+2,12]) != "4 Jahre":
   #    individual_response.append(0)
   # #Q4      

   # if(surveys_df.iloc[i+2,13]) == "Bundesregierung":
   #    individual_response.append(0)    
   # if(surveys_df.iloc[i+2,13]) == "Bundesrat":
   #    individual_response.append(0) 
            
   # #Q5           
   # if(surveys_df.iloc[i+2,14]) != "Sie ernennen die Kabinettsmitglieder des Bundsrates":
   #    individual_response.append(0)
   # #Q6   
   # if(surveys_df.iloc[i+2,15]) != "Zur Hälfte vom Bundesrat und zur anderen Hälfte vom Bundestag, jeweils mit 2/3 Mehrheit, auf 12 Jahre":
   #    individual_response.append(0)
   # #Q7      
   # if(surveys_df.iloc[i+2,16]) != "Angela Merkel":
   #    individual_response.append(0)
   # #Q8      
   # if(surveys_df.iloc[i+2,17]) != "Die Bundesversammlung":
   #    individual_response.append(0)   
   # #Q9   
   # if(surveys_df.iloc[i+2,18]) != "Der Bundestag":
   #    individual_response.append(0)   
   # #Q10
   # if(surveys_df.iloc[i+2,19]) != "Frank-Walter Steinmeier":
   #    individual_response.append(0)
      
   # #Q11
   # if(surveys_df.iloc[i+2,20]) != "Vorschlagen der Bundesminister":
   #    individual_response.append(0)
      
   # #Q12    
   # if(surveys_df.iloc[i+2,21]) == "Höchstes Gericht in Deutschland":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,21]) == "Prüft Gesetze auf potentielle Verfassungswidrigkeit":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,21]) == "Maßstab bei der Rechtssprechung ist das Grundgesetz":
   #    individual_response.append(1)
    
   # #Q13
   # if(surveys_df.iloc[i+2,22]) == "Vorsitz des Bundestages":
   #    individual_response.append(0)
   # if(surveys_df.iloc[i+2,22]) == "Ernennen der Bundesminister":
   #    individual_response.append(0)
   
   # #Q14
   # if(surveys_df.iloc[i+2,23]) == "Gesetzesinitative":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,23]) == "Entscheidung über Bundeshaushalt":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,23]) == "Kontrolle der Regierung":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,23]) == "Wahl des Bundeskanzlers":
   #    individual_response.append(1)
   
   # #Q15      
   # if(surveys_df.iloc[i+2,24]) == "Gesetzesinitiative":
   #    individual_response.append(1)
   # if(surveys_df.iloc[i+2,24]) == "Mitwirken in auswärtigen Angelegenheiten":
   #    individual_response.append(1)    
   
   # #Q16
   # if(surveys_df.iloc[i+2,25]) == "Kanzler,- Kollegial,- Ressortprinzip":
   #    individual_response.append(8)       
      
      
   participants_resp_edu.append(individual_response)
   print(individual_response)