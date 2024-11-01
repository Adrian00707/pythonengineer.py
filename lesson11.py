import yaml
import json
import pandas as pd


class DataHandler:
    def __init__(self):
        self.data_list = []
        self.dataframe = pd.DataFrame()

    def add_data(self, data):
        if isinstance(data, dict):
            self.data_list.append(data)
        else:
            print("Data must be represent as dict")

    def save_to_yaml(self, filename):
        with open(filename, 'w') as file:
            yaml.dump(self.data_list, file)

    def load_from_yaml(self, filename):
        with open(filename, 'r') as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data_list, file)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            self.data_list = json.load(file)

    def safe_to_csv(self, filename):
        self.dataframe.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        self.dataframe = pd.read_csv(filename)

    def display_data(self):
        print("List of dict")
        print(self.data_list)
        print('DataFrame')
        print(self.dataframe)


class DataHolder:
    def __init__(self):
        self.data_list = []
        self.dataframe = pd.DataFrame()

    def add_data(self, filedict):
        if isinstance(filedict, dict):
            self.data_list.append(filedict)
        else:
            print("Data must be represented as 'dict'")

    def save_to_yaml(self, filename):
        with open(filename, 'w') as file:
            yaml.dump(self.data_list, filename)

    def load_yaml(self, filename):
        with open(filename, 'r') as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data_list, filename)

    def load_json(self, filename):
        with open(filename, 'r') as file:
            self.data_list = json.load(file)

    def save_to_csv(self, filename):
        self.dataframe.to_csv(filename, index=False)

    def load_csv(self, filename):
        self.dataframe = pd.read_csv(filename)

    def show_alldata(self):
        print("Here is list of data's")
        print(self.data_list)
        print('Dataframe')
        print(self.dataframe)


class DataHolding:
    def __init__(self):
        self.data_list = []
        self.data_frame = pd.DataFrame()

    def save_to_yaml(self, filename):
        with open(filename, 'w') as file:
            yaml.dump(self.data_list, file)

    def load_yaml(self, filename):
        with open(filename, 'r') as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data_list, file, indent=4)

    def load_json(self, filename):
        with open(filename, 'r') as file:
            self.data_list = json.load(file)

    def save_csv(self, filename):
        self.data_frame.to_csv(filename, index=False)

    def load_csv(self, filename):
        self.data_frame = pd.read_csv(filename)

    def display_file(self):
        print(self.data_list)

    def display_data_frame(self):
        print(self.data_frame)

    def from_yaml_to_json(self, yaml_file, json_file):
        self.load_yaml(yaml_file)
        self.save_to_json(json_file)

    def from_json_to_yaml(self, json_file, yaml_file):
        self.load_json(json_file)
        self.save_to_yaml(yaml_file)


class DataHalder:
    def __init__(self):
        self.data_list = []
        self.data_frame = pd.DataFrame()

    def save_to_yaml(self, file_name):
        with open(file_name, 'w') as file:
            yaml.dump(self.data_list, file)

    def load_yaml(self, file_name):
        with open(file_name, 'r') as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.data_list, file, indent=4)

    def load_json(self, file_name):
        with open(file_name, 'r') as file:
            self.data_list = json.load(file)

    def save_to_csv(self, file_name):
        self.data_frame.to_csv(file_name, index=False)

    def load_csv(self, file_name):
        self.data_frame = pd.read_csv(file_name)

    def from_yaml_to_json(self, yaml_name, json_name):
        self.load_yaml(yaml_name)
        self.save_to_json(json_name)

    def from_json_to_yaml(self, json_file, yaml_file):
        self.load_json(json_file)
        self.save_to_yaml(yaml_file)

    def show_data_list(self):
        print(self.data_list)

    def show_data_frame(self):
        print(self.data_frame)


class DATAHold:
    def __init__(self):
        self.data_list = []
        self.data_frame = pd.DataFrame()

    def add_file(self, new_data: dict):
        self.data_list.append(new_data)

    def save_to_yaml(self, file_name):
        with open(file_name, 'w') as file:
            yaml.dump(self.data_list, file)

    def load_yaml(self, file_name):
        with open(file_name, 'r') as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.data_list, file, indent=4)

    def load_json(self, file_name):
        with open(file_name, 'r') as file:
            self.data_list = json.load(file)

    def save_csv(self, data_frame):
        self.data_frame.to_csv(data_frame, index=False)

    def load_csv(self, data_frame):
        self.data_frame = pd.read_csv(data_frame)

    def show_data(self):
        for item in self.data_list:
            print(item)

    def display_data_list(self):
        print(self.data_list)


class HoldData:
    def __init__(self):
        self.data_list = []
        self.df_list = pd.DataFrame()

    def save_to_yaml(self, file_name):
        with open(file_name, 'w',) as file:
            yaml.dump(self.data_list, file)

    def load_yaml(self, file_name):
        with open(file_name, 'r',) as file:
            self.data_list = yaml.safe_load(file)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.data_list, file, indent=4)

    def load_json(self, file_name):
        with open(file_name, 'r') as file:
            self.data_list = json.load(file)

    def save_to_csv(self, filename):
        self.df_list.to_csv(filename, index=False)

    def load_csv(self, filename):
        self.df_list = pd.read_csv(filename)

    def add_list(self, file: dict):
        self.data_list.append(file)

    def show_datas(self):
        print(self.data_list)

    def show_df(self):
        print(self.df_list)
