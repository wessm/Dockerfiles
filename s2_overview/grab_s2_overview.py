from huey import RedisHuey, crontab



huey = RedisHuey('grab_s2_overview')

@huey.task()
def add_numbers(a, b):
    print(a)
    print(b)
    return a + b
