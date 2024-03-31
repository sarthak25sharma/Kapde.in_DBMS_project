from dataclasses import dataclass
from typing import List

from rich.table import Column


class MetaTable(type):
    def __repr__(self) -> str:
        return self.__name__


@dataclass
class Table(metaclass=MetaTable):
    @classmethod
    def columns(cls) -> List[Column]:
        cols: List[Column] = []
        for name in cls.__dict__:
            attr = getattr(cls, name)
            if isinstance(attr, Column):
                cols.append(attr)

        return cols

    @classmethod
    def colnames(cls) -> List[str]:
        return [col.name for col in cls.columns()]


@dataclass
class Column:
    dtype: str
    name: str = ""
    constraints: str = ""
    full: str = ""

    def __str__(self):
        return self.name


class Brand(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    name = Column("VARCHAR(64)", constraints="NOT NULL")


class User(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    username = Column("TEXT", constraints="NOT NULL")
    password = Column("VARCHAR(64)", constraints="NOT NULL DEFAULT 'pass'")  # Hashed
    is_customer = Column("NUMBER(1,0)", constraints="NOT NULL DEFAULT '1'")
    house_num = Column("VARCHAR(5)", constraints="NOT NULL DEFAULT 'ab12'")
    locality = Column("FLOAT", constraints="NOT NULL DEFAULT 'locality_a'")
    city = Column("FLOAT", constraints="NOT NULL DEFAULT 'city_a'")
    state = Column("FLOAT", constraints="NOT NULL DEFAULT 'state_a'")
    pin_code = Column("NUMBER(6,0)", constraints="NOT NULL")
    country = Column("TEXT", constraints="NOT NULL")
    gender = Column("VARCHAR(1)", constraints="NOT NULL")


class Admin(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    password = Column("VARCHAR(64)", constraints="NOT NULL")  # Hashed


class Product(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    name = Column("VARCHAR(32)", constraints="NOT NULL")
    description = Column("TEXT", constraints="NOT NULL")
    price = Column("FLOAT", constraints="NOT NULL DEFAULT 0.0")
    brand_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {Brand}(id)")  # todo add {Brand.id}


class Seller(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    name = Column("VARCHAR(32)", constraints="NOT NULL")
    username = Column("VARCHAR(32)", constraints="NOT NULL")
    password = Column("VARCHAR(64)", constraints="NOT NULL")  # Hashed


class Orders(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    user_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {User}(id)")


class OrderItem(Table):
    user_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {User}(id)")
    order_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {Orders}(id)")
    product_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {Product}(id)")
    quantity = Column("INTEGER", constraints=f"NOT NULL")


class CartItem(Table):
    id = Column("INTEGER", constraints="PRIMARY KEY AUTOINCREMENT")
    product_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {Product}(id)")
    user_id = Column("INTEGER", constraints=f"NOT NULL REFERENCES {User}(id)")
    quantity = Column("INTEGER", constraints="NOT NULL")


TABLES = (
    User,
    Admin,
    Brand,
    Product,
    CartItem,
    Orders,
    OrderItem,
)
