"""added restaurant reservation foreign key

Revision ID: 6a97a0a558ed
Revises: b52b02cb558b
Create Date: 2019-04-16 19:26:49.100200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a97a0a558ed'
down_revision = 'b52b02cb558b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('restaurant_reservation', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reservation', 'restaurant', ['restaurant_reservation'], ['restaurant_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reservation', type_='foreignkey')
    op.drop_column('reservation', 'restaurant_reservation')
    # ### end Alembic commands ###