"""create appointments table

Revision ID: 175c06f8a68c
Revises: 65a06b47f35d
Create Date: 2023-08-17 13:19:06.270551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '175c06f8a68c'
down_revision: Union[str, None] = '65a06b47f35d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('barber_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('booked', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['barber_id'], ['barbers.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    # ### end Alembic commands ###