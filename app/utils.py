import string
import random

def random_name(n=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

def file_random_name(file, rand_name, pad):
    name = file.name
    real_name, ext = name.split('.')
    return f"{rand_name}_{pad}.{ext}"

def handle_upload(data_uji, files):
    new_name = random_name()
    result = []
    for i, file in enumerate(files):
        name = file.name
        real_name, ext = name.split('.')
        new_full_name = f"uploads/{new_name}_{i}.{ext}"
        content = file.read()
        with open(new_full_name, 'wb') as f:
            f.write(content)
            result.append(new_full_name, new_name)
    return result