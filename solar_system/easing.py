def ease_out_quad(t, b, c, d):
    """
    :param t: the current time (or position) of the tween.
    :param b: the beginning value of the property.
    :param c: the change between the beginning and destination value of the property.
    :param d: the total time of the tween.
    :return: the current value of the tween.
    """
    t /= d
    return -c * t*(t-2) + b
