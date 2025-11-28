from src.extract_schema import extract
from src.transform_schema import transform
from src.utils import convert_json_to_yaml


def main():
    columns_info, constraints_info = extract()
    schema = transform(columns_info, constraints_info)

    yaml_schema = convert_json_to_yaml(schema)
    print(yaml_schema)


if __name__ == "__main__":
    main()
