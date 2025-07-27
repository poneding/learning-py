from concurrent.futures import ThreadPoolExecutor


def task(name):
    for i in range(1000):
        print(f"Task {name} is running iteration {i}")


if __name__ == "__main__":
    # 创建线程池
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(100):
            t.submit(task, name=f"Task-{i}")  # 提交任务

    # 这里会等待 with 块结束后所有线程完成
    print("All tasks submitted")
