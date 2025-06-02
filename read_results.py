import pandas as pd

stable = pd.read_csv('results/raw/stable_results.csv')
egal = pd.read_csv('results/raw/egal_results.csv')


## SOLVABILITY

c0_frame = stable[stable['c_setting'] == "c0"].groupby("n")["solvable"].mean().rename("c0")
c1_frame = stable[stable['c_setting'] == "c1"].groupby("n")["solvable"].mean().rename("c1")
c2_frame = stable[stable['c_setting'] == "c2"].groupby("n")["solvable"].mean().rename("c2")
c3_frame = stable[stable['c_setting'] == "c3"].groupby("n")["solvable"].mean().rename("c3")
c4_frame = stable[stable['c_setting'] == "c4"].groupby("n")["solvable"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/solvability.csv', index=True)  

print("\nSOLVABILITY:")

with open("results/processed/solvability.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## ODD CYCLES

c0_frame = stable[stable['c_setting'] == "c0"].groupby("n")["odd"].mean().rename("c0")
c1_frame = stable[stable['c_setting'] == "c1"].groupby("n")["odd"].mean().rename("c1")
c2_frame = stable[stable['c_setting'] == "c2"].groupby("n")["odd"].mean().rename("c2")
c3_frame = stable[stable['c_setting'] == "c3"].groupby("n")["odd"].mean().rename("c3")
c4_frame = stable[stable['c_setting'] == "c4"].groupby("n")["odd"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/oddcycles.csv', index=True)  

print("\nODD CYCLES:")

with open("results/processed/oddcycles.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## ODD AGENTS

c0_frame = stable[stable['c_setting'] == "c0"].groupby("n")["oddagents"].mean().rename("c0")
c1_frame = stable[stable['c_setting'] == "c1"].groupby("n")["oddagents"].mean().rename("c1")
c2_frame = stable[stable['c_setting'] == "c2"].groupby("n")["oddagents"].mean().rename("c2")
c3_frame = stable[stable['c_setting'] == "c3"].groupby("n")["oddagents"].mean().rename("c3")
c4_frame = stable[stable['c_setting'] == "c4"].groupby("n")["oddagents"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/oddagents.csv', index=True)  

print("\nODD AGENTS:")

with open("results/processed/oddagents.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## STABLE TIMING

c0_frame = stable[stable['c_setting'] == "c0"].groupby("n")["time"].mean().rename("c0")
c1_frame = stable[stable['c_setting'] == "c1"].groupby("n")["time"].mean().rename("c1")
c2_frame = stable[stable['c_setting'] == "c2"].groupby("n")["time"].mean().rename("c2")
c3_frame = stable[stable['c_setting'] == "c3"].groupby("n")["time"].mean().rename("c3")
c4_frame = stable[stable['c_setting'] == "c4"].groupby("n")["time"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/timingstable.csv', index=True)  

print("\nSTABLE TIMING:")

with open("results/processed/timingstable.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## EGAL TIMING

c0_frame = egal[egal['c_setting'] == "c0"].groupby("n")["time"].mean().rename("c0")
c1_frame = egal[egal['c_setting'] == "c1"].groupby("n")["time"].mean().rename("c1")
c2_frame = egal[egal['c_setting'] == "c2"].groupby("n")["time"].mean().rename("c2")
c3_frame = egal[egal['c_setting'] == "c3"].groupby("n")["time"].mean().rename("c3")
c4_frame = egal[egal['c_setting'] == "c4"].groupby("n")["time"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/timingegal.csv', index=True)  

print("\nEGAL TIMING:")

with open("results/processed/timingegal.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## STABLE COST

c0_frame = stable[stable['c_setting'] == "c0"].groupby("n")["cost"].mean().rename("c0")
c1_frame = stable[stable['c_setting'] == "c1"].groupby("n")["cost"].mean().rename("c1")
c2_frame = stable[stable['c_setting'] == "c2"].groupby("n")["cost"].mean().rename("c2")
c3_frame = stable[stable['c_setting'] == "c3"].groupby("n")["cost"].mean().rename("c3")
c4_frame = stable[stable['c_setting'] == "c4"].groupby("n")["cost"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/coststable.csv', index=True)  

print("\nSTABLE COST:")

with open("results/processed/coststable.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))



## EGAL COST

c0_frame = egal[egal['c_setting'] == "c0"].groupby("n")["cost"].mean().rename("c0")
c1_frame = egal[egal['c_setting'] == "c1"].groupby("n")["cost"].mean().rename("c1")
c2_frame = egal[egal['c_setting'] == "c2"].groupby("n")["cost"].mean().rename("c2")
c3_frame = egal[egal['c_setting'] == "c3"].groupby("n")["cost"].mean().rename("c3")
c4_frame = egal[egal['c_setting'] == "c4"].groupby("n")["cost"].mean().rename("c4")

solvability = pd.concat([c0_frame, c1_frame, c2_frame, c3_frame, c4_frame], axis=1, join="inner")

solvability.to_csv('results/processed/costegal.csv', index=True)  

print("\nEGAL COST:")

with open("results/processed/costegal.csv", "r") as f:
    for line in f:
        print(" ".join(line.strip().split(",")))