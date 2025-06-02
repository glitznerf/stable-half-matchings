from pulp import *
from math import ceil
import time
import numpy as np
from numpy import random



## SETUP

# Create an environment with your WLS license
params = {
  "REDACTED"
}
env = gp.Env(params=params)

# Create the model within the Gurobi environment
model = gp.Model(env=env)



## INSTANCE GENERATION

# Generate preferences uniformly at random for given number of agents n and a seed
def generate_instance(n, seed):
  random.seed(seed)
  agents = []
  for i in range(1, n+1):
    pref = []
    if i > 1:
      for j in range(1,i):
        pref.append(j)
    if i < n:
      for j in range(i+1, n+1):
        pref.append(j)
    pref = np.array(pref)
    random.shuffle(pref)
    agents.append([int(i) for i in pref])
  return agents

def get_index(agents):
    index = {}
    for ix, ranking in enumerate(agents):
        for entry_ix, entry in enumerate(ranking):
            index[(ix+1, entry_ix+1)] = entry
    return index



## ILP MODELS

def stable_model(agents, caps, index=None):
  pairs = []
  for i in range(len(agents)):
      for j in range(len(agents)):
            pairs.append((i+1, j+1))

  # To create a problem object by using pulp package,
  prob = LpProblem("Stable Half-Matching", LpMinimize)

  # Create dictionaries of decision variables.
  # full[i,j] = 1 if a_i,a_j are fully matched, 0 otherwise
  full = LpVariable.dicts("full", pairs, cat='Binary')

  # half[i,j] = 1 if a_i,a_j are half matched, 0 otherwise
  half = LpVariable.dicts("half", pairs, cat='Binary')

  # w[i,j] = 1 if a_i is filled up with agents at least as good as a_j, 0 otherwise
  w = LpVariable.dicts("w", pairs, cat='Binary')


  for ix, ranking in enumerate(agents):

    # Capacity constraints
    prob += lpSum([full[(ix+1, j)] + 0.5*half[(ix+1, j)] for j in ranking]) <= caps[ix]

    # Add w constraints
    better = []
    for entry in ranking:
      better.append(entry)
      prob += lpSum([full[(ix+1, j)] + 0.5*half[(ix+1, j)] for j in better]) >= caps[ix] * w[(ix+1, entry)]


  for i, j in pairs:

    # No overlap constraints
    prob += full[(i, j)] + half[(i, j)] <= 1

    # Symmetry constraints
    prob += full[(i, j)] == full[(j, i)]
    prob += half[(i, j)] == half[(j, i)]

    # Stability constraints
    if i != j:
      prob += full[(i, j)] + w[(i, j)] + w[(j, i)] >= 1
  
  # Trivial objective function minimising the number of self-matches of agent 1
  prob += full[(1, 1)]

  return prob, full, half, pairs


def egal_model(agents, caps, index):
  prob, full, half, pairs = stable_model(agents, caps)

  # Objective function: sum over ranks to account for costs
  prob += lpSum([[rank*(full[(agent, index[agent, rank])] + 0.5*half[(agent, index[agent, rank])]) for rank in range(1, len(agents))] for agent in range(1, len(agents) + 1)])

  return prob, full, half, pairs



### MAIN EXPERIMENT

def get_cycle_stats(pairs, half):
  half_partners = [list() for i in range(len(agents))]
  for pair in pairs:
    if half[pair].varValue >= 0.99:
      half_partners[pair[0]-1].append(pair[1])

  seen = []
  num_odd_cycles = 0
  num_odd_cycle_agents = 0
  for ix, partners in enumerate(half_partners):
    if ix+1 not in seen and len(partners) > 0:
      current = ix+1
      current_partners = partners
      cyclesize = 1

      while current_partners[0] not in seen or current_partners[1] not in seen:
        seen.append(current)
        cyclesize += 1
        if current_partners[0] not in seen:
            current = current_partners[0]
        else:
            current = current_partners[1]
        current_partners = half_partners[current-1]

      if cyclesize > 1 and cyclesize % 2:
        num_odd_cycles += 1
        num_odd_cycle_agents += cyclesize
  return num_odd_cycles, num_odd_cycle_agents


def get_cost(agents, full, half):
    cost = 0
    for agent in range(1, len(agents) + 1):
        for rank in range(1, len(agents)):
                cost += rank*(full[(agent, index[agent, rank])].varValue + 0.5*half[(agent, index[agent, rank])].varValue)
    return cost
   

# Main execution loop and writing results
with open("egal_results.csv","a") as egal_results:
    with open("stable_results.csv","a") as stable_results:
        
        # Only write headers once
        #stable_results.write("n,seed,c_setting,c,solvable,cost,odd,oddagents,time")
        #egal_results.write("n,seed,c_setting,c,solvable,cost,odd,oddagents,time")

        # Loop over even-sized instances with different numbers of agents
        for n in range(2,33,2):
            cap_lookup = [1, ceil((n-1)/4), ceil((n-1)/2), ceil((3*n-3)/4), n-1]
            for seed in range(0,1000):
                agents = generate_instance(n, seed)

                index = get_index(agents)
                line = []
                for c in range(5):
                    cap = cap_lookup[c]
                    caps = [cap]*n

                    
                    # Compute any stable half-matching
                    prob, full, half, pairs = stable_model(agents, caps, index)

                    start = time.process_time()
                    status = prob.solve(GUROBI(msg=False, env=env))
                    timing = time.process_time() - start

                    cost = get_cost(agents, full, half)

                    # Output the results
                    stats = get_cycle_stats(pairs, half)
                    stable_results.write(f"\nstable,{n},{seed},c{c},{cap},{1 if stats[0] == 0 else 0},{cost:.4f},{stats[0]},{stats[1]},{timing:.4f}")
                    

                    
                    # Compute an egalitarian stable half-matching
                    
                    prob, full, half, pairs = egal_model(agents, caps, index)

                    start = time.process_time()
                    status = prob.solve(GUROBI(msg=False, env=env))
                    timing = time.process_time() - start

                    cost = get_cost(agents, full, half)

                    # Output the results
                    stats = get_cycle_stats(pairs, half)

                    if LpStatus[status] != "Optimal":
                        raise Exception("Not computed to optimality!")
                    egal_results.write(f"\negal,{n},{seed},c{c},{cap},{1 if stats[0] == 0 else 0},{cost:.4f},{stats[0]},{stats[1]},{timing:.4f}")