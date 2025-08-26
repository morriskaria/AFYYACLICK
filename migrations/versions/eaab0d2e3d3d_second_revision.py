"""second  revision

Revision ID: eaab0d2e3d3d
Revises: 8c2a1a7b2582
Create Date: 2025-08-26 12:25:04.521810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaab0d2e3d3d'
down_revision: Union[str, Sequence[str], None] = '8c2a1a7b2582'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
