def validate(addr):
    if addr.count('.') == 3:
        temp = [int(k) for k in addr.split('.')]
        addr = addr.split('.')

        for i in temp:
            if i < 0 or i > 255:
                return False

        for s in addr:
            if s[0] == '0' and len(s) > 1:
                return False

        return True

    return False

def classify(addr):
    result = validate(addr)

    if result:
        if addr == '127.0.0.1':
            return 'localhost'
        else:
            temp = addr.split('.')
            if temp[0] == '192' and temp[1] == '168' or temp[0] == '10' or temp[0] == '172' and temp[1] == '16':
                result = 'private'
            else:
                result = 'public'
    else:
        result = 'invalid'

    return result
            
addrs = [
        '192.168.1.1', # private: 192.168.x.x
        '10.25.30.50', # private: 10.x.x.x
        '172.20.10.5', # public
        '127.0.0.1',   # localhost: loopback
        '172.32.0.1',  # public
        '266.32.0.1',  # invalid: 266 > 255
        '216.58.214.206' # public
        ]

for addr in addrs:
    result = classify(addr)

    print(f"{addr}: {result}")
