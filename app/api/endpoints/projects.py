# app/api/meeting_room.py
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import charity_project_crud
from app.schemas.projects import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate
)
from app.api.validators import (
    check_name_duplicate,
    check_project_exists,
    check_project_invested_amount,
    check_new_full_amount,
    check_closed_project

)
from app.services.investing_service import invest_in_projects
from app.core.user import current_superuser

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_project(
        project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    await check_name_duplicate(project.name, session)
    new_project = await charity_project_crud.create(project, session)
    await invest_in_projects(session, new_project)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_project(
        project_id: int,
        project_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    project = await check_project_exists(
        project_id, session
    )
    if project_in.name is not None:
        await check_name_duplicate(project_in.name, session)
    await check_closed_project(project_id, session)
    await check_new_full_amount(project, project_in.full_amount)
    project = await charity_project_crud.update(
        project, project_in, session
    )
    return project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    project = await check_project_exists(project_id, session)
    project = await check_project_invested_amount(project_id, session)
    project = await charity_project_crud.remove(project, session)
    return project
