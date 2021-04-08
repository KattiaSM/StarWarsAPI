"""empty message

Revision ID: cbca8c8bbcb0
Revises: e347ebf83615
Create Date: 2021-04-08 17:17:43.834347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbca8c8bbcb0'
down_revision = 'e347ebf83615'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_people', sa.Integer(), nullable=True),
    sa.Column('id_planets', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_people'], ['people.id'], ),
    sa.ForeignKeyConstraint(['id_planets'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favoritos')
    # ### end Alembic commands ###