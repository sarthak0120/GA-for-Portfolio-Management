import math
import numpy as np
import copy 
import matplotlib.pyplot as plt


class parameters:
    def __init__(self):
        self.mutation_rate  = 0.1
        self.crossover_rate = 0.5
        self.N = 100
        self.avenues = []
        self.avenues_params = []
        self.w0 = 1
        self.w1 = 1
        self.w2 = 1
        self.w3 = 1
        
def decimal_chromosome(bin_chromosome):
    dec_chromosome = []
    dec = 0
    for i in range(50):
        x = i%10
        dec = dec + bin_chromosome[i]*math.pow(2, 9 - x)
        
        if x == 9:
            dec_chromosome.append(dec)
            dec = 0
    return dec_chromosome

def is_valid(member): 
    dec_sum  = 0
    dec_member = decimal_chromosome(member)
    for item in dec_member:
        dec_sum = dec_sum + item

    return dec_sum == 1023

def cover():
    member = [0 for i in range(50)]
    while(not is_valid(member)):
        member = [np.random.randint(2) for i in range(50)]
    return member

def initialize():
    params = parameters()
    population = []
    
    while(len(population)<params.N):
        population.append(cover())
    
    for i in range(5):
        params.avenues[i] = input("Enter avenue ", i+1, ": ")
    
    for i in range(5):
        temp_list = []
        for j in range(4):
            if j==0:
                temp_list.append(int(input("Enter Risk (Avenue ", i+1, "): ")))
                
            if j==1:
                temp_list.append(int(input("Enter Return (Avenue ", i+1, "): ")))
                
            if j==2:
                temp_list.append(int(input("Enter Liquidity (Avenue ", i+1, "): ")))
                
            if j==3:
                temp_list.append(int(input("Enter Complexity (Avenue ", i+1, "): ")))
                
        params.avenues_params.append(temp_list)
    return population, params

def fitness(member, params):
    dec_member = decimal_chromosome(member)
    tot_risk = 0
    tot_return = 0
    tot_liquidity = 0
    tot_complexity = 0
    
    for i in range(len(dec_member)):
        tot_risk = tot_risk + dec_member[i]*params.avenues_params[i][0]
        tot_return = tot_return + dec_member[i]*params.avenues_params[i][1]
        tot_liquidity = tot_liquidity + dec_member[i]*params.avenues_params[i][2]
        tot_complexity = tot_complexity + dec_member[i]*params.avenues_params[i][3]

    return (params.w1*tot_return + params.w2*tot_liquidity)/(params.w0*tot_risk + params.w3*tot_complexity)

def selection(population, params, n):
    
    fitness_list = []
    for member in population:
        fitness_list.append(fitness(member, params))
    
    fitness_sum = 0
    for item in fitness_list:
        fitness_sum = fitness_sum + item
    
    probabilities = []
    for item in fitness_list:
        probabilities.append(item/fitness_sum)
    
    cumulative_prob = [0]
    for i in range(len(fitness_list)):
        cumulative_prob.append(probabilities[i] + cumulative_prob[len(cumulative_prob)-1])
        
    mating_pool = []
    for i in range(n):
        random_num = np.random.random()
        for j in range(len(cumulative_prob)-1):
            if (cumulative_prob[j]<random_num and cumulative_prob[j+1]>random_num):
                mating_pool.append(population[j])
    
    return mating_pool, fitness_sum/len(population)
        
        
def crossover(mating_pool):
    
    temp_1 = np.random.randint(len(mating_pool))
    temp_2 = np.random.randint(len(mating_pool))
    
    parent_copy_1 = copy.deepcopy(mating_pool[temp_1])
    parent_copy_2 = copy.deepcopy(mating_pool[temp_2])

def mutate(mating_pool):
    pass

def run_ga():
    
    population, params = initialize()
    avg_fitness_list = []
    iteration_list = []
    
    for i in range(1000):
        
        mating_pool, avg_fitness = selection(population)
        avg_fitness_list.append(avg_fitness)
        iteration_list.append(i)
        
        if np.random.rand()<params.crossover_rate:
            crossover(mating_pool)
        
        if np.random.rand()<params.mutation_rate:
            mutate(mating_pool)
        
        population = mating_pool
        
    plt.plot(avg_fitness_list, iteration_list)
