import csv
from datetime import datetime, timedelta

import pandas as pd


def extract_logs_to_list(file_path: str) -> list:
    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data


def extract_start_time(data: list) -> datetime:
    start_time = datetime.strptime(data[0], "%a %b %d %H:%M:%S CEST %Y")
    return start_time


def parse_data(data: list, start_time: datetime) -> list:
    rows = []
    for line in data[4:]:
        line_splited = line.split()
        add_seconds = int(line_splited[2].split(".")[0])
        timestamp = start_time + timedelta(seconds=add_seconds)
        transfer_mbytesec = int(line_splited[4])
        bandwidth_gbitsec = float(line_splited[6])
        retr = int(line_splited[8])
        cwnd_kybytes = int(line_splited[9])
        rows.append(
            (timestamp, transfer_mbytesec, bandwidth_gbitsec, retr, cwnd_kybytes)
        )
    return rows


def write_to_csv(data: list, file_dst_path: str):
    headers = ["timestamp", "transfer_mbs", "bandwidth_gbs", "retr", "cwnd_kbs"]
    with open(file_dst_path, "w") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(data)


def print_statistics(file_name: str):
    iperf_data = pd.read_csv(
        file_name, parse_dates=["timestamp"], index_col=["timestamp"]
    )
    print(iperf_data.describe())


if __name__ == "__main__":
    text_data = extract_logs_to_list(
        "Del_03_Branje_in_pisanje_v_datoteke/data/iperf.txt"
    )
    start_time = extract_start_time(text_data)
    parsed_data = parse_data(text_data, start_time)
    write_to_csv(
        parsed_data, "Del_03_Branje_in_pisanje_v_datoteke/data/iperf_clean.csv"
    )
    print_statistics("Del_03_Branje_in_pisanje_v_datoteke/data/iperf_clean.csv")
