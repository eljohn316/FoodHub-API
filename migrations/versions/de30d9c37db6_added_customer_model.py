"""Added customer model

Revision ID: de30d9c37db6
Revises: 1126fd3580ae
Create Date: 2019-04-02 12:40:51.676000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de30d9c37db6'
down_revision = '1126fd3580ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('customer',
    sa.Column('customer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('contact_number', sa.String(length=11), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('password_hash', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('customer_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('owner',
    sa.Column('owner_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('contact_number', sa.String(length=11), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('password_hash', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('owner_id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    op.drop_table('customer')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###