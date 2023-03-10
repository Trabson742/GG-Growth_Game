"""empty message

Revision ID: d2004d3b7cc1
Revises: 369d7c78a8ea
Create Date: 2023-02-09 13:08:05.258430

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2004d3b7cc1'
down_revision = '369d7c78a8ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produtos', sa.Column('preco', sa.String(length=120), nullable=True))
    op.add_column('produtos', sa.Column('preco_desconto', sa.String(length=120), nullable=True))
    op.drop_column('produtos', 'valor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produtos', sa.Column('valor', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('produtos', 'preco_desconto')
    op.drop_column('produtos', 'preco')
    # ### end Alembic commands ###
