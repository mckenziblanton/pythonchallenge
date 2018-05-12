import os 
import csv

#current location > raw_data > file you need 
csvpath = os.path.join('.',"raw_data", "election_data_1.csv")

votes = 0 
candidates = []
dict_candidate = {}
vote_count = []

print("Election Results")
print('--------------------')

# read csv file 
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    for row in csvreader: 
        if row[2] != "Candidate":
            votes = votes + 1 
            candidates.append(row[2])
    print("Total votes: " + str(votes))
    print('--------------------')
    set_candidate = set(candidates)
    list_candidate = list(set(candidates))
 
     
    for i in range(len(list_candidate)):
        dict_candidate.update({list_candidate[i]:candidates.count(list_candidate[i])})
        percent_vote = (candidates.count(list_candidate[i])/(votes)*100)
        vote_count.append(percent_vote)
    #print(dict_candidate)
    
    for i in list_candidate:
        print(i+ " : " +  str(candidates.count(i)/votes*100) + "%" + " (" + str(candidates.count(i)) + ")")
    print('--------------------')

    for candidate in list_candidate: 
        if (dict_candidate[candidate]/votes*100) == max(vote_count):
            print("winner: " + str(candidate))
            print('--------------------')






    