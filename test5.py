import random
import pandas as pd
import datetime
import multiprocessing
import time

# starting time
start = time.time()
print("processing",multiprocessing.cpu_count())

quantity = pd.read_excel(r'C:\Users\user\PycharmProjects\basket_optimization\new_basket_LONG.xlsx', sheet_name='Quantity')
store = pd.read_excel(r'C:\Users\user\PycharmProjects\basket_optimization\new_basket_LONG.xlsx', sheet_name='Stores')

#calculation
# def cal(basket, store):
#     ind = 0
#     # print(basket,stores)
#     store_price = []
#     # print(basket,store)
#     # for length,i in enumerate(basket):
#     #         #print(length,i)
#     #         print(i[1])
#     # for i in range(len(store)):
#     #print("basket:",basket)
#     for ind, j, quan in zip(range(len(basket)), basket, quantity.loc[1].values):
#         # print(stores)
#         #print("j:", j)
#         df_store = store[['STORE']].values  # store.loc[store['STORE'] == j]
#         df_store_id = df_store  # .iat[0,0]
#         #print("store_id:",df_store_id[0][0])
#
#         # print(df_store_id,j,quan)
#         if int(df_store_id[0][0]) == int(j):
#             # store_=store.loc[(store['STORE'] == j) & ()]
#             store_ = store[store['STORE'] == j].values
#             col_name = "triggered_delivery"
#             index_no = store.columns.get_loc(col_name)
#             #print('triggered_delivery index:',index_no)
#             st = store_[0][1:index_no]
#             store_price.append(st[ind] * quan)
#             # ind+=1
#         else:
#             store_price.append(0)
#     #print("store_pric:",store_price)
#             # ind+=1
#     sum_ = sum(store_price)
#     # total += int(sum(price))
#     triggered_delivery = store['triggered_delivery'].values  # [0].astype(int)
#     triggered_discount = store['triggered_discount'].values  # [0].astype(int)
#     discount_percent = store['discount'].values  # [0].astype(int)
#
#     if int(discount_percent) == 0:
#         discount_percent_ = store['discount_percent'].values
#         discount_percent = sum_ * (int(discount_percent_) / 100)
#     else:
#         discount_percent = discount_percent
#
#     if sum_ > 0 and sum_ >= int(triggered_delivery):
#         delivery = 0
#     # elif sum_ == 0 and sum_ <= int(triggered_delivery):
#     #     delivery = 0
#     else:
#         delivery = store['discount_delivery'].values  # [0]
#         #
#     if sum_ >= int(triggered_discount):
#         discount = discount_percent
#     else:
#         discount = 0
#         #
#     Net = sum_ + delivery - discount
#     print('Net:',Net)
#     final = [store_price, sum_, delivery, discount, Net]
#     print("final:",final)
#     return Net
#     # print(store_price)
#     # print(store_price[5:])
#     # print(quan)
#     # print(j,quan)
#
#     # for k in range(len(i)):
#     #         ind=k
#     #         store_=store[store['STORE'] == j].values
#     #         st=store_[0][0:6]
#     #         store_price.append(st[ind]*quan)
#     #         # price=[i * j for i,j in zip(st,quantity.loc[1])]
#     #         # print(price)
#
#
#
#
# def fitness_(basket, quantity, store):
#     fitness = 0
#     bas = []
#     baskets = []
#     prices = []
#     total = []
#     #print("basket/individual:",basket)
#     # price=0
#     for i in range(len(data)):
#         num = 0
#         # prices=[]
#         # print(basket.loc[i].values,quantity.loc[i].values)
#         for j in range(len(store)):
#             # print(cal(data[i],store.loc[store['STORE'] == j + 1]))#,store.loc[store['STORE'] == ind +1]))
#             prices.append(cal(basket,store.loc[store['STORE'] == j + 1]))#cal(data[i], store.loc[store['STORE'] == j + 1]))
#             baskets.append(basket)#data[i])
#             if j == 1:
#                 tot = float(sum(prices))
#                 if len(total) == 0:
#                    # print("prices:",prices,"basket:",baskets)
#                     total.append(float(sum(prices)))
#                     bas.append(baskets[0])
#
#                     # total.append(prices)
#                     prices = []
#                     baskets = []
#                 elif len(total) > 0 and total[0] < tot:
#                     prices = []
#                     baskets = []
#                 elif len(total) > 0 and total[0] > tot:
#                     total[0] = tot
#                     bas[0] = baskets[0]
#                     prices = []
#                     baskets = []
#             else:
#                 pass
#     print('total forwarded:',total,'basket forwarded:',bas)
#     return total[0],bas[0]
#

