import asyncio
import random
from dataclasses import dataclass
from timeit import default_timer
import math
import uuid


async def generate_uid():

    return uuid.uuid4().hex


async def random_sleep(caller: str = ''):

    i = random.randint(0, 10)

    print(f'{caller} working (sleeping) for {i} seconds.')

    await asyncio.sleep(i)

    
async def producer(name: int, q: asyncio.Queue) -> None:

    n = random.randint(1, 5)

    for _ in range(n):
        await random_sleep(caller=f'Producer {name}')

        res = await generate_uid()

        t = default_timer()

        await q.put((res, t))

        print(f'Producer {name} added <{res}> to queue.')


async def consumer(name: int, q: asyncio.Queue) -> None:

    while True:

        await random_sleep(caller=f'Consumer {name}')

        i, t = await q.get()

        d_time = default_timer() - t

        print(f'Consumer {name} received <{i}> in {d_time:0.5f} seconds.')

        q.task_done()

        
async def main():

    q = asyncio.Queue()

    producers = [asyncio.create_task(producer(q=q, name=n)) for n in range(5)]
    consumers = [asyncio.create_task(consumer(q=q, name=n)) for n in range(5)]

    await asyncio.gather(*producers)
    await q.join() # Wait cunsumers.

    for cons in consumers:
        cons.cancel()


if __name__ == '__main__':

    start = default_timer()
    asyncio.run(main())
    elapsed = default_timer() - start

    print(f'Exiting after (s): {elapsed:0.5f}')

