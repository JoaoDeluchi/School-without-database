from fastapi import APIRouter
from App.data import list_of_approved_students
from App.models import Students_Model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Students_Model])
async def get_approved_students():
    """
    View that returns a list with approved students
    """
    return list_of_approved_students