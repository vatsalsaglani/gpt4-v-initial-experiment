from typing import List, Dict, Optional, Union
from pydantic import BaseModel


class QARequest(BaseModel):
    messages: List[Dict]
    voice: Optional[str] = "alloy"
    language: Optional[str] = "english"