def cal(basket, store):
    ind = 0
    #print('store:',store['STORE'][0])
   # print('basket:',basket)
    # print(basket,stores)
    store_price = []

    #for i in range(len(basket)):
    for i,j in enumerate(basket):
        #print(store['STORE'][j-1])
        store_ = store[store['STORE'] == j].values
        #print('index:',i,'store_',store_[0])
        col_name = "triggered_delivery"
        index_no = store.columns.get_loc(col_name)
       # print('index no',index_no)
        store_array=store_[0][1:index_no]
        store_price.append(store_array[i])
    #print('store_price:',store_price)
    quantity_=quantity.iloc[1].values
    final_price=[i*j for i,j in zip(store_price,quantity_)]
    sum_=sum(final_price)
    #print('final_price:',final_price,'sum final_price:',sum_)
    return sum_



# setup data
data = [(1,1,1,1,1)]#[(1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1)]

data_1=[1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1]


# geneSet = 1,2
# target = [(2,1,1,2,2)]
# optimalFitness = 45.0

def generate_parent(data,store):
    length = len(store)
    #print(length)
    x = []
    for i in data:
        #print(i)
        x.append([random.randint(1, length) for _ in i])
    #     fit=fitness_(x[0],quantity,store)
    #     print(fit)
    #     if fit[0] < 47.0:
    #         x.append([random.randint(1, length) for _ in i])
    #     else:
    #         x.append([random.randint(1, length) for _ in i])
    #         fit = fitness_(x[0], quantity, store)
#    print("return",x[0])
    return x[0]

# indi=generate_parent(data)
# print("individual:",indi)

# def get_fitness(guess):
#     fitnes_value=fitness_(guess,quantity,store)
#     return fitnes_value[0]
def get_fitness(guess):
    fitnes_value=cal(guess,store)
    return fitnes_value

    # if 50 <= fitnes_value[0] :
    #     return 1
    # else:
    #     return 0


def crossover(parent_1, parent_2):
    """Crossover (mate) two parents to produce two children.

    :param parent_1: candidate solution representation (list)
    :param parent_2: candidate solution representation (list)
    :returns: tuple containing two children

    """
    index = random.randrange(1, len(parent_1))
    child_1 = parent_1[:index] + parent_2[index:]
    child_2 = parent_2[:index] + parent_1[index:]
    return child_1, child_2



def mutate(parent):
    #print("parent:",parent)
    index = random.randrange(0, len(parent))
    #print("index",index)
    childGenes = list(parent)
  #print("child genes:",childGenes)
    newGene, alternate = random.sample({i+1 for i in range(len(store))}, 2)
    #print("genSet:",geneSet)
    print("newGene:",newGene,"alternative:",alternate)
    childGenes[index] = alternate \
    if newGene == childGenes[index] \
    else newGene
    return childGenes

#print(mutate(indi))


def display(guess):
    startTime = datetime.datetime.now()
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))



random.seed()
# bestParent = generate_parent(data,store)
# bestFitness = get_fitness(bestParent)


population=[generate_parent(data,store) for i in range(len(store))]#(len(data_1)**2)]#len(store))]#len(store))]

# population = []
# for i in range(1,8):
#     for j in range(1,8):
#         for k in range(1,8):
#             for l in range(1,8):
#                 for m in range(1,8):
#                     population.append([i,j,k,l,m])



# li=[]
# for i in range(9765625):
#     x=generate_parent(data,store)
#     print(x)
#     li.append(x)
print(population)
print('length of population:',len(population))
population_fitnes=[[i,get_fitness(j)] for i,j in enumerate(population)]
print(population_fitnes)
best_fit=[]
for i in population_fitnes:
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



def selection(population_passed,fitness_members):
    #Tournament pool
    # members = random.sample(population_passed,k)
    # fitness_members=sorted([(i,get_fitness(j)) for i, j in enumerate(members)])
    members=population_passed
    lowest=fitness_members[0]
    lowest2=fitness_members[1]
    for i in fitness_members:
        if i[1] < lowest[1]:
            lowest2 = lowest
            lowest = i
        elif lowest2 == lowest or lowest2[1] > i[1]:
            lowest2 = i

    return members[lowest[0]],members[lowest2[0]]#,lowest,lowest2#fitness_members,lowest,lowest2#,best_fit#[best_fit[0][0]],best_fit[0][1]

#print('selection:',selection(population,population_fitnes))


def largest(poulation_fitness):
    largest = poulation_fitness[0]
    for i in poulation_fitness:
        if i[1]> largest[1]:
            largest=i
    return largest

print('largest:',largest(population_fitnes))

bestParent = population[best_fit[0][0]]
bestFitness = best_fit[0][1]



fit=[]
best_basket=[]

fit.append(bestFitness)#(childFitness)
best_basket.append(bestParent)#(child)
display(best_basket[0])
num=0
if len(store) <= 10:  # discuss
    breaker = len(store) ** 2
