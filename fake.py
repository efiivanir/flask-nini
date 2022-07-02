from app.models import Therapist, House, db
statuses = ['RIP','FUNCTIONAL','NURSING','TIRED']

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
    username = 'sungirl7',
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
