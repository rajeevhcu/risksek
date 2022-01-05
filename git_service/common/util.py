from ..common import constants


def get_page_num_size(page_number, page_size):
    try:
        if page_number in [None, '']:
            page_number = constants.PAGE_NUMBER
        else:
            try:
                page_number = int(page_number)
            except ValueError:
                page_number = constants.PAGE_NUMBER
        if page_size in [None, '']:
            page_size = constants.PAGE_SIZE
        else:
            try:
                page_size = int(page_size)
            except ValueError:
                page_size = constants.PAGE_SIZE
        return page_number, page_size
    except Exception as err:
        raise Exception(err)


def get_time_in_ms(unix_time):
    """get the time in milliseconds."""
    return int(round(unix_time * 1000))
