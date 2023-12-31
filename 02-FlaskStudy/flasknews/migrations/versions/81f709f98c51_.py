"""empty message

Revision ID: 81f709f98c51
Revises: 7731b5539706
Create Date: 2022-12-17 18:16:33.959828

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '81f709f98c51'
down_revision = '7731b5539706'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('type_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('base_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_model',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('date_time', mysql.DATETIME(), nullable=True),
    sa.Column('type_name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('news_type')
    # ### end Alembic commands ###
