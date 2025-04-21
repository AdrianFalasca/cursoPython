from peewee import *
from datetime import datetime


db = SqliteDatabase(
            database="base_python")

class BaseModel(Model):
    """Clases que crean y conectan con la bbdd y la tabla. ORM """
    class Meta:
        database = db
        
class Logica(BaseModel):
    id = AutoField()
    fecha = DateTimeField(default=datetime.now().strftime("%d/%m/%Y - %H:%M:%S"))
    conector = CharField()
    simbolo = CharField()
    info = TextField()

db.connect()
db.create_tables([Logica])
db.close()
