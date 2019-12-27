def handle_error_by_throwing_exception():
    raise Exception("An Exception")


def handle_error_by_returning_none(input_data):
    try:
        data = int(input_data)
        return data
    except Exception:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        data = int(input_data)
        return True, data
    except Exception:
        return False, ()


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
        filelike_object.close()
    except Exception:
        filelike_object.close()
        filelike_object.do_something()
