def check_str(data):
    def wrapper(*args, **kwargs):
        result = data(*args, **kwargs)
        for i in result:
            if isinstance(i, str):
                return f"<b>{result}</b>"
            else:
                return result
    return wrapper
@check_str
def get_data(data_1):
    res = data_1
    return res
print(get_data('asdaadsfsdsd'))