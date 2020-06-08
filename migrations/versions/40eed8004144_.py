"""empty message

Revision ID: 40eed8004144
Revises: 70c5d049dfc0
Create Date: 2020-05-27 14:41:14.681188

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '40eed8004144'
down_revision = '70c5d049dfc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('G:Bot Data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('G:Bot Data',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('number', mysql.VARCHAR(length=4096), nullable=True),
    sa.Column('user_input', mysql.VARCHAR(length=4096), nullable=True),
    sa.Column('date', mysql.VARCHAR(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###