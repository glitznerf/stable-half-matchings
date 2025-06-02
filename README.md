
# Approximation Algorithms for Stable Roommates

## Purpose

Code and empirical results for [_Unsolvability and Beyond in Many-To-Many Non-Bipartite Stable Matching_, Technical Report no. 2505.11456, Computing Research Repository, Cornell University Library, 2025.](https://arxiv.org/abs/2505.11456)

## Status

Manuscript submitted.


## Get Started
1. Make sure you have a recent Python 3 version installed. 
2. Install required packages: e.g., from the main project folder, run `pip install -r requirements.txt`. 
3. Understand the code structure in `experiment.py`.

## Structure
```
project
└───results
│   └───raw          	-- database containing all experimental results
│   └───processed		-- summary statistics from a variety of angles
└───experiment.py		-- random generation, ILP models and experiment loop
└───read_results.py		-- reads raw results and creates summary statistics
```

## People
This is a project by F Glitzner ([Website](https://glitznerf.github.io/)).