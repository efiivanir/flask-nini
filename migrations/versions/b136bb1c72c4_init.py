"""Init

Revision ID: b136bb1c72c4
Revises: 
Create Date: 2022-01-18 21:35:38.129152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b136bb1c72c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patients_status_status'), 'patients_status', ['status'], unique=True)
    op.create_table('therapist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=16), nullable=False),
    sa.Column('last_name', sa.String(length=32), nullable=False),
    sa.Column('tz_id', sa.String(length=9), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address_city', sa.String(length=64), nullable=True),
    sa.Column('address_street', sa.String(length=64), nullable=True),
    sa.Column('address_house_num', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_therapist_email'), 'therapist', ['email'], unique=False)
    op.create_index(op.f('ix_therapist_tz_id'), 'therapist', ['tz_id'], unique=False)
    op.create_index(op.f('ix_therapist_username'), 'therapist', ['username'], unique=True)
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_first_name', sa.String(length=64), nullable=False),
    sa.Column('main_last_name', sa.String(length=64), nullable=False),
    sa.Column('main_birth_year', sa.Integer(), nullable=True),
    sa.Column('main_phone', sa.String(length=15), nullable=True),
    sa.Column('main_is_dutch', sa.Boolean(), nullable=True),
    sa.Column('main_status_id', sa.Integer(), nullable=True),
    sa.Column('second_first_name', sa.String(length=64), nullable=True),
    sa.Column('second_last_name', sa.String(length=64), nullable=True),
    sa.Column('second_birth_year', sa.Integer(), nullable=True),
    sa.Column('second_phone', sa.String(length=15), nullable=True),
    sa.Column('second_is_dutch', sa.Boolean(), nullable=True),
    sa.Column('second_status_id', sa.Integer(), nullable=True),
    sa.Column('address_city', sa.String(length=64), nullable=False),
    sa.Column('address_street', sa.String(length=64), nullable=False),
    sa.Column('address_house_num', sa.String(length=64), nullable=False),
    sa.Column('therapist_id', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['main_status_id'], ['patients_status.id'], ),
    sa.ForeignKeyConstraint(['second_status_id'], ['patients_status.id'], ),
    sa.ForeignKeyConstraint(['therapist_id'], ['therapist.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('main_first_name', 'main_last_name', 'address_city', 'address_street', 'address_house_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('house')
    op.drop_index(op.f('ix_therapist_username'), table_name='therapist')
    op.drop_index(op.f('ix_therapist_tz_id'), table_name='therapist')
    op.drop_index(op.f('ix_therapist_email'), table_name='therapist')
    op.drop_table('therapist')
    op.drop_index(op.f('ix_patients_status_status'), table_name='patients_status')
    op.drop_table('patients_status')
    # ### end Alembic commands ###
