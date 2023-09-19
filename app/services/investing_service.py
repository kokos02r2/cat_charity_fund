from datetime import datetime

from app.crud.donation import donation_crud
from sqlalchemy.ext.asyncio import AsyncSession


async def invest_in_projects(session: AsyncSession, object):
    while True:
        project, donation = await donation_crud.get_open_object(session)
        if not project or not donation:
            await session.commit()
            await session.refresh(object)
            return object

        balance_project = project.full_amount - project.invested_amount
        balance_donation = donation.full_amount - donation.invested_amount

        if balance_project > balance_donation:
            project.invested_amount += balance_donation
            donation.invested_amount += balance_donation
            donation.fully_invested = True
            donation.close_date = datetime.utcnow()
        elif balance_project <= balance_donation:  # Объединяем два условия
            project.invested_amount += min(balance_project, balance_donation)
            donation.invested_amount += min(balance_project, balance_donation)
            project.fully_invested = True
            project.close_date = datetime.utcnow()
            if balance_project == balance_donation:
                donation.fully_invested = True
                donation.close_date = datetime.utcnow()

        session.add(project)
        session.add(donation)
        await session.commit()
        await session.refresh(project)
        await session.refresh(donation)
