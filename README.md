# ChatBot-Jhonny

The aim of the Chat-Bot Project was to make a bot based on keyword-matching and intent-recognition.  The Bot had to store the conversations in a knowledgebase using a flat file. It would interact with web services and help user with multiple tasks like weather reports, perform searches on web and recommend eateries within campus. 

The core of the bot was made using AIML. The AIML campus specific files query was added along. It was based on the principles of the Alice-bot. Integration of the services in the AIML was done by invoking scripts whenever similar query was asked by user using regular-expression matching.

The bot is invoked through CLI and a snip of it's conversation with the user can be seen below-

![image](https://user-images.githubusercontent.com/71601478/197355081-86637ac7-210d-457b-87a8-22de6fb5f0b9.png)

Following libraries were used while making the chatbot-


1. aiml- Interpreter for using Artificial Intelligence Markup Language files.
2. Selenium- To automate web browser interaction.
3. Pillow- To display the image of several food outlets menu.
