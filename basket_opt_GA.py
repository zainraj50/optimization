import random
import pandas as pd
import datetime
import multiprocessing
import time
import itertools
import numpy as np
# starting time
start = time.time()
print("processing",multiprocessing.cpu_count())

quantity = pd.read_excel(r'C:\Users\user\PycharmProjects\basket_optimization\new_basket_LONG.xlsx', sheet_name='Quantity')
store = pd.read_excel(r'C:\Users\user\PycharmProjects\basket_optimization\new_basket_LONG.xlsx', sheet_name='Stores')

# setup data
data = [(1,1,1,1,1)]

def cal(basket, stores):
    ind = 0
    store_price = []
    quantity_ = quantity.iloc[1].values

    for i,j in enumerate(basket):


        if stores[0][0] == j:#store_:

                #print('bas:',bas,'j:',j)

                #print('index:',i,'store_',store_[0])
                stores_=stores[0]
               # print('stores_:',stores_)
                col_name = "triggered_delivery"

                index_no = store.columns.get_loc(col_name)


               # print('index no',index_no)
                store_array=stores_[1:index_no]
              #  print('store_array:',store_array)
                store_price.append(store_array[i] * quantity_[i])
        else:
                store_price.append(0)

    return store_price#sum_
def unique(list1):
    x = np.array(list1)
    return np.unique(x)

def fitness(basket,store):
    stores_=unique(basket)
    li=[]
    net = []
    #stores=[[store.iloc[i].values for i in range(len(store))]]#[store[store['STORE'] == j].values for i, j in enumerate([2,1,1,2,2])]##

    stores=[store[store['STORE'] == x].values for x in stores_]
    #print('stores:',stores[0])

    for i in stores:
     #   print('store:',i)
        for j in i:
           # print('store j',j)
            basket_store=cal(basket,[j])
            #print('basket:',basket)
            li.append([j[0],sum(basket_store)])
    #return li
    #print('li:',li)
    for total in li:
       # print('total of baskets:',total)
        store_data=stores#store[store['STORE'] == total[0]].values
        # print('total for store:',total[0])
        # print('store_data:',store_data[0][0][0])

        if total[1] > 0 and total[1]>= store_data[0][0][6]:
            #print('store_data[0][6]:',store_data[0][6])
            delivery = 0
        elif total[1] > 0 and total[1] != store_data[0][0][6]:
            #print('store_data[7]:', store_data[0][7])
            delivery =  store_data[0][0][7]
        else:
            delivery=0#store_data[0][0][7]

        # print('delivery:',delivery)
        # print('store:',store_data[0][0])
        # print('total:',total)
        discount=0
        if total[1] > store_data[0][0][8] and store_data[0][0][9] == 0:
            dis=store_data[0][0][10]
            disc=dis/100
            discount=disc * total[1]
        elif total[1] > store_data[0][0][8] and store_data[0][0][9] != 0:
            discount=store_data[0][0][9]
        elif total[1] < store_data[0][0][8]:
            discount=0
        #print('discount:',discount)
        Net=total[1] + delivery - discount
        net.append(Net)
    tot=sum(net)




    return tot



def get_fitness(guess):
    fitnes_value=fitness(guess,store)
    return fitnes_value

def generate_parent(data,store):
    length = len(store)
    #print(length)
    x = []
    for i in data:
        #print(i)
        x.append([random.randint(1, length) for _ in i])

    return x[0]


random.seed()

heuristic_or_not=1
population_size=30
heuristic_basket=[2,1,1,2,2]
survival_rate=10
randomization=20
no_of_offspring=  2
no_of_bits_to_mutate=20
no_of_pop_to_mutate=100
condition_breaker=60
breaker=1000
def generate_population(heuristic_or_not,population_size,heuristic_basket):
    if heuristic_or_not == 0:
        population=[generate_parent(data,store) for i in range(population_size)]
    else:
        population_size=population_size - heuristic_or_not
        population = [generate_parent(data, store) for i in range(population_size)]
        population.append(heuristic_basket)
    return sorted(population)

population=generate_population(heuristic_or_not,population_size,heuristic_basket)
population_evaluate=[[i,get_fitness(j)] for i,j in enumerate(population)]
print(population)
print(population_evaluate)

def selection(population,population_evaluate,survival_rate):
    survive=survival_rate / 100
    survival_rate=round(survive * len(population))

    li=[]
    for i in population_evaluate:
        li.append(i[1])
    li.sort()

    survived=[]
    for i in population_evaluate:
        if i[1] in li[:survival_rate] and i not in survived:
            survived.append(i)

    # for ind,val in enumerate(population_evaluate):
    #     for ind2,val2 in enumerate(survive_parents):
    #         if val[1] < val2[1] and val not in survive_parents:
    #             survive_parents[ind2] =val

    sur=[population[i[0]] for i in survived]
    return sur  #,survived



