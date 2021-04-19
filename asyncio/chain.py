import os
import asyncio
from dataclasses import dataclass
from timeit import default_timer
import uuid


@dataclass
class User:
    id: str
    name: str
    profile_pic_path: str


async def get_user(user_id: str) -> User:

    print('get_user function start.')

    start = default_timer()
    await asyncio.sleep(2)

    data_from_db = {'name': 'Test User 1', 'profile_pic_uri': '../img.jpg'}
    user = User(user_id, data_from_db['name'], data_from_db['profile_pic_uri'])

    end = default_timer() - start
    print(f'get_user end after (s): {end}')

    return user


async def get_profile_picture(path: str) -> bytearray:

    print('get_profile_picture function start.')

    start = default_timer()
    await asyncio.sleep(2)

    end = default_timer() - start
    print(f'get_profile_picture end after (s): {end}')

    return bytearray(os.urandom(100000))


async def chain(user_id: str):

    print('chain function start.')

    start = default_timer()

    user = await get_user(user_id=user_id)

    profile_picture = await get_profile_picture(path=user.profile_pic_path)

    end = default_timer() - start

    print(f'chain function end after (s): {end}')


async def main():

    ids = [uuid.uuid4().hex, uuid.uuid4().hex, uuid.uuid4().hex]
    await asyncio.gather(*(chain(id) for id in ids))


if __name__ == '__main__':
    
    start = default_timer()

    asyncio.run(main())

    end = default_timer() - start

    print(f'Exiting after (s): {end}')
    
'''
SAMPLE OUTPUT:
chain function start.
get_user function start.
chain function start.
get_user function start.
chain function start.
get_user function start.
get_user end after (s): 2.0031747829998494
get_profile_picture function start.
get_user end after (s): 2.0033754749965738
get_profile_picture function start.
get_user end after (s): 2.0034250559983775
get_profile_picture function start.
get_profile_picture end after (s): 2.0016810950000945
chain function end after (s): 4.007249425998452
get_profile_picture end after (s): 2.003777458998229
chain function end after (s): 4.009071958000277
get_profile_picture end after (s): 2.005618831997708
chain function end after (s): 4.010968480000884
Exiting after (s): 4.013840653999068
'''