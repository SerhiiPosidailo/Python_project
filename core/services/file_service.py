import os
from uuid import uuid1


class FileService:
    @staticmethod
    def upload_avatar(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.surname, 'avatars', f'{uuid1()}.{ext}')

    @staticmethod
    def upload_car_photo(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join('cars_photo', f'{uuid1()}.{ext}')
