import websockets
import asyncio
import json


class MyRequests:
    @staticmethod
    def add(name: str, surname: str, phone: str, age: int, id_req: str = 'sfda-11231-123-adfa'):
        data = '{' \
                 f'"id": "{id_req}",' \
                 '"method": "add",' \
                 f'"name": "{name}",' \
                 f'"surname": "{surname}",' \
                 f'"phone": "{phone}",' \
                 f'"age": {age}' \
                 '}'

        return MyRequests._send(data)

    @staticmethod
    def delete(phone, id_req: str = 'sfda-11231-123-adfa'):
        data = '{' \
               f'"id": "{id_req}",' \
               '"method": "delete",' \
               f'"phone": "{phone}"' \
               '}'

        return MyRequests._send(data)

    @staticmethod
    def update(name: str, surname: str, phone: str, age: int, id_req: str = 'sfda-11231-123-adfa'):
        data = '{' \
               f'"id": "{id_req}",' \
               '"method": "update",' \
               f'"name": "{name}",' \
               f'"surname": "{surname}",' \
               f'"phone": "{phone}",' \
               f'"age": {age}' \
               '}'

        return MyRequests._send(data)

    @staticmethod
    def select(name: str = None, surname: str = None, phone: str = None, id_req: str = '123412-adf-13213'):
        if name is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"name": "{name}"' \
                   '}'
        elif surname is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"surname": "{surname}"' \
                   '}'
        elif phone is not None:
            data = '{' \
                   f'"id": "{id_req}",' \
                   '"method": "select",' \
                   f'"phone": "{phone}"' \
                   '}'
        else:
            raise Exception(f"Все критерии поиска были пустыми")

        return MyRequests._send(data)

    @staticmethod
    def any_method(data: str):
        return MyRequests._send(data)

    @staticmethod
    async def do_smth(data: str, uri: str = 'ws://127.0.0.1:4000'):
        async with websockets.connect(uri) as ws:
            await ws.send(data)
            repl = await ws.recv()

            return str(json.loads(repl))

    @staticmethod
    def _send(data: str):
        return asyncio.get_event_loop().run_until_complete(MyRequests.do_smth(data))
