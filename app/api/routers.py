from fastapi import APIRouter

from app.api.endpoints import user_router, projects_router, donations


main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(
    projects_router, prefix='/charity_project', tags=['charity projects']
)
main_router.include_router(
    donations, prefix='/donation', tags=['donations']
)