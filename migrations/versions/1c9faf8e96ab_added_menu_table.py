"""added menu table

Revision ID: 1c9faf8e96ab
Revises: 464cde6b804e
Create Date: 2019-05-03 16:21:54.549731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9faf8e96ab'
down_revision = '464cde6b804e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('menu_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('menu_name', sa.String(length=30), nullable=False),
    sa.Column('menu_type', sa.String(length=30), nullable=False),
    sa.Column('bio', sa.String(length=200), nullable=False),
    sa.Column('locations', sa.String(length=200), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['owner.owner_id'], ),
    sa.PrimaryKeyConstraint('menu_id'),
    sa.UniqueConstraint('menu_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu')
    # ### end Alembic commands ###
