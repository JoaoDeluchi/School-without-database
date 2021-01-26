from fastapi import FastAPI
from App.students_views import router as student_routers
from App.tests_views import router as answers_sheet_routers

def create_app():
    app = FastAPI()
    app.include_router(student_routers, prefix="/students", tags=["Students Management"])
    app.include_router(answers_sheet_routers, prefix="/answers", tags=["Tests Management"])
    return app
