
from agent import Agent
from config import templates
from environment import Environment
# from scenario import Scenario

print("Welcome to the Home building Simulator")
print("While I am sure you are excited to get started, I need to know some things?")
user_name = input("What would you like to be called? ")
print("Welcome to the crew", user_name)

print('There are 3 different levels, which one would you like. ("please enter the number")')
print("1.Rookie, 2.Skilled Worker, 3.Forman")


try:
    user_template = int(input("Enter 1,2,3 " ))
except ValueError:
    user_template=1

if user_template == 1:
    print("Welcome to the Rookie level, it will be hard mentaly and physically but here we go... ")
elif user_template==2:
    print("Welcome to the Skilled Worker level, Thankfully you alreay know what you are getting into... ")
elif user_template==3:
    print("Welcome to the Forman level, I know you are sore and tired but it's time to teach. ")
else:
    print("It looks like you did not understand the question, so you must me a Rookie")
    user_template=1
     

print("Now I need to know how you spend you night after work. 1. getting lots of sleep, 2. being a night owl, 3. drinking ?")



try:
    night_life=int(input("Enter 1,2,3 "))
except ValueError:
    night_life=1


if night_life ==1:
    print("It really is good to get sleep, but not a lot of fun. ")
elif night_life ==2:
    print("Yeah staying up late is fun, but is it worth it?")
elif night_life ==3:
    print("Why does this seem to be so popular, it hurts tomorrow. ")
else: 
    print("It looks like you did not understand the question, so you must drink a lot!")
    night_life=3

agent = Agent(user_name, user_template, night_life)
env = Environment()


while env.time_remaining > 0:

    available = env.get_available_actions(agent)

    print("\nAVAILABLE ACTIONS:", available)

    
    if not available:
        print("\nNo actions available — crew is exhausted or time ran out.")
        break
    
    print("\nChoose an action:")

    for i, action in enumerate(available, start=1):
        print(f"{i}. {action}")

    try:
        choice = int(input("Enter number: "))
        chosen = available[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice — losing time due to confusion.")
        env.time_remaining -= 1
        continue


    print("Executing:", chosen)

    env.execute_action(agent, chosen)


    agent.print_stats()
    print(env.progress)
    print("\n".join(env.history))
