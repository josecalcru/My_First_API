"""empty message

Revision ID: 8250cf8d57fc
Revises: 762402052503
Create Date: 2021-03-30 01:16:10.784127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8250cf8d57fc'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    # ### end Alembic commands ###
