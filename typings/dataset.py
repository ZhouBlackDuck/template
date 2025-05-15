from typing import Annotated, Literal

from jsonargparse.typing import Path_drw, Path_dc
from pydantic import BaseModel, ConfigDict, Field


class Dataset(BaseModel):
    model_config = ConfigDict(extra='ignore', arbitrary_types_allowed=True)
    name: Annotated[str, Field(description='Name of the dataset')]
    batch_size: Annotated[int, Field(description='Batch size of the dataset')] = 32
    split_ratio: Annotated[float, Field(gt=0.0, lt=1.0, description='Split ratio of train/validate dataset')] = 0.8
    shuffle: Annotated[bool, Field(description='Shuffle the dataset or not')] = True
    device: Annotated[Literal['cpu', 'cuda'], Field(description='Device for the dataset')] = 'cpu'
    raw_path: Annotated[Path_drw, Field(description='Path to the raw dataset')]
    processed_path: Annotated[Path_dc, Field(description='Path to the processed dataset')]
