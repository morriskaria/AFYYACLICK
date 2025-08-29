"""create users and posts tables

Revision ID: 25d3ea1e5ce4
Revises: eaab0d2e3d3d
Create Date: 2025-08-29 10:21:22.455570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25d3ea1e5ce4'
down_revision: Union[str, Sequence[str], None] = 'eaab0d2e3d3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
