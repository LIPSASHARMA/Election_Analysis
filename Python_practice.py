#print("Hello World")

#num_candidates = 3
#winning_percentage = 73.81
#candidate = "Diane"
#won_election = True

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")


#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")


#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")


#x = 0
#while x <= 5:
#    print(x)
#    x = x + 1


#for county in counties:
 #   print(county)


#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)

#for num in range(5):
#    print(num)


#for i in range(len(counties)):
#    print(counties[i])


#counties_tuples = ("Arapahoe","Denver","Jefferson")

#for county in counties_tuples:
#      print(county)

#for county in counties_tuples:
#      print(counties)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.keys():
# print(county)
#print("-----------------------------------------")

# for voters in counties_dict.values():
#     print(voters)
# print("-----------------------------------------")

# for county in counties_dict:
#     print(counties_dict[county])
# print("-----------------------------------------")

# for county in counties_dict:
#     print(counties_dict.get(county))
# print("-----------------------------------------")

# for county, voters in counties_dict.items():
#     print(county, voters)
# print("-----------------------------------------")


#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
   #            {"county":"Denver", "registered_voters": 463353},
   #            {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
 #print(county_dict)
#print("-----------------------------------------")

#for i in range(len(voting_data)):
#      print(voting_data[i]['county'])
#print("-----------------------------------------")


#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
#print("-----------------------------------------")


#for county_dict in voting_data:
#    print(county_dict['county'])
#print("-----------------------------------------")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#print("-------------------------------------------------------------------")

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
 #print("--------------------------------------------------------------------")


#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")
#print("--------------------------------------------------------------------")


#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)
#print("--------------------------------------------------------------------")

#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)    
#print("--------------------------------------------------------------------")


# Import the datetime class from the datetime module.
#  import datetime
# Use the now() attribute on the datetime class to get the present time.
#  now = datetime.datetime.now()
# Print the present time.
#  print("The time right now is ", now)


# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for counties in voting_data:
        #print(f"{counties} county has {votes} registered voters.")
        #print(counties['county'])
        print(counties['registered_voters'])
        #print(f"{counties['county']} county has {counties['registered_voters']} registerd voters.")
