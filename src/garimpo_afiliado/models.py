from typing import List
from pydantic import BaseModel, Field




class Produto(BaseModel):
    
    nome: str = Field(description="Nome do produto como aparece na loja")
    plataforma: str = Field(description="Onde foi encontrado: shopee, amazon ou mercado livre")
    faixa_preco: str = Field(description="Faixa de preço aproximada em reais, ex: R$ 30 a R$ 50")
    por_que_esta_em_alta: str = Field(description="Motivo da alta procura, em 1 frase")


class ListaProdutos(BaseModel):
    
    produtos: List[Produto] = Field(description="Lista de produtos em alta encontrados")




class ProdutoAvaliado(BaseModel):
    
    nome: str = Field(description="Nome do produto escolhido")
    nota: float = Field(
        ge=0, le=10,
        description="Nota de 0 a 10 seguindo os critérios definidos",
    )
    justificativa: str = Field(description="Por que este produto entrou no top 3")


class Top3(BaseModel):
    
    top3: List[ProdutoAvaliado] = Field(
        min_length=3, max_length=3,  
        description="Exatamente 3 produtos, do melhor para o pior",
    )




class Estrategia(BaseModel):
    
    produto: str = Field(description="Nome do produto que será divulgado")
    titulo_para_leads: str = Field(description="Título chamativo para atrair interessados")
    descricao_video_ou_imagem: str = Field(
        description="Descrição do vídeo ou da imagem a ser criada, com o que mostrar",
    )
    hashtags: List[str] = Field(
        description="Hashtags para alcançar engajamento, cada uma começando com #",
    )


class EstrategiasRede(BaseModel):
    rede_social: str = Field(description="Nome da rede: tiktok, pinterest ou instagram")
    estrategias: List[Estrategia] = Field(
        description="2 estratégias para CADA produto do top 3 (6 no total)",
    )