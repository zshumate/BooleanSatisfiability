'''
Authors: Adam Vest, Dane Copple, Zack Shumate
CECS 545 Final Project
'''


import argparse
import time
import random
import numpy as np


#constants
VAR_COUNT_OFFSET = 2
CLAUSE_COUNT_OFFSET = 3


#options for running solver
class GASATOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('--data_path', default="./sat_data_20_91/uf20-01.cnf", help="data file containing problem to satisfy")
        self.parser.add_argument('--visualize_results', type=int, default=1, help="whether to visualize results")

    def parse_args(self):
        return self.parser.parse_args()

#solver structure for 3-SAT
class SATSolver():
    def __init__(self, data_path):
        self.variables, self.clauses = [], []
        self.variable_count, self.clause_count = 0, 0

        with open(data_path) as f:
            for line in f:
                words = line.split()

                if words[0] == "c":
                    continue
                elif words[0] == "%":
                    break
                elif words[0] == "p":
                    self.variable_count = int(words[VAR_COUNT_OFFSET])
                    self.clause_count = int(words[CLAUSE_COUNT_OFFSET])
                    self.variables = [False for i in range(self.variable_count)]
                else:
                    clause = []

                    for i in range(len(words[:-1])):
                        clause.append(int(words[i]))

                    self.clauses.append(clause)

    def makes_true(self, clause, variables):
        for var in clause:
            if var > 0 and variables[var-1] == 1:
                return 1
            elif var < 0  and variables[(-1*var)-1] == 0:
                return 1

        return 0

    def test_solution(self, variables):
        true_count = 0

        for clause in self.clauses:
            true_count += self.makes_true(clause, variables)

        return true_count


# initializes population according to some strategy
def initialize_population():
    print "hi"

#selects parents to mate based on probabilities assigned by parent individual costs
def select_mating_pairs():
    print "hi"

#combines two parent solutions to produce a child
def crossover():
    print "hi"

#combine population solutions via Wisdom of Crowds and find its weight
def combine_via_woc():
    print "hi"

#find the best individual and its cost in the current generation
def get_best_child():
    print "hi"

#solve TSP using a genetic algorithm
def ga_solve():
    start_time = time.time()
    population = initialize_population()
    generation_count, no_improvement_count = 0, 0
    best_cost, best_solution = np.inf, None
    combined_solution_costs, best_child_costs = [], []

    while no_improvement_count < args.generations_limit:
        parents_to_mate = select_mating_pairs()
        children = [crossover() for parents in parents_to_mate]
        children = [mutate() for child in children]
        combined_soln, combined_soln_cost = combine_via_woc()
        best_child, best_child_cost = get_best_child()
        population = children

        if best_child_cost < ((1-args.improvement_limit) *  best_cost):
            best_solution = best_child
            best_cost = best_child_cost
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        generation_count += 1
        combined_solution_costs.append((generation_count, combined_soln_cost))
        best_child_costs.append((generation_count, best_child_cost))

        print "Overall Best Solution: %s" % best_solution
        print "Overall Best Solution Cost: %g" % best_cost
        print "Generation %d Combined Solution: %s" % (generation_count, combined_soln)
        print "Generation %d Combined Solution Cost: %g" % (generation_count, combined_soln_cost)
        print "Generation %d Best Child: %s" % (generation_count, best_child)
        print "Generation %d Best Child Cost: %g\n" % (generation_count, best_child_cost)

    print "Execution Time: %g seconds" % (time.time() - start_time)

    if args.visualize_results:
        print "hi"


if __name__ == "__main__":
    args = GASATOptions().parse_args()
    sat_solver = SATSolver(args.data_path)
    print sat_solver.test_solution([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1])
    # ga_solve()
