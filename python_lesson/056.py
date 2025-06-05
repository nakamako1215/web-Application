ascii_dict = {'0x30': '0', '0x40': '@', '0x50': 'P'}
reversed_dict = {value: key for key, value in ascii_dict.items()}
print(reversed_dict)