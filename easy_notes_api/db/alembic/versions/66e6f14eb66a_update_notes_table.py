"""Update notes table

Revision ID: 66e6f14eb66a
Revises: 7a1ba5ef935b
Create Date: 2024-07-19 18:23:43.877328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '66e6f14eb66a'
down_revision: Union[str, None] = '7a1ba5ef935b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('note', sa.Column('tag', sa.TEXT(), nullable=True))
    op.create_unique_constraint(op.f('uq__note__id'), 'note', ['id'])
    op.create_unique_constraint(op.f('uq__user__id'), 'user', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__user__id'), 'user', type_='unique')
    op.drop_constraint(op.f('uq__note__id'), 'note', type_='unique')
    op.drop_column('note', 'tag')
    op.drop_column('note', 'date_created')
    # ### end Alembic commands ###
