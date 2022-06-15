from app.models import PatientsStatus, Therapist, House, db
statuses = ['RIP','FUNCTIONAL','NURSING','TIRED']

for st in statuses:
    s = PatientsStatus(status=st)
    db.session.add(s)
    db.session.commit()

t = Therapist(
    username = 'ivanir',
    email = 'efi.ivanir@gmail.com',
    first_name = 'Efi',
    last_name = 'Ivanir',
    tz_id = '022397103',

    phone = '0547884102',
    address_city = 'K.Tiveon',
    address_street = 'Dayan Moshe',
    address_house_num = '5/8',
)
t.set_password('123456')
db.session.add(t)
db.session.commit()

t = Therapist(
    username = 'admin',
    email = 'efi.ivanir@gmail.com',
    first_name = 'Efi',
    last_name = 'Ivanir',
    tz_id = '022397103',

    phone = '0547884102',
    address_city = 'K.Tiveon',
    address_street = 'Dayan Moshe',
    address_house_num = '5/8',
)
t.set_password('123456')
db.session.add(t)
db.session.commit()

t = Therapist(
    username = 'danaik',
    email = 'sungirl7@gmail.com',
    first_name = 'Dana',
    last_name = 'Ivanir Kalizki',
    tz_id = '333750875',

    phone = '0547884102',
    address_city = 'K.Tiveon',
    address_street = 'Dayan Moshe',
    address_house_num = '5/8',
)
t.set_password('123456')
db.session.add(t)
db.session.commit()
