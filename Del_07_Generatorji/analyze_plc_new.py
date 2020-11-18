import os

import matplotlib.pyplot as plt
import pandas as pd


class LogParser:
    def __init__(self, input_file_name: str):
        self.input_file_name = input_file_name
        self.data = self._clean_data(self._read_file())
        self.timespan = self._get_timespan()

    def __str__(self):
        return f"Dataset: {self.input_file_name}\nSize: {self.data.shape}\nTimespan: {self.timespan}"

    def _read_file(self) -> pd.DataFrame:
        df = pd.read_csv(
            self.input_file_name, delimiter=";", low_memory=False, na_values=['=""']
        )
        return df

    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # odstranimo posebne znake
        df = df.replace('="', "", regex=True)
        df = df.replace('"', "", regex=True)
        # uredimo stolpec time
        df["Time"] = pd.to_datetime(df["Time"], format="%Y.%m.%d %H:%M:%S.%f")
        df["Original_Time"] = df["Time"]
        df = df.set_index("Time")
        # pretvorimo stolpec Type v kategorijo
        df["Type"] = df["Type"].astype("category")
        return df

    def _get_timespan(self):
        diff = self.data["Original_Time"].max() - self.data["Original_Time"].min()
        return diff

    def export_clean_data(self, export_format: str = "csv"):
        """Exports clean data to selected format (csv, json, xlsx)"""
        converted_file_name = (
            f"{os.path.splitext(self.input_file_name)[0]}-converted.{export_format}"
        )
        if export_format == "csv":
            self.data.to_csv(converted_file_name)
        elif export_format == "json":
            data_to_json = self.data.copy()
            data_to_json = data_to_json.reset_index()
            data_to_json.to_json(converted_file_name, orient="index")
        elif export_format == "xlsx":
            self.data.to_excel(converted_file_name)
        else:
            raise ValueError("Parameter export_format should be: csv, json, xlsx.")

    def type_rrep_resample_count(self, resample: int = 60) -> pd.DataFrame:
        df_log_rrep = self.data[
            self.data["Type"].str.contains("LOADNG RREP", na=False)
        ].copy()
        groups_rrep = (
            df_log_rrep["Type"]
            .resample(f"{resample}T", label="right", closed="right")
            .count()
        )
        return pd.DataFrame(groups_rrep)

    def plot_type_rrep_resample_count(self, resample=60):
        df_result = self.type_rrep_resample_count(resample)
        fig, ax = plt.subplots()
        df_result.plot(kind="bar", ax=ax, legend=False, color="red")
        ax.set_xlabel("Time")
        ax.set_ylabel("# of rrep")
        ax.set_title("rrep results")
        plt.tight_layout()
        plt.savefig(f"{self.input_file_name}_{resample}_plot.png")


if __name__ == "__main__":
    input_file = "Del_07_Generatorji/data/20200915 081812_10_2_6_26.csv"

    parser = LogParser(input_file)
    # parser.export_clean_data(export_format="json")

    # print(parser.data.head())

    print(parser.type_rrep_resample_count())
    parser.plot_type_rrep_resample_count()
