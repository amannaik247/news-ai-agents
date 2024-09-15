from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
#call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature =0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")
                             )

# Creating a senior researcher agent with memory and verbose mode

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
    
)

## Creating a writer agent with custom tools responsible in writing new blog

news_analyzer = Agent(
    role="Writer",
    goal="Craft compelling content on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for analyzing complex topics, you craft"
        "a score between -10 to +10, with -10 being negative net impact"
        "and +10 being positive impact."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False

)
