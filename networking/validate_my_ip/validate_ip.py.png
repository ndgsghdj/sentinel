addr = input()

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

result = validate(addr)

if result:
    result = 'Valid'
else:
    result = 'Invalid'
        
print(f'{addr}: {result}')
