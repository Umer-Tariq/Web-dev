"""empty message

Revision ID: 846a17e030c0
Revises: 
Create Date: 2024-12-11 21:01:32.609255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846a17e030c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Friend',
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('img_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('fid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Friend')
    # ### end Alembic commands ###
