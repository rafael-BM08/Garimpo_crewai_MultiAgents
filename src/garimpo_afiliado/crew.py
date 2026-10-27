from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from garimpo_afiliado.models import ListaProdutos, Top3, EstrategiasRede
from crewai_tools import TavilySearchTool


@CrewBase
class GarimpoAfiliado():

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def pesquisar_produtos(self) -> Agent:

        buscar_web = TavilySearchTool(
            search_depth="basic",     
            max_results=8,            
            time_range="month",       
        )

        return Agent(
            config=self.agents_config['pesquisar_produtos'], 
            tools=[buscar_web],
            verbose=True
        )

    @agent
    def avaliador_produtos(self) -> Agent:
        return Agent(
            config=self.agents_config['avaliador_produtos'], 
            verbose=True
        )

    @agent
    def marketing_digital(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_digital'], 
            verbose=True
        )

    @task
    def tarefa_pesquisa(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_pesquisa'], 
            output_pydantic=ListaProdutos,
        )

    @task
    def tarefa_avaliacao(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_avaliacao'],
            output_pydantic=Top3, 
        )

    @task
    def tarefa_tiktok(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_tiktok'],
            output_pydantic=EstrategiasRede,
        )

    @task
    def tarefa_pinterest(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_pinterest'], 
            output_pydantic=EstrategiasRede,
        )

    @task
    def tarefa_instagram(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_instagram'], 
            output_pydantic=EstrategiasRede,
        )

    @crew
    def crew(self) -> Crew:
        
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
