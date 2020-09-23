import sqlite3
import vobject

def table_exists(cursor, table_name):
    cursor.execute('''
        SELECT count(name)
        FROM sqlite_master
        WHERE type='table' AND name='{}'
        '''.format(table_name))
        
    return cursor.fetchone()[0] == 1


def create_vcard(name, phone_number):
    card = vobject.vCard()
    card.add('fn')
    card.fn.value = name
    card.add('tel')
    card.tel.type_param = 'CELL'
    card.tel.value = phone_number

    return card


def save_vcf(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(contacts)
        file.close()


conn = sqlite3.connect('viber.db')
cursor = conn.cursor()

sql_expression1 = '''
SELECT Contacts.id, Contacts.DisplayName, PhoneNumbers.OriginalNumber
FROM Contacts INNER JOIN PhoneNumbers
ON Contacts.id = PhoneNumbers.id
'''

sql_expression2 = '''
SELECT ContactID, Name, Number, ClientName
FROM 'Contact'
WHERE Name != 'null'
'''

contacts = ''

if table_exists(cursor, 'Contacts'):
    print('Contacts table exists!')

    for row in cursor.execute(sql_expression1):
        contacts += create_vcard(name=row[1], phone_number=row[2]).serialize().replace('\r\n', '\n')

elif table_exists(cursor, 'Contact'):
    print('Contact table exists!')

    for row in cursor.execute(sql_expression2):
        contacts += create_vcard(name=row[1], phone_number=row[2]).serialize().replace('\r\n', '\n')

if contacts:
    save_vcf('new_contacts.vcf', contacts)


conn.close()