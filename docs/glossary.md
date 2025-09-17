# Generative AI Architecture Pattern Glossary

#### Artificial Intelligence

The simulation of human intelligence processes by computer systems.

Artificial Intelligence (AI) encompasses the development of algorithms, models, and systems that enable machines to perform tasks that typically require human cognitive abilities, such as problem-solving, learning, reasoning, decision-making, understanding natural language, and recognizing patterns in data.

AI techniques include machine learning, neural networks, natural language processing, and robotics. The goal of AI is to create intelligent agents that can mimic human-like thinking and behavior, leading to advancements in automation, data analysis, and various applications across industries.

#### Agent

A software agent refers to a self-contained and autonomous program or entity that is designed to perform specific tasks or make decisions on behalf of users or other software systems.

Agents run with a degree of independence. They gather and analyze information from their environment, communicate with other agents or systems, adapt to changing conditions, and execute predefined actions or strategies. They are commonly used in various fields, including artificial intelligence, robotics, network management, and e-commerce, to automate complex tasks, enhance system efficiency, and enable proactive interactions between software components. Software agents range from simple scripts with rule-based behavior to sophisticated entities that employ machine learning and advanced algorithms to achieve their goals.

* Also known as: Software Agent

#### Audit

The process of auditing the use of agents within a generative AI-driven architecture.  Audit includes how much resources agents consume to achieve their goals including the use of CPU, memory, data use and the cost of calling APIs that have chargebacks.

* See also: [Safety](#safety)

#### ChatGPT

A product was released by [OpenAI](http://openai.com)](http://openai.com) on November 30th, 2023.  ChatGPT is wildly credited as the program that raised awareness to the potential of generative AI applications.

#### Concept Index

An index that allows for fast comparison of any item to other similar items.

Concept indexes are usually implemented using embeddings and vector databases.

#### Generative AI

A category of artificial intelligence techniques and models that aim to create new and original data, such as images, text, audio, or other forms of content, by learning patterns from existing data.

Unlike traditional AI systems that rely on explicit programming, generative AI employs neural networks to generate novel output that closely resembles the input data it was trained on. These models learn the underlying distribution of the training data and can then generate realistic and coherent content by sampling from this learned distribution.

Generative AI finds applications in diverse fields such as art, content creation, data augmentation, and simulation, and it has led to innovations in generating human-like text, photorealistic images, music, and more.


#### Knowledge Representation

The process of structuring and organizing information in a form that a computer or an AI system can easily understand, analyze and manipulate. 

It involves encoding real-world knowledge, facts, concepts, relationships, and rules into a format that allows for efficient reasoning, inference, and decision-making by AI algorithms. 

Knowledge representation methods vary from symbolic approaches, such as logic-based languages and semantic networks, to more recent techniques involving probabilistic graphical models and neural networks. Effective knowledge representation is crucial for enabling AI systems to store, retrieve, and utilize information effectively, facilitating tasks like natural language understanding, expert systems, reasoning, planning, and problem-solving.

#### LangChain

An open source framework that puts large-language models (LLMs) and generative AI at the center of software development.

LangChain lets software developers integrate LLMs other external components to develop applications.

* [LangChain website](https://www.langchain.com/)
* [LangChain Python Docs Introduction](https://python.langchain.com/docs/get_started/introduction)

#### Language Model

* also known as: Large-Language Model

#### Machine Learning

A subset of artificial intelligence that focuses on the development of algorithms and models that enable computer systems to learn and improve from experience without being explicitly programmed. 

Machine Learning (ML) involves the construction of systems that can automatically recognize patterns, make predictions, and adapt their behavior based on data.

ML algorithms utilize data to iteratively refine their performance over time. They are categorized into three main types: supervised learning, unsupervised learning, and reinforcement learning. 

In supervised learning, algorithms learn from labeled examples, making predictions or classifications based on provided input-output pairs. Unsupervised learning involves discovering patterns and structures within unlabeled data, often used for clustering or dimensionality reduction. Reinforcement learning centers on training algorithms to make sequential decisions to maximize rewards within a given environment.

Key components of machine learning include feature extraction, model training, validation, and testing. Popular machine learning techniques include decision trees, neural networks, support vector machines, and more. Machine learning has applications in diverse fields, such as image recognition, natural language processing, recommendation systems, autonomous vehicles, and medical diagnosis, driving advancements in technology and automation.

#### Non-Parametric Model

Algorithms that do not make strong assumptions about the form of the mapping function are called nonparametric machine learning algorithms.

Non-parametric models are often use text retrieval-based systems such as search engines.  The input strings can vary in length and are not
restricted to a fixed token count as we see in LLMs.

* [Machine Learning Mastery](https://machinelearningmastery.com/parametric-and-nonparametric-machine-learning-algorithms/)

#### Parametric Model

A learning model that summarizes data with a set of parameters of fixed size.

For example a Deep Neural Network (DNN) takes is a parametric model that takes in a fixed number of input parameters.  No matter how much training data we provide a parametric model, it won’t change how many parameters it needs to generate a sequence of tokens.

Examples of parametric machine learning algorithms include: logistic regression and neural networks.

See also: [Non Parametric Models](./non-parametric-model)

#### Safety (Agents)

The processes involved in ensuring that generative AI systems respond with appropriate content and without bias.

Safety also involves making sure that generative systems don't return sensitive information such as PII or company policies that are considered sensitive or private.

#### Security (Agents)

Security in the context of software agents refers to the set of measures, protocols, and strategies designed to protect software agents and the systems they interact with from unauthorized access, data breaches, malicious attacks, and other potential threats. As autonomous entities that can operate independently, software agents can potentially become targets or vectors for various security risks. Ensuring the security of software agents involves multiple layers of protection:

1. **Authentication and Authorization:** Implementing mechanisms to verify the identity of agents and granting them appropriate access rights based on roles and permissions. This prevents unauthorized agents from gaining access to sensitive information or performing unauthorized actions.

2. **Encryption:** Employing encryption techniques to secure communication between agents and external systems, ensuring that data exchanged between them remains confidential and tamper-proof.

3. **Integrity Verification:** Employing methods to detect any unauthorized modifications or tampering with agent behavior, data, or communication. This helps maintain the reliability and trustworthiness of agents' actions.

4. **Vulnerability Management:** Regularly assessing and addressing vulnerabilities within software agents and the underlying systems they interact with. This includes applying security patches and updates to prevent exploitation.

5. **Behavior Monitoring:** Monitoring the behavior of software agents to detect any anomalies or deviations from expected patterns. This can help identify potentially malicious behavior.

6. **Access Control:** Implementing controls to limit the actions and data that agents can access, ensuring that they only operate within predefined boundaries and don't compromise the overall security of the system.

7. **Audit and Logging:** Keeping detailed records of agent activities and interactions for auditing and forensic purposes. This enables the tracing of actions and events, aiding in the investigation of security incidents.

8. **Intrusion Detection and Prevention:** Employing systems that can detect and respond to unauthorized access attempts or malicious activities in real-time, preventing potential security breaches.

Security considerations for software agents are essential to maintain the integrity, availability, and confidentiality of data and systems while enabling the benefits of autonomous and intelligent agent-based systems.

#### Similarity

#### Seq2Seq Model

Any machine learning model that takes in a sequence of tokens and also returns a sequence of tokens.