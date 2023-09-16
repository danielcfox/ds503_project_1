from faker import Faker
import csv
import random
import string
from my_faker import Hobby, Friendship, Access
import numpy as np
import time

# Initialize faker classes to generate random values.
fake = Faker()
hobby = Hobby()
friendship = Friendship()
access = Access()


## Define constants/ number of rows (please scale down for testing and scale up for the actual requirements)
facein_num_rows = 200001 // 1000
associate_num_rows = 20000001 // 1000
access_num_rows = 10000001 // 1000


# Generate FaceInPage dataset
# -------------------------------------------------------------------------------------------------
facein_ids = []

start_time = time.time()

with open('FaceInPage.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(["ID", "Name", "Nationality", "CountryCod", "Hobby"])  # add if want the column names to appear in the final csv file.
    for i in range(1, facein_num_rows):
        facein_ids.append(i)
        writer.writerow([i, fake.name(), fake.country(), random.randint(1, 50), hobby.get_rand()])

print(f"Datasets FaceInPage.csv generated successfully after {time.time() - start_time} seconds!")

# Generate Associates dataset
# -------------------------------------------------------------------------------------------------

start_time = time.time()
facein_ids = np.array(facein_ids)
with open('Associates.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    friend_relations = set() # to keep track of equivalent symmetrical relationships

    # writer.writerow(["FriendRel", "PersonA_ID", "PersonB_ID", "DateofFriendship", "Desc"])  # add if want the column names to appear in the final csv file.
    for i in range(1, associate_num_rows):
        person_a_id = np.random.choice(facein_ids)
        available_ids = facein_ids[facein_ids != person_a_id]
        person_b_id = np.random.choice(available_ids)
        if (person_a_id, person_b_id) not in friend_relations and (person_b_id, person_a_id) not in friend_relations:
            friend_relations.add((person_a_id, person_b_id))
            friend_relations.add((person_b_id, person_a_id)) # adding this due to the symmetrical relationship between a and b
            writer.writerow([i, person_a_id, person_b_id, random.randint(1, 1000000), friendship.get_rand()]) 

print(f"Datasets Associates.csv generated successfully after {time.time() - start_time} seconds!")

# Generate AccessLogs dataset
# -------------------------------------------------------------------------------------------------

start_time = time.time()

with open('AccessLogs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(["AccessId", "ByWho", "WhatPage", "TypeOfAccess", "AccessTime"])  # add if want the column names to appear in the final csv file.
    
    for i in range(1, access_num_rows):
        bywho = np.random.choice(facein_ids)

        # since we don't have a self-visiting case, the WhatPage entries are randomly pulled from a pool without the bywho ID
        available_ids = facein_ids[facein_ids != bywho]
        whatpage = np.random.choice(available_ids)

        writer.writerow([i, bywho, whatpage, access.get_rand(), random.randint(1, 1000000)])

print(f"Datasets AccessLogs.csv generated successfully after {time.time() - start_time} seconds!")