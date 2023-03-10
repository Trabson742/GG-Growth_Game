"""empty message

Revision ID: 369d7c78a8ea
Revises: 8c86967d4928
Create Date: 2023-02-09 10:24:11.346216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '369d7c78a8ea'
down_revision = '8c86967d4928'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('desafios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=120), nullable=True),
    sa.Column('moedas', sa.String(length=120), nullable=True),
    sa.Column('data_inicio', sa.Date(), nullable=True),
    sa.Column('data_final', sa.Date(), nullable=True),
    sa.Column('grupo', sa.String(length=120), nullable=True),
    sa.Column('categoria', sa.String(length=120), nullable=True),
    sa.Column('situacao', sa.String(length=120), nullable=True),
    sa.Column('banner', sa.String(length=120), nullable=True),
    sa.Column('card', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=True),
    sa.Column('valor', sa.String(length=120), nullable=True),
    sa.Column('marca', sa.String(length=120), nullable=True),
    sa.Column('modelo', sa.String(length=120), nullable=True),
    sa.Column('categoria', sa.String(length=120), nullable=True),
    sa.Column('ano', sa.String(length=120), nullable=True),
    sa.Column('quantidade_estoque', sa.String(length=120), nullable=True),
    sa.Column('descricao', sa.TEXT(), nullable=True),
    sa.Column('imagem', sa.String(length=120), nullable=True),
    sa.Column('ativo', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtos')
    op.drop_table('desafios')
    # ### end Alembic commands ###
