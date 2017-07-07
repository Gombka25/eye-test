import time


def wait_until(condition, timeout=10, raise_exception=True, msg=""):

    t0 = time.time()

    while  time.time() - t0 < timeout:
        if condition():
            return True
        time.sleep(0.1)

    if raise_exception:
        raise TimeoutError(f"{msg} after {timeout} sec")
    else:
        return False
