#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class JioMartChatbot:
    def __init__(self):
        self.name="Jio Mart Chatbot"
        
    def get_response(self, user_query):
        if "product" in user_query:
            return"We have wide range of products. What specific you are looking for?"
        elif"offers" in user_query:
            return"We have different offers on differnt products. Please visit our website for more details"
        elif"delivery" in user_query:
            return"We offer fast delivery services"
        elif"payment" in user_query:
            return"we accept multiple payment option including netbanking ,UPI and Cash on delivery"
        elif"contact" in user_query:
            
            return"You can contact our consumer care at 1800-xxx-xxxx"
        else:
            return"I am sorry ,I couldn't understand your query.How can i help you?"

chatbot=JioMartChatbot()
print(f"Welcome to {chatbot.name}! How can I help you today?")
while True:
      user_input=input("User: ")
      if user_input.lower()=="exit":
          print("thank you for using our chatbot. Have a great day!")
          break
      response= chatbot.get_response(user_input.lower())
      print(f"{chatbot.name}: {response}")


# In[ ]:




