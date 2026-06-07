"""add content column to posts table

Revision ID: 3f8a8dba7137
Revises: 76e4dd07a3ff
Create Date: 2026-05-29 01:56:42.290335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f8a8dba7137'
down_revision: Union[str, Sequence[str], None] = '76e4dd07a3ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
