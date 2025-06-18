import pathlib as p

o = p.Path('test.txt')
o.touch()
o.unlink()
print(o.exists())

print(list(p.Path('.').glob('*.py')))