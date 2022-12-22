import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engineをインメモリで作成し、SQL実行結果を発行する
engine = sqlalchemy.create_engine("sqlite:///:memory:", echo=True)

# engineをSQLiteで作成し書き込む際の接続情報
# engine = sqlalchemy.create_engine("sqlite:///test_sqlite.db", echo=True)

base = sqlalchemy.ext.declarative.declarative_base()


# Models定義
class Person(base):
    __tablename__ = "persons"
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# CREATE
person1 = Person(name="Mike")
session.add(person1)

person2 = Person(name="Nancy")
session.add(person2)

person3 = Person(name="Jun")
session.add(person3)

session.commit()

# UPDATE
person4 = session.query(Person).filter_by(name="Mike").first()
person4.name = "Mikey"
session.add(person4)
session.commit()

# DELETE
person5 = session.query(Person).filter_by(name="Nancy").first()
session.delete(person5)
session.commit()

# READ
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
