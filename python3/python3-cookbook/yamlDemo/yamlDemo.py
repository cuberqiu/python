import yaml

with open('./test.yaml', 'r') as f:
    data = yaml.load(f)

    print(type(data))
    print(data)

    print(data['DISK']['path'])