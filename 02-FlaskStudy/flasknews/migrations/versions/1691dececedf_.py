"""empty message

Revision ID: 1691dececedf
Revises: 97415fa80878
Create Date: 2022-12-18 11:58:33.893959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1691dececedf'
down_revision = '97415fa80878'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('desc', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'desc')
    # ### end Alembic commands ###
