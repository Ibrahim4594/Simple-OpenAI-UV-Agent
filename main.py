import os
from dataclasses import dataclass
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

french_agent = Agent(
    name="FrenchAssistant",
    instructions="Translate the input to French.",
    handoff_description="If unable to translate, refer to the Russian translation."
)

russian_agent = Agent(
    name="RussianAssistant",
    instructions="Translate the input to Russian.",
    handoff_description="If unable to translate, refer to the French translation."
)

dutch_agent = Agent(
    name="DutchAssistant",
    instructions="Translate the input to Dutch.",
    handoff_description="If unable to translate, refer to the German translation."
)

german_agent = Agent(
    name="GermanAssistant",
    instructions="Translate the input to German.",
    handoff_description="If unable to translate, refer to the French translation."
)

main_agent = Agent(
    name="MainAssistant",
    instructions="Translate the input to Dutch. If unable, hand off to German, then French or Russian as needed.",
    handoffs=[dutch_agent, german_agent, french_agent, russian_agent]
)

# Run the main agent and print the result
result = Runner.run_sync(main_agent, "Hello I am Ibrahim in German", run_config=config)
print("Main agent translation:", result.final_output)

