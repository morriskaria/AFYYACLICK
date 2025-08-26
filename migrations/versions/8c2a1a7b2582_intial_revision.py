"""intial revision

Revision ID: 8c2a1a7b2582
Revises: 
Create Date: 2025-08-26 12:24:21.027488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c2a1a7b2582'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    #this will contain all the changfes you want to make 
    pass


def downgrade() -> None:
    """Downgrade schema."""
    #this will contain the changes you want to undo when the migration is rolled back 
    pass