'''
SAMPLE OUTPUT:
Producer 0 working (sleeping) for 5 seconds.
Producer 1 working (sleeping) for 9 seconds.
Producer 2 working (sleeping) for 10 seconds.
Producer 3 working (sleeping) for 4 seconds.
Producer 4 working (sleeping) for 5 seconds.
Consumer 0 working (sleeping) for 8 seconds.
Consumer 1 working (sleeping) for 9 seconds.
Consumer 2 working (sleeping) for 7 seconds.
Consumer 3 working (sleeping) for 7 seconds.
Consumer 4 working (sleeping) for 9 seconds.
Producer 3 added <8534ccd1eb04492e8c194bcf1f21da0c> to queue.
Producer 3 working (sleeping) for 8 seconds.
Producer 0 added <5a7102e446844c439eff1a0415cedb25> to queue.
Producer 0 working (sleeping) for 7 seconds.
Producer 4 added <a7be77918ba04f1dbd835ec0cc9aa052> to queue.
Producer 4 working (sleeping) for 0 seconds.
Producer 4 added <2b514366eba4407086f5c9b47f9353ac> to queue.
Producer 4 working (sleeping) for 6 seconds.
Consumer 2 got element <8534ccd1eb04492e8c194bcf1f21da0c> in 2.99869 seconds.
Consumer 2 working (sleeping) for 0 seconds.
Consumer 3 got element <5a7102e446844c439eff1a0415cedb25> in 2.00287 seconds.
Consumer 3 working (sleeping) for 4 seconds.
Consumer 2 got element <a7be77918ba04f1dbd835ec0cc9aa052> in 2.00281 seconds.
Consumer 2 working (sleeping) for 5 seconds.
Consumer 0 got element <2b514366eba4407086f5c9b47f9353ac> in 3.00045 seconds.
Consumer 0 working (sleeping) for 7 seconds.
Producer 1 added <f2ae5d87340f4db6bb02f9731382605a> to queue.
Producer 1 working (sleeping) for 2 seconds.
Consumer 1 got element <f2ae5d87340f4db6bb02f9731382605a> in 0.00020 seconds.
Consumer 1 working (sleeping) for 6 seconds.
Producer 2 added <5e00ab94a9d74719ac18edc608f3e76f> to queue.
Producer 2 working (sleeping) for 0 seconds.
Consumer 4 got element <5e00ab94a9d74719ac18edc608f3e76f> in 0.00017 seconds.
Consumer 4 working (sleeping) for 10 seconds.
Producer 2 added <12b1014d3fb046de917cfbb06f2ea081> to queue.
Producer 2 working (sleeping) for 3 seconds.
Producer 4 added <d62b7b72d4104a24871871d689efb734> to queue.
Producer 4 working (sleeping) for 9 seconds.
Producer 1 added <4c81be043d634680939f0163e7b690ff> to queue.
Producer 1 working (sleeping) for 1 seconds.
Consumer 3 got element <12b1014d3fb046de917cfbb06f2ea081> in 1.00464 seconds.
Consumer 3 working (sleeping) for 1 seconds.
Producer 0 added <9ba874d78438438c8c068eb36aedf6fe> to queue.
Producer 0 working (sleeping) for 7 seconds.
Consumer 2 got element <d62b7b72d4104a24871871d689efb734> in 0.99987 seconds.
Consumer 2 working (sleeping) for 5 seconds.
Producer 3 added <a2d3e12c6d39494c8d0bb646bcd15dec> to queue.
Producer 3 working (sleeping) for 3 seconds.
Producer 1 added <c890db89b9e34554abd27cbbd16b80d2> to queue.
Producer 1 working (sleeping) for 3 seconds.
Consumer 3 got element <4c81be043d634680939f0163e7b690ff> in 1.00138 seconds.
Consumer 3 working (sleeping) for 5 seconds.
Producer 2 added <9d309d840f004e8cba22b9b4a76de7c9> to queue.
Producer 2 working (sleeping) for 6 seconds.
Consumer 0 got element <9ba874d78438438c8c068eb36aedf6fe> in 3.00314 seconds.
Consumer 0 working (sleeping) for 3 seconds.
Consumer 1 got element <a2d3e12c6d39494c8d0bb646bcd15dec> in 3.00071 seconds.
Consumer 1 working (sleeping) for 10 seconds.
Producer 3 added <4715acd15d154843a02ebf316ec7a0a2> to queue.
Producer 3 working (sleeping) for 0 seconds.
Producer 3 added <764c75b034b64eb7b1d3efcf07abd67f> to queue.
Producer 3 working (sleeping) for 4 seconds.
Producer 1 added <f3dfc3eb0d5f4ecdab8310f48b39c4f0> to queue.
Producer 1 working (sleeping) for 5 seconds.
Consumer 2 got element <c890db89b9e34554abd27cbbd16b80d2> in 5.00192 seconds.
Consumer 2 working (sleeping) for 1 seconds.
Consumer 3 got element <9d309d840f004e8cba22b9b4a76de7c9> in 4.00496 seconds.
Consumer 3 working (sleeping) for 0 seconds.
Consumer 3 got element <4715acd15d154843a02ebf316ec7a0a2> in 2.00280 seconds.
Consumer 3 working (sleeping) for 8 seconds.
Consumer 0 got element <764c75b034b64eb7b1d3efcf07abd67f> in 3.00150 seconds.
Consumer 0 working (sleeping) for 0 seconds.
Consumer 0 got element <f3dfc3eb0d5f4ecdab8310f48b39c4f0> in 3.00050 seconds.
Consumer 0 working (sleeping) for 6 seconds.
Producer 0 added <591461f77349436fa28ad29f4217b80d> to queue.
Producer 0 working (sleeping) for 10 seconds.
Producer 2 added <b371162152b94b09914ba959a5a2ae23> to queue.
Producer 2 working (sleeping) for 8 seconds.
Consumer 2 got element <591461f77349436fa28ad29f4217b80d> in 0.00037 seconds.
Consumer 2 working (sleeping) for 9 seconds.
Producer 3 added <463f20151a0646d88946c5dccc8382be> to queue.
Consumer 4 got element <b371162152b94b09914ba959a5a2ae23> in 0.99779 seconds.
Consumer 4 working (sleeping) for 1 seconds.
Producer 4 added <590ea5137e4747b2b4b74b32facdb4ff> to queue.
Producer 4 working (sleeping) for 1 seconds.
Producer 1 added <d3c1697942fc4927be1ff23e7beb89c4> to queue.
Consumer 4 got element <463f20151a0646d88946c5dccc8382be> in 1.99797 seconds.
Consumer 4 working (sleeping) for 8 seconds.
Producer 4 added <c0f44b1287f64b55ad1f2ab14214efa7> to queue.
Consumer 0 got element <590ea5137e4747b2b4b74b32facdb4ff> in 4.00595 seconds.
Consumer 0 working (sleeping) for 10 seconds.
Consumer 1 got element <d3c1697942fc4927be1ff23e7beb89c4> in 4.99901 seconds.
Consumer 1 working (sleeping) for 8 seconds.
Consumer 3 got element <c0f44b1287f64b55ad1f2ab14214efa7> in 4.00336 seconds.
Consumer 3 working (sleeping) for 2 seconds.
Producer 2 added <d3e1a59d687e44989a801eeedeeac7f1> to queue.
Consumer 3 got element <d3e1a59d687e44989a801eeedeeac7f1> in 0.00326 seconds.
Consumer 3 working (sleeping) for 8 seconds.
Producer 0 added <2028b52a098044fc8b1e75cfbabb9f00> to queue.
Producer 0 working (sleeping) for 2 seconds.
Consumer 4 got element <2028b52a098044fc8b1e75cfbabb9f00> in 0.00022 seconds.
Consumer 4 working (sleeping) for 3 seconds.
Producer 0 added <62e37483fe134b9a9196cc2ecf962817> to queue.
Consumer 2 got element <62e37483fe134b9a9196cc2ecf962817> in 0.00014 seconds.
Consumer 2 working (sleeping) for 4 seconds.
Program completed in 31.01554 seconds.
'''