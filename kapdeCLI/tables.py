from dataclasses import dataclass
from typing import List


class MetaTable(type):
    def __repr__(self) -> str:
        return self.__name__


@dataclass
class Table(metaclass=MetaTable):
    @classmethod
    def columns(cls):
        cols: List[Column] = []
        for name in dir(cls):
            attr = getattr(cls, name)
            if isinstance(attr, Column):
                cols.append(attr)

        return cols


@dataclass
class Column:
    dtype: str
    name: str = ""
    constraints: str = ""
    full: str = ""

    def __str__(self):
        return self.name


class Buyer(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY")
    name = Column("VARCHAR(32)", constraints="NOT NULL")
    username = Column("VARCHAR(32)", constraints="NOT NULL")
    password = Column("VARCHAR(64)", constraints="NOT NULL")  # Hashed
    money = Column("FLOAT", constraints="NOT NULL DEFAULT 0")


class User(Table):
    user_id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    user_name = Column("TEXT", constraints="NOT NULL")
    password = Column("VARCHAR(64)", constraints="NOT NULL DEFAULT 'pass'")  # Hashed
    is_customer = Column("VARCHAR(32)", constraints="NOT NULL DEFAULT '1'")
    house_num = Column("VARCHAR(5)", constraints="NOT NULL DEFAULT 'ab12'")
    locality = Column("FLOAT", constraints="NOT NULL DEFAULT 'locality_a'")
    city = Column("FLOAT", constraints="NOT NULL DEFAULT 'city_a'")
    state = Column("FLOAT", constraints="NOT NULL DEFAULT 'state_a'")
    pin_code = Column("NUMBER(6,0)", constraints="NOT NULL")
    country = Column("TEXT", constraints="NOT NULL")
    gender = Column("VARCHAR(1)", constraints="NOT NULL")


class Admin(Table):
    admin_id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    password = Column("VARCHAR(64)", constraints="NOT NULL")  # Hashed


class Brand(Table):
    brand_id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    brand_name = Column("VARCHAR(32)", constraints="NOT NULL")


class Product(Table):
    product_id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    product_name = Column("VARCHAR(32)", constraints="NOT NULL")
    description = Column("TEXT", constraints="NOT NULL")
    price = Column("FLOAT", constraints="NOT NULL DEFAULT 0.0")
    brand_id = Column("INTEGER", constraints="NOT NULL")


class Seller(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    name = Column("VARCHAR(32)", constraints="NOT NULL")
    username = Column("VARCHAR(32)", constraints="NOT NULL")
    password = Column("VARCHAR(64)", constraints="NOT NULL")  # Hashed


TABLES = (
    User,
    Admin,
    Product,
    Brand,
)
