#Exercitiul 3
#Create a script that reads the access log from a file. The name of the file is provided as an argument.
#An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them.

import sys
from collections import Counter

def process_log(infile):
    infile = r"/Users/miancu/PycharmProjects/my-python-project/pythonProject/access.log.5"
    with open(infile, 'r') as f:
        user_agents = [line.split('"')[5] for line in f if '"GET' in line or '"POST' in line]

    real_user_agents = len(set(user_agents))
    print(f"Number of different user agents: {real_user_agents}")
    user_agent_req_count = Counter(user_agents)
    for agent, count in user_agent_req_count.items():
        print(f"{agent}: {count} requests ")

acces_log_file = sys.argv[0]
process_log(acces_log_file)
