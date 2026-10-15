# Bibliotecas
from typing import List, Optional
from pydantic import BaseModel, Field

class PredictionImput(BaseModel):
    tamanho_m2: float = Field(..., gt=10, lt=2000, description="Área útil do imóvel em metros quadrados")
    idade_imovel: int = Field(default=None, ge=0, le=10, description="Idade de construção em anos")
    num_banheiros: int = Field(default=1, ge=1, le=5, description="Número de banheiros do imóvel")
    proximidade_metro: float = Field(..., ge=0, le=200, description="Distância até o centroo urbano em km")

class BatchPredictionImput(BaseModel):
    inputs: List[PredictionImput]

class SinglePredictionOutput(BaseModel):
    predict: float = Field(..., description="valor estimado do aluguel em Reais")

class BatchPredictionOutput(BaseModel):
    predictions: List[SinglePredictionOutput]