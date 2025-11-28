from src.extract_schema import extract
from src.transform_schema import transform
from src.utils import convert_json_to_yaml
from src.generate_query import generate_query
from src.run_query import run_query


def main():
    columns_info, constraints_info = extract()
    schema = transform(columns_info, constraints_info)
    yaml_schema = convert_json_to_yaml(schema)

    while True:
        question = input("Enter your query: ")

        if question == "exit":
            break

        query = generate_query(question, yaml_schema)
        if len(query) > 1:
            print("\n\n******GENERATED QUERY******\n\n")
            print(query)

            print("\n\n******GENERATED RESULT******\n\n")
            result = run_query(query)

            for row in result:
                print(row)

        else:
            print("Invalid Schema Provided")


if __name__ == "__main__":
    main()
