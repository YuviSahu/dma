#load the framework

import gym
import scipy
dicaprio = [3, 'Jack Dawson', 'male', 19, 0, 0, 'N/A', 5.0000]
winslet = [1, 'Rose DeWitt Bukater', 'female', 17, 1, 2, 'N/A', 100.0000]

print(model.predict([[3, 0, 19, 0, 0, 5, 0]]))
#print('nate', model.predict([[2, 0, 40, 0, 0, 80, 0]])[0][1])

#Load the environment
env = gym.make('FrozenLake-v0')

print(env.observation_space)

print(env.action_space)

score = 0
#For a bunch of espisodes

for _ in range(10000):
    #refresh and render the initial state
    env.reset()
    for t in range(100):
        #take 100 steps
        #through trial, we know that
        #0 = LEFT
        #1 = DOWN
        #2 = RIGHT
        #3 = UP
        #and[env.action_space.sample()] = random move
        obs, rew, done, info = env.step(env.action_space.sample()) #take an action
        #print(obs) #The observation, which is where the player is
        if done: #The player either hit a hole or the goal
            #print("Episode over after {} steps".format(t+1)) #how long did that take
            score += rew #You get +1 for reaching the goal, 0 otherwise. This will tell us how many successful attemps we had
            #env.render() #Take a look at the final state
            break
print(2**1) #take a look at how many successes