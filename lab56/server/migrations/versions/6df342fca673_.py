"""empty message

Revision ID: 6df342fca673
Revises: 
Create Date: 2020-12-12 01:27:35.112869

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6df342fca673'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.Column('first_name', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.Column('last_name', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.Column('phone_number', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_login'), 'user', ['login'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_login'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
