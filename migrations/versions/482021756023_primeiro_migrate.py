"""primeiro migrate

Revision ID: 482021756023
Revises: 
Create Date: 2025-03-04 22:17:40.443056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '482021756023'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('datanascimento', sa.DateTime(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('responde', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato')
    # ### end Alembic commands ###
