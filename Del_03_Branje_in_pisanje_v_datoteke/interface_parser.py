import json


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as file_reader:
        json_object = json.load(file_reader)
    return json_object


def parse_to_txt(data: dict, dst_file_path: str):
    imdata = data["imdata"]

    with open(dst_file_path, "w") as writer:
        for interface in imdata:
            attributes = interface["l1PhysIf"]["attributes"]
            dn = attributes["dn"]
            speed = attributes["speed"]
            mtu = attributes["mtu"]
            data_string = f"{dn:50} {speed:8} {mtu:7}\n"
            writer.write(data_string)


if __name__ == "__main__":
    interfaces_data = read_json(
        "Del_03_Branje_in_pisanje_v_datoteke/data/exer1-interface-data.json"
    )

    parse_to_txt(
        interfaces_data, "Del_03_Branje_in_pisanje_v_datoteke/data/interface_output.txt"
    )
