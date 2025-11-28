import yaml


def convert_json_to_yaml(data):
    yaml_str = yaml.dump(data, sort_keys=False)
    with open("schema.yaml", "w") as f:
        yaml.dump(data, f, sort_keys=False)

    return yaml_str