#print(selection(population,population_evaluate,survival_rate))

def crossover(survived,rand,offspring):
    """Crossover (mate) two parents to produce two children.

    :param survived: candidate solution representation (list)
    :param rand: randomly choosen solution which again append to survived
    :param offspring: number of offspring to be created for each couple
    :returns: new crossover list of solutions

    """



    ran=rand / 100
    rand=round(ran * len(survived))
    #print('random:',rand)

    ind_rand=random.choices(survived, k = rand)# for i in range(rand)]
    #print('ind_rand:',ind_rand)
    for i in ind_rand:
        survived.append(i)
    #print('survived after random:',survived,'length:',len(survived))
    cross=[]
    #print('len of survived:',len(survived))
    first = survived[0]
    length_of_survived=len(survived)
    n=0
    for i in survived[1:]:
        n+=1

        # print('cross before loop:', cross)
        # print('first before loop:', first)

        if offspring == 2:
            index = random.randrange(1, len(survived[0]))
#            print('i:',i,'first:',first)
            #print('index:',index)
            child_1 = first[:index] + i[index:]
            child_2 = i[:index] + first[index:]
            cross.append(child_1)
            cross.append(child_2)
            if int(n + 1) == length_of_survived:
                first=survived[0]
            else:
                first=i
            #print('first:', first)
        elif offspring == 3:
            index = random.randrange(1, len(survived[0]))
            #print('index:',index)
            child_1 = first[:index] + i[index:]
            child_2 = i[:index] + first[index:]
            index2 = random.randrange(1, len(survived[0]))
            child_3 =first[:index2] + i[index2:]
            cross.append(child_1)
            cross.append(child_2)
            cross.append(child_3)
            if int(n + 1) == length_of_survived:
                first = survived[0]
            else:
                first = i
        elif offspring ==4:
            index = random.randrange(1, len(survived[0]))
            #print('index:',index)
            child_1 = first[:index] + i[index:]
            child_2 = i[:index] + first[index:]
            index2 = random.randrange(1, len(survived[0]))
            child_3 =first[:index2] + i[index2:]
            child_4 = i[:index2] + first[index2:]
            cross.append(child_1)
            cross.append(child_2)
            cross.append(child_3)
            cross.append(child_4)
            if int(n + 1) == length_of_survived:
                first = survived[0]
            else:
                first = i
        elif offspring == 5:
            index = random.randrange(1, len(survived[0]))
            #print('index:',index)
            child_1 = first[:index] + i[index:]
            child_2 = i[:index] + first[index:]
            index2 = random.randrange(1, len(survived[0]))
            child_3 =first[:index2] + i[index2:]
            child_4 = i[:index2] + first[index2:]
            index3 = random.randrange(1, len(survived[0]))
            child_5 = first[:index3] + i[index3:]
            cross.append(child_1)
            cross.append(child_2)
            cross.append(child_3)
            cross.append(child_4)
            cross.append(child_5)
            if int(n + 1) == length_of_survived:
                first = survived[0]
            else:
                first = i
        elif offspring == 6:
            index = random.randrange(1, len(survived[0]))
            #print('index:',index)
            child_1 = first[:index] + i[index:]
            child_2 = i[:index] + first[index:]
            index2 = random.randrange(1, len(survived[0]))
            child_3 =first[:index2] + i[index2:]
            child_4 = i[:index2] + first[index2:]
            index3 = random.randrange(1, len(survived[0]))
            child_5 = first[:index3] + i[index3:]
            child_6 = i[:index3] + first[index3:]
            cross.append(child_1)
            cross.append(child_2)
            cross.append(child_3)
            cross.append(child_4)
            cross.append(child_5)
            cross.append(child_6)
            if int(n + 1) == length_of_survived:
                first = survived[0]
            else:
                first = i

    return cross

# survived=selection(population,population_evaluate,survival_rate)
# print('survived:',survived)
# cross=crossover(survived,randomization,no_of_offspring)
# print('crossover:',cross)

# print('len of cross:',len(cross))
# print('cross:',cross)



