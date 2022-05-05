from multiprocessing import Pool
from functools import partial
from libs import core

if __name__ == "__main__":
    length = core.integer('Min length')
    amount = core.integer('Wallets amount')
    threads = core.integer('Treads')

    partial_work = partial(core.generate, min_length=length)

    pool = Pool(threads)
    pool.map(partial_work, range(amount))
    pool.close()
    pool.join()
