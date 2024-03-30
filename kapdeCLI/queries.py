from sqlite3 import Connection, Cursor
from typing import Type

from tables import Table, Column, TABLES, User


# What the create_table query generates
# query = f"""
#         CREATE TABLE IF NOT EXISTS {User} (
#             {User.user_id}      {User.user_id.dtype}        {User.user_id.constraints},
#             {User.user_name}    {User.user_name.dtype}      {User.user_name.constraints},
#             {User.is_customer}  {User.is_customer.dtype}    {User.is_customer.constraints},
#             {User.password}     {User.password.dtype}       {User.password.constraints},
#             {User.house_num}    {User.house_num.dtype}      {User.house_num.constraints},
#             {User.locality}     {User.locality.dtype}       {User.locality.constraints},
#             {User.city}         {User.city.dtype}           {User.city.constraints},
#             {User.state}        {User.state.dtype}          {User.state.constraints},
#             {User.pin_code}     {User.pin_code.dtype}       {User.pin_code.constraints},
#             {User.gender}       {User.gender.dtype}         {User.gender.constraints},
#         );
#     """


def initialize_metadata_for_table(cls: Type[Table]):
    for name in dir(cls):
        attribute = getattr(cls, name)
        if isinstance(attribute, Column):
            if attribute.name == "":
                attribute.name = name

            attribute.full = f"{cls.__name__}.{attribute}"


def initialize_metadata_for_all_tables():
    for table_class in TABLES:
        initialize_metadata_for_table(table_class)


def insert_tuple(con: Connection, params: str, table: str) -> Cursor:
    query = f"INSERT INTO {table}"
    query += f" ({User.user_name}, {User.house_num}, {User.locality}, {User.city}, {User.state}, {User.pin_code}, {User.country}, {User.gender}) "
    query += f"VALUES {params};"
    print(query)
    return con.execute(query)


def create_table(con: Connection, table: Type[Table]) -> Cursor:
    query = f"CREATE TABLE IF NOT EXISTS {table} (\n\t"
    query += ",\n\t".join(f"{col} {col.dtype} {col.constraints}" for col in table.columns())
    query += "\n);"
    print(query)  # TODO Remove
    return con.execute(query)


def create_tables(con: Connection):
    for table in TABLES:
        create_table(con, table)
