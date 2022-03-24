import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.verbose(False)
kernel.setBotPredicate("name", "Jhonny")

up_stream = open("knowledge_base.log","w+")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
    

print("\n Hello user!!, my name is Jhonny.\n\n I am chatbot designed to reply back to queries of users \n Having speciality and inclination towards the queries related to BITS Pilani, Hyderabad Campus :)")

print("\n Please feel free to ask any queries. \n I am flexible bot. \n Even if I don't give you satisfactory reply you can always ask me to google stuff and I will do so")
print("\n I can give you\n ->weather report \n ->provide google images for your query \n ->suggest delicious and different eateries at BPHC as per your choice")
print("\n What are you waiting for?\n\n Let's get started dude!!")

while True:
    message = raw_input("Enter your message to your Bot, Jhonny:").lower()
    if message == "quit":
      kernel.saveBrain("bot_brain.brn") 
      exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print(bot_response)
        up_stream.write("User: " + message + "\n")
        up_stream.write("Bot: "+bot_response+"\n")
