from typing import Literal, Annotated

from jsonargparse.typing import Path_dc
from pydantic import BaseModel, ConfigDict, Field


class Model(BaseModel):
    model_config = ConfigDict(extra='ignore', arbitrary_types_allowed=True)
    name: Annotated[str, Field(description='Name of the model')]
    device: Annotated[Literal['cpu', 'cuda'], Field(description='Device for the model')] = 'cpu'
    save_path: Annotated[Path_dc, Field(description='Path to save the model')]
    hidden_size: Annotated[int, Field(description='Input size for hidden layer')] = 768
    epochs: Annotated[int, Field(description='Training epochs')] = 3
    infer: Annotated[bool, Field(description='Whether to run inference')] = False
