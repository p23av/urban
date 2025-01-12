import logging

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        res = a / b
        logging.info(f'Успешное деление {a} / {b}')
        return res
    except ZeroDivisionError as err:
        logging.error('На ноль делить нельзя!', exc_info=True)
        return 0

def sqrt(a):
    return a**0.5

def pow(a, b):
    return a ** b

if __name__ == "__main__":
    # logging.debug('dbg')
    # logging.info('info')
    # logging.warning('warn')
    # logging.error('err')
    # logging.critical('crit')
    logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    print(div(3, 4))
    print(div(3, 0))