def mutate(cross,bits_to_mutate,population_to_mutate):
    ### no of bits to mutate ###
    no_of_bits=bits_to_mutate / 100
    bits_to_mutate=round(no_of_bits * len(cross[0]))
    print('bits to mutate:',bits_to_mutate)

    ####   END    #####

    ### no of population of crossovers to mutate ####
    no_of_pop=population_to_mutate / 100
    population_to_mutate=round(no_of_pop * len(cross))
    print('population_to_mutate:',population_to_mutate)

    ###    END   ####

    mutated=[]
    #print('cross:',cross)
    for i in range(population_to_mutate):
        #print('i:', i)
        offspring = cross[i]
        #print('offspring:', offspring)
        #
        if bits_to_mutate == 0 or bits_to_mutate <= 0:
     #       print('------------mutation if condition-------------')
     #       print('offspring_1:', offspring)
            index = random.randrange(0, len(offspring))
            # print("index",index)
            childGenes = list(offspring)
            #mutated.append(childGenes)
            cross[i] = childGenes
            #cross[i]=childGenes
            #return mutated
        else:
      #      print('------------mutation else condition-------------')
            indexes=random.sample(range(len(offspring)),bits_to_mutate)#[random.randrange(0, len(offspring)) for i in range(bits_to_mutate)]
           # mutated_list=[bits_mutate(offspring) for i in range(bits_to_mutate)]
            bits=[random.sample({i + 1 for i in range(len(store))}, 2) for j in range(0,len(indexes))]

          #  print('offspring_2:',offspring)
            childGenes = list(offspring)
      #      print('ind:', indexes, 'bit:', bits)
            n=0
            for ind,bit in zip(indexes,bits):
                n+=1
            #    print('ind:',ind,'bit:',bit)

                #print('offspring_3:',childGenes)
                newGene, alternate = bit[0],bit[1]
                #print('newGene:',newGene,'alternate:',alternate)
                childGenes[ind] = alternate \
                    if newGene == childGenes[ind] \
                    else newGene
             #   print('childGenes:', childGenes)
                childGenes=childGenes
              #  print('cross[i]:',cross[i])
                if bits_to_mutate == n:
                    cross[i]=childGenes
               #     print('i:',i,'cross[i]:',cross[i])
                    #mutated.append(childGenes)
            #print('mutated:',mutated)
    return cross#mutated

                #cross[i]=childGenes

        #return mutated,#indexes,bits#cross#bits_to_mutate,population_to_mutate

#print(mutate(cross,no_of_bits_to_mutate,no_of_pop_to_mutate))

def display(guess):
    startTime = datetime.datetime.now()
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))

def largest(poulation_fitness):
    largest = poulation_fitness[0]
    for i in poulation_fitness:
        if i[1]> largest[1]:
            largest=i
    return largest

best_fit=[]
for i in population_evaluate:
    if len(best_fit)==0:

        best_fit.append(i)

    if len(best_fit) ==1 and float(best_fit[0][1]) <= float(i[1]):
        # print('i',i)
        # print(best_fit[0])
        continue
    else:
        best_fit.pop()
        best_fit.append(i)
print('best_fit:',best_fit)
print('best fit chromosome:',population[best_fit[0][0]],'best fitness:',best_fit[0][1] )

bestParent = population[best_fit[0][0]]
bestFitness = best_fit[0][1]

fit=[]
best_basket=[]

fit.append(bestFitness)#(childFitness)
best_basket.append(bestParent)#(child)
display(best_basket[0])

num=0
# if len(store) <= 10:  # discuss
#     breaker = len(store) ** 2
# elif len(store) >=500:
#     breaker=500
# else:
#     breaker = len(store)
first_breaker=0
end_breaker=0
while True: # here will need discussion
     first_breaker+=1
     end_breaker+=1
     survived=selection(population,population_evaluate,survival_rate)
     print('survived:', survived)
     cross_=crossover(survived,randomization,no_of_offspring)
     print('cross:', cross_)
     mutated_=mutate(cross_,no_of_bits_to_mutate,no_of_pop_to_mutate)
     print('mutated:',mutated_)
     print('best_parent:',best_basket,'best_fit:',fit)
     mut_fit=[]
     for mut in mutated_:
         child_fitness=get_fitness(mut)
         if  child_fitness < fit[0]:
     #        print('executing if')
             best_basket[0]=mut
             fit[0]=child_fitness
             #print('best_fit:',best_fit[0][0],'best_fit:',best_fit)
             index=best_fit[0][0]
             population[index]=mut
             population_evaluate[index]=[index,child_fitness]
             first_breaker=0
         #     best_fit[0]=child_fitness
         elif child_fitness > fit[0]:

             biggest_value_basket=largest(population_evaluate)
             if biggest_value_basket[1] > child_fitness:
      #           print('executing elif if')
                 index=biggest_value_basket[0]
                 population[index]=mut
                 population_evaluate[index]=[index,child_fitness]
       #          print('[index,child_fitness]:',[index,child_fitness])

         #     print('mutated fitness:', mut_fitness, 'biggest_value_basket:', biggest_value_basket)
         #     if mut_fitness < biggest_value_basket[1]:
         #         index = best_fit[0][0]
         #         population[index] = child
         #         population_fitnes[index] = [index, childFitness]
     print('best_basket:',best_basket,'fit:',fit)
     print(population_evaluate)
     if first_breaker == condition_breaker:
         print('first_breaker:',first_breaker,'condition breaker:',condition_breaker)
         break
     elif end_breaker == breaker:
         print('end_breaker:',end_breaker,'breaker:',breaker)
         break
#
