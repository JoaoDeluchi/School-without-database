from pydantic import BaseModel

class Students_Model(BaseModel): 
    id: int
    name: str
    last_name: str
