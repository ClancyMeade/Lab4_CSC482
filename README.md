## Steps to get started on the MYSQL Server:

Download the server: \
https://dev.mysql.com/downloads/mysql/

- This will ask you to pick a root password, remember that!

Then once that us done:\
`Run pip3 install mysql-connector-python`

After this create a `.py` files with the following contents:

```
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user={$yourname},
        password={lab4$yourname},
        database="lab4",
    ) as connection:
       print(connection)
except Error as e:
    print(e)

```

Where $yourname will be your first name in lower case:

Ex:
clancy, dane, divya

---

If this does not work you might just have to do everything locally as `root`. In this case your file will look like:

```
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password={password you set above},
    ) as connection:
       print(connection)
except Error as e:
    print(e)
```

Helpful Links:

- https://realpython.com/python-mysql/
