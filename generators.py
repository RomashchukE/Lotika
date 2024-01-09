from faker import Faker
import hashlib

faker_en = Faker('En')
Faker.seed()

def generate_test_email():
    first_name = faker_en.first_name()
    last_name = faker_en.last_name()
    mail_name = f"{first_name}{last_name}"
    email = f"{mail_name}@any.pink"
    # hashed_email_address = hashlib.md5(email.encode('utf-8')).hexdigest()
    # Get test email
    return mail_name, email

def write_data_to_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(data))
        print(f"Данные успешно записаны в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи данных в файл: {e}")
