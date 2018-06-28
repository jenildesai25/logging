# https://docs.python.org/3/library/configparser.html
try:
    from logger import Logger
    import os
    import json
    import pprint
except Exception as e:
    Logger().error('can not install module'+str(e))

class Config:

    def __init__(self):
        # self.logger = []
        # self.mapr = []
        # self.mongo = []
        self.file_open = open('E:/Study/python projects/app.json')
        self.load_config_file = json.load(self.file_open)
        # print(self.load_json_file)

    def get_appSettings(self, key):
        self.appSettings = self.load_config_file['appSettings']
        return self.appSettings[key]

    def get_logger(self, version=None,disable_existing_loggers=None,handlers=None,file_handler=None,loggers=None,formatters=None,root=None):
        self.logger_info = self.load_config_file['logging']
        # self self.logger_info(logger_info['disable_existing_loggers'])
        return self.logger_info[handlers][file_handler]

    # def get_mongo(self, key=None):
    #     self.mongo_info = self.load_config_file['logging']
    #     # self self.logger_info(logger_info['disable_existing_loggers'])
    #     return self.mongo_info[]

if __name__ == '__main__':

    config_obj = Config()
    appsetting = config_obj.get_appSettings(key='evolve')
    pprint.pprint(config_obj.get_logger(handlers='handlers',file_handler='file_handler'))


