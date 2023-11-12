from libro import Libro
from disponible import Disponible
from prestado import Prestado
from extraviado import Extraviado
from datetime import datetime, timedelta
libro1 = Libro(123,"asd","desc",200)
print(libro1.get_estado())


a = datetime.now()
nuevafecha = a + timedelta(days=90)
print(nuevafecha)

