from ple import PLE
import pygame
import frogger_new
import numpy as np
from pygame.constants import K_w,K_a,K_F15, K_s
import math
# from constants import *
import random
import json
Kbox = 32


kfrogstep = 32
kstepsize = 1
with open('Q.json', 'r') as fp:
    Q = json.load(fp)
# with open('N_a.json', 'r') as fp:
#     N_a = json.load(fp)

# def write(Q, N_a):
#     with open('Q.json', 'w') as fp:
#         json.dump(Q, fp)
#     with open('N_a.json', 'w') as fp:
#         json.dump(N_a, fp)

def getfeatures(obs, action, complete):
    frog_x = obs['frog_x']
    frog_y = obs['frog_y']

    NW = pygame.Rect(frog_x - Kbox, frog_y - Kbox, Kbox, Kbox)
    N = pygame.Rect(frog_x, frog_y - Kbox, Kbox, Kbox)
    NE = pygame.Rect(frog_x + Kbox, frog_y - Kbox, Kbox, Kbox)

    W = pygame.Rect(frog_x - Kbox, frog_y, Kbox, Kbox)
    E = pygame.Rect(frog_x + Kbox, frog_y, Kbox, Kbox)

    SW = pygame.Rect(frog_x - Kbox, frog_y + Kbox, Kbox, Kbox)
    S = pygame.Rect(frog_x, frog_y + Kbox, Kbox, Kbox)
    SE = pygame.Rect(frog_x + Kbox, frog_y + Kbox, Kbox, Kbox)

    state_ = state()
    objects = obs['cars'] + obs['rivers'] + obs['homeR']
    for block in objects:
        if NW.colliderect(block):
            state_.up[0] = 1

        if N.colliderect(block):
            state_.up[1] = 1 
        if NE.colliderect(block):
            state_.up[2] = 1
        
        if W.colliderect(block):
            state_.up[0] = 1 
        if E.colliderect(block):
            state_.up[2] = 1 

        if SW.colliderect(block):
            state_.up[0] = 1
        if S.colliderect(block):
            state_.up[0] = 1 
        if SE.colliderect(block):
            state_.up[0] = 1 

    state_.level_y = int(frog_y)
    state_.action = action
    state_.level_x = int(math.ceil(frog_x/(kstepsize*kfrogstep)))
    state_.homes = obs['homes']



    state_.turtles1 = int(math.ceil((obs['rivers'][0][0]))/(kstepsize*kfrogstep))
    current_state = state_.getstate()
    str1 = ''.join(str(e) for e in current_state)
    return str1

class state():
    def __init__(self):
        self.up = [0,0,0]
        self.middle = [0,0,0]
        self.down = [0,0,0]
        self.level_x = 0
        self.level_y = 0
        self.action = None
        self.homes = 0
        self.turtles1 = 0

    def getstate(self):
        temp = []
        for i in self.up:
            temp.append(i)
        for i in self.middle:
            temp.append(i)
        for i in self.down:
            temp.append(i)
        temp.append(self.level_x)
        temp.append(self.level_y)
        
        for filled in range(len(self.homes)):
            if (filled == 0.33 or filled == 0.66):
                temp.append(1)
            else:
                temp.append(0)
        temp.append(self.turtles1)
        temp.append(self.action)
        return temp



