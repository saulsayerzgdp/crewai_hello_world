from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool  # Import Serper tool

@CrewBase
class HelloWorld():
    agents: list
    tasks: list

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],
            verbose=True,
            llm='gpt-4.1'
        )

    @agent
    def web_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['web_search_agent'],
            tools=[SerperDevTool()],  # Attach the Serper tool
            verbose=True,
            llm='gpt-4.1'
        )

    @agent
    def information_compiler_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['information_compiler_agent'],
            verbose=True,
            llm='gpt-4.1'
        )

    @task
    def web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_search_task']
        )

    @task
    def information_compiler_task(self) -> Task:
        return Task(
            config=self.tasks_config['information_compiler_task']
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )