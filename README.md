# Personal Financial Chatbot 🤖🤖

## Requirements
-> We are required to build a personal financial management chatbot using OpenAI's language model. The chatbot should have the following features:
- The chatbot should provide a conversational interface where users can interact with the chatbot to ask questions about their finances, get insights from their transaction history, or receive personalized financial advice. The chatbot should be able to handle different types of user queries, such as factual, analytical, or advisory.
- The chatbot should use OpenAI's language model to generate natural and coherent responses to user queries. The language model is a neural network that can generate text based on a given input or context. You should use the OpenAI Playground to access and fine-tune the language model. You should also provide some examples of the language model's input and output.
- The chatbot should use a user's transactions as the source of data for providing financial insights and advice. The transactions should include information such as date, amount, category, and description. The chatbot should be able to analyze the transactions and extract useful information, such as spending patterns, income sources, savings goals, etc.
- The chatbot should be able to provide personalized financial advice based on the user's transactions and goals. The chatbot should be able to understand the user's context and preferences, and provide relevant and actionable suggestions. The chatbot should also be able to explain the rationale behind its advice and provide evidence or examples to support it.

## Implementation (Data creation)
- As we have in form of Json structure or can be converted into CSV format i.e. 

```javascript
[ { “date”: “2021-01-01”, “amount”: 1000, “category”: “income”, “description”: “salary” }, { “date”: “2021-01-02”, “amount”: -50, “category”: “groceries”, “description”: “milk and eggs” }, { “date”: “2021-01-03”, “amount”: -100, “category”: “entertainment”, “description”: “movie tickets” }, { “date”: “2021-01-04”, “amount”: -20, “category”: “transportation”, “description”: “bus fare” }, { “date”: “2021-01-05”, “amount”: -200, “category”: “bills”, “description”: “electricity bill” }, { “date”: “2021-01-06”, “amount”: -30, “category”: “groceries”, “description”: “bread and cheese” }, { “date”: “2021-01-07”, “amount”: -150, “category”: “clothing”, “description”: “new shoes” }, { “date”: “2021-01-08”, “amount”: -40, “category”: “healthcare”, “description”: “prescription drugs” }, { “date”: “2021-01-09”, “amount”: -80, “category”: “education”, “description”: “online course” }, { “date”: “2021-01-10”, “amount”: -60, “category”: “entertainment”, “description”: “pizza delivery” }, {“date”: “2021-01-11”, “amount”: -25, “category”: “transportation”, “description”: “taxi ride” }, { “date”: “2021-01-12”, “amount”: -300, “category”:“bills”, “description”:“internet bill” }, { “date”:“2021-01-13”, “amount”:-50, “category”:“groceries”, “description”:“fruits and vegetables” } ]
```

Therefore first, I've converted it into csv dataframe format with columns :
1. **Date -** Date of transaction.
2. **Amount -** How much sales or amount is involved in transaction.
3. **Results -** Overall we got profit or loss. If amount is positive, we'll take it as a profit else loss.
4. **Category -** In which category, transaction occurs.
5. **Description -** What is bought or sold in that category.

![Data creation](https://github.com/Hg03/kniru_take_home/blob/main/images/Snap1.png)

## Implementation (Creating chatbot)
- [Langchain](https://python.langchain.com/en/latest/index.html) is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model. Here I've used conversation chain of langchain which helps to build a conversation bot using custom csv data. 
- [Chains](https://python.langchain.com/en/latest/modules/chains.html) - Using an LLM in isolation is fine for some simple applications, but many more complex ones require chaining LLMs - either with each other or with other experts. LangChain provides a standard interface for Chains, as well as some common implementations of chains for ease of use.)

**Steps -**
- First I've loaded the csv data and creates its index data.
- Then pass it to our conversation retrieval chain of langchain.
- We'll query it.

![bot](https://github.com/Hg03/kniru_take_home/blob/main/images/Snap2.png)

## Implementation (Interface)
- I've used streamlit to create a beautiful interface where user can enter their OPENAI API key and upload their data.
- Then they can communicate and query , according to the data.