class NaiveAgent():
    def __init__(self, actions):
        self.actions = actions
        self.step = 0
        self.NOOP = K_F15

    def pickAction(self, reward, obs, action, old_obs):
        # oldfeatures = getfeatures(old_obs, action,1)
        # if oldfeatures not in N_a:
        #     N_a[oldfeatures] = 1

        # N_a[oldfeatures] += 1
        # Qsample = reward + kGamma*(maxQ(obs))
        # if oldfeatures not in Q:
        #     Q[oldfeatures] = 0.0
        # # Q[oldfeatures] = Q[oldfeatures] + (1/N_a[oldfeatures]) * (Qsample - Q[oldfeatures])
        # Q[oldfeatures] = Q[oldfeatures] + 1.0/math.sqrt(N_a[oldfeatures])*(Qsample - Q[oldfeatures])
        # Q[oldfeatures] = Q[oldfeatures] + 1.0/((N_a[oldfeatures])**(1./3.))*(Qsample - Q[oldfeatures])
        # Q[oldfeatures] = Q[oldfeatures] + 1.0/(N_a[oldfeatures])*(Qsample - Q[oldfeatures])

		
		#picking action
        # return best_action(obs)
        # return self.actions[np.random.randint(0,len(self.actions))]
        # if state_excess():
        #     return best_action(obs)
        # onlyfeature = getfeatures(obs, K_w, 0)
        # if onlyfeature not in Statecount:
        #     Statecount[onlyfeature] = 1
        # else:
        #     Statecount[onlyfeature] += 1
        # print(onlyfeature)
        # if Statecount[onlyfeature] > kIterations:
        #     action = best_action(obs)
        #     return action


        # if :
        #     pass
        # if(Statecount[onlyfeature] < kIterations):
        #     if(random.randint(1,40) > math.sqrt(Statecount[onlyfeature])):
        #         return self.actions[np.random.randint(0,len(self.actions))]
        # # if(random.randint(1,50) > (Statecount[onlyfeature]**(1./3.))):
            # return self.actions[np.random.randint(0,len(self.actions))]

        # if(random.randint(1,40) > math.sqrt(Statecount[onlyfeature])):
        # count = 0
        # for action in p.getActionSet():
        #     current_feature = getfeatures(obs, action, 1)
        #     if current_feature not in N_a:
        #         N_a[current_feature] = 0
        #     count += N_a[current_feature]

        # if count > 500:
        #     action = best_action(obs)
        #     # print(action)
        #     return action
        

        # if(random.randint(1,100) < 10):
        
        # # if(random.randint(1,50) > (Statecount[onlyfeature]**(1./3.))):
        #     return self.actions[np.random.randint(0,len(self.actions))]
        # else:
        #     action = best_action(obs)
        #     # print(action)
        #     return action
        return best_action(obs)


# def state_excess():



def best_action(obs):
    action_final = None
    maxprofit = -np.inf
    for action in p.getActionSet():
        if maxprofit < getprofit(obs, action):
            # print(getprofit(obs, action))
            # print(maxprofit)
            action_final = action
            maxprofit = getprofit(obs, action)
    # print(maxprofit)
    # print(action_final)
    return action_final
	

	
        

        #return self.NOOP
        #Uncomment the following line to get random actions
        #return self.actions[np.random.randint(0,len(self.actions))]
# def maxQ(obs):
#     maxprofit = -np.inf
#     for action in p.getActionSet():
#         if maxprofit < getprofit(obs, action):
#             maxprofit = getprofit(obs, action)
#     return maxprofit
	
def getprofit(obs, action):
    features = getfeatures(obs, action,1)
    if features not in Q:
        Q[features] = 0
	
    return Q[features]
	
	
game = frogger_new.Frogger()
fps = 30
p = PLE(game, fps=fps,force_fps=False)
agent = NaiveAgent(p.getActionSet())
reward = 0.0
obs = game.getGameState()
action = None
#p.init()
# counter = 0


reward_current = 0
reward_total = 0
games = 0
while True:
    # print(N_a)
    # print(Q)
    # print(Statecount)
    # counter += 1
    # if counter %3000 == 0:
    #     counter = 1
    #     # write to the file
    #     write(Q, N_a, Statecount)


    if p.game_over():
        
        reward_total += reward_current
        print("This game reward: ", reward_current)
        reward_current = 0
        games +=1
        print("Average reward: ", reward_total/games)
        print("*****************************************")
        p.reset_game()


    old_obs = obs
    obs = game.getGameState()
    action = agent.pickAction(reward, obs, action, old_obs)
    reward = p.act(action)
    reward_current += reward











                            

    
