import time
from multiprocessing.dummy import Pool # 导入线程池模块对应的类

'''
线程池：multiprocessing.dummy 实际上是 threading 模块的一个包装器，它提供了与 multiprocessing 相同的接口，但使用的是线程而不是进程。
适用场景：适用于 I/O 密集型任务，例如网络请求、文件读写等，因为这些任务主要等待外部资源的响应，使用线程可以在等待期间处理其他任务。
全局解释器锁 (GIL)：由于使用的是线程，受限于 Python 的 GIL，多个线程不能同时执行 Python 字节码，因此在 CPU 密集型任务中效果不佳。
multiprocessing
进程池：multiprocessing 使用的是进程，每个进程都有自己的 Python 解释器和 GIL，因此可以真正并行地执行任务。
适用场景：适用于 CPU 密集型任务，例如复杂计算、数据处理等，因为这些任务需要大量的 CPU 时间，使用多进程可以充分利用多核 CPU 的优势。
开销：进程间通信和进程创建的开销比线程大，但在处理 CPU 密集型任务时，这些开销通常是值得的
'''




# # 使用单线程串行方式执行
# def get_page(str):
#     print('正在下载： ', str)
#     time.sleep(2)  # 模拟阻塞操作
#     print('下载成功： ', str)
#
#
# name_list = ['aa', 'bb', 'cc', 'dd']
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%d second' % (end_time - start_time))


# 使用线程池的方式执行
start_time = time.time()


def get_page(str):
    print('正在下载：', str)
    time.sleep(2)  # 模拟阻塞操作
    print('下载成功：', str)


name_list = ['aa', 'bb', 'cc', 'dd']
# 实例化一个线程池对象
pool = Pool(4)
# 将列表中的每一个元素传递给get_page处理，返回值就是get_page的返回值
pool.map(get_page, name_list)
end_time = time.time()

pool.close()
pool.join()
print(end_time - start_time, 'second')