elif len(store) >=500:
    breaker=500
else:
    breaker = len(store)
while True: # here will need discussion



    print('new generation try')

    p1,p2=selection(population,population_fitnes)
    cross_1,cross_2=crossover(p1,p2)#(best_basket[0],random.choice(population))#population[num])#generate_parent(data,store))
    # if get_fitness(cross_1) <= get_fitness(cross_2):
    #     cross=cross_1
    # else:
    #     cross=cross_2
    # print('crossover basket:',cross)
    child=[]
    child_fitness_=[]
    for cross in ([cross_1,cross_2]):
        childs=mutate(cross)
        child.append(childs)#(cross)
        #print("child:", child)
        child_fitness_.append(get_fitness(childs))
        # fit.append(bestFitness)
        # best_basket.append(bestParent)#
    num += 1
    print('num:',num)
    for child,childFitness in zip(child,child_fitness_):
        print('child:',child)
        print('child_fitness:',childFitness)
        if float(childFitness) < fit[0]:
            #print(num)
            fit[0]=childFitness
            best_basket[0]=child
            index=best_fit[0][0]
            population[index]=child
            population_fitnes[index]=[index,childFitness]
            num=0
            print('num 0:',num)
            # bestFitness = fit[0]#childFitness
            # bestParent = best_basket[0]#child



            display(child)

        if float(childFitness) > fit[0]:
            larg=largest(population_fitnes)
            population[larg[0]]=child
            population_fitnes[larg[0]]=[larg[0],childFitness]

    print('iteration',num)


    if num >=breaker:#len(store)**2:
        break



#
#
print('basket:',best_basket[0],' fit:',fit[0], 'final number of iteration:', num,'population fitness:',population_fitnes)
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")
#print([fitness_(i,quantity,store) for i in li])
    # if childFitness > bestFitness:
    #     print("creating new parent")
    #     random.seed()
    #     bestParent = generate_parent(data, store)
    #     bestFitness = get_fitness(bestParent)
    #     display(bestParent)

    # if num >= 10 :
    #     print('parent list number of iteration:',bestParent,'best price:',bestFitness,' number of iteration:',num)
    #     break
    # display(bestParent)
    # # #print("childFitness:", childFitness)
    # # if float(childFitness) == float(bestFitness) or float(childFitness) <= float(
    # #         bestFitness):  # float(optimalFitness) or float(childFitness) <= float(optimalFitness):
    # #     break
    # display(child)
    # bestFitness = childFitness
    # bestParent = child





      # if float(bestFitness) <= float(optimalFitness):
      #     print("parent created and passed !!")
      #     display(bestParent)
      #     return bestParent,bestFitness
      #
      #
      # elif float(bestFitness) <= float(optimalFitness):
      #         break
      # else:
      #     random.seed()
      #     bestParent = generate_parent(data)
      #     bestFitness = get_fitness(bestParent)
      #     display(bestParent)
      #     print("creating new parent")


# bestParent_=get_best(get_fitness, optimalFitness , data, display)
# print(bestParent_)

#print("bestParent:",bestParent)
# if bestParent[1] < optimalFitness:
#     return bestParent
#else:
# while True:
#   child = mutate(bestParent)
#   #print("child:", child)
#   childFitness = get_fitness(child)
#   if float(childFitness) >= 43.0:  # float(optimalFitness):
#       continue
#   display(child)
#   # #print("childFitness:", childFitness)
#   if float(childFitness) == float(43.0) or float(childFitness) <= float(
#           43.0):  # float(optimalFitness) or float(childFitness) <= float(optimalFitness):
#       break
#   display(child)
#   bestFitness = childFitness
#   bestParent = child


#print(get_best(get_fitness, optimalFitness , data, display))


# random.seed()
# startTime = datetime.datetime.now()
# bestParent = generate_parent(data)
# print("best parent:",bestParent)
# bestFitness = get_fitness(bestParent)
# print("best fitness:",bestFitness)
# # if float(bestFitness) > 50:
# #     bestParent=generate_parent(data)
# #     bestFitness = get_fitness(bestParent)
# # else:
# display(bestParent)
#
# while True:
#   child = mutate(bestParent)
#   childFitness = get_fitness(child)
#   if  float(childFitness) >= bestFitness:
#       #print("childFitness:", childFitness)
#       continue
#   display(child)
#
#   if childFitness == bestFitness or float(childFitness) <= bestFitness:
#       break
#   display(child)
#
#   # else:
#   #     display(child)
#   #     break
#   # elif float(childFitness) == float(41) or childFitness < float(41):
#   #     display(child)
#   #     print("bestFitness:",bestFitness)
#   #     print("childFitness:",childFitness)
#   #     break
#
#   # if childFitness >= len(bestParent):
#   #     break
#   bestFitness = childFitness
#   bestParent = child
