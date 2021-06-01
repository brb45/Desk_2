#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: zy7y
@file: base_requests.py
@ide: PyCharm
@time: 2020/7/31
"""
from loguru import logger
import requests


class BaseRequest(object):
    def __init__(self):
        pass

    #   #
    def base_requests(self, method, url, data=None, file_var=None, file_path=None, header=None):
        """
                 : Param method: request method
                 : Param URL: Interface Path
                 : PARAM DATA: Data, please enter the string of DICT style
                 : param file_path: Uploaded file path
                 : param file_var: Parameter name of receiving file objects in the interface
                 : param header: request head
                 : return: Complete Response Object
        """
        session = requests.Session()
        if (file_var in [None, '']) and (file_path in [None, '']):
            files = None
        else:
            #
            files = {file_var: open(file_path, 'rb')}
            # GET Request Parameter Transfer Form Params
        if method == 'get':
            res = session.request(method=method, url=url, params=data, headers=header)
        else:
            res = session.request(method=method, url=url, data=data, files=files, headers=header)
            Logger.info(f
            'request method: {method}, request path: {url}, request parameters: {data}, request file: {files}, request head: {header})')
            return res.json()

    # !/usr/bin/env/python3
    # -*- coding:utf-8 -*-
    """
@project: apiAutoTest
@author: zy7y
@file: read_data.py
@ide: PyCharm
@time: 2020/7/31
"""
    import json

    import jsonpath
    import xlrd
    from xlutils.copy import copy
    from loguru import logger

    class ReadData(object):
        def __init__(self, excel_path):
            self.excel_file = excel_path
            self.book = xlrd.open_workbook(self.excel_file)

        def get_data(self):
            """
        :return:
        """
            data_list = []
            title_list = []

            table = self.book.sheet_by_index(0)
            for norw in range(1, table.nrows):
                #
                if Table.cell_Value(Norw, 3) == 'No':
            continue
            #   3rd column 3, the title is taken alone
            title_list.append(table.cell_value(norw, 1))

            # Returns all cells of the line consisting of data table.row_values ​​(0) 0 represents column 1
            case_number = table.cell_value(norw, 0)
            path = table.cell_value(norw, 2)
            is_token = table.cell_value(norw, 4)
            method = table.cell_value(norw, 5)
            file_var = table.cell_value(norw, 6)
            file_path = table.cell_value(norw, 7)
            dependent = table.cell_value(norw, 8)
            data = table.cell_value(norw, 9)
            expect = table.cell_value(norw, 10)
            actual = table.cell_value(norw, 11)
            value = [case_number, path, is_token, method, file_var, file_path, dependent, data, expect, actual]
            logger.info(value)
            #     To convert each line into a tuple storage, cater to Pytest's parameterized operation, if you don't need to comment out Value = tuple (Value)
            value = tuple(value)
            data_list.append(value)

        return data_list, title_list

    def write_result(self, case_number, result):
        """
             : param case_number: Sample number: case_001
             : Param Result: The response value that needs to be written
    :return:
    """
        row = int(case_number.split('_')[1])
        Logger.info('Started back to write actual response results into the use case data.')

    result = json.dumps(result, ensure_ascii=False)
    new_excel = copy(self.book)
    ws = new_excel.get_sheet(0)
    # 11 is the number of columns in Excel actually responding to the result column - 1
    ws.write(row, 11, result)
    new_excel.save(self.excel_file)
    Logger.info(F
    ') is completed: - Write file: {self.excel_file}, line number: {row + 1}, list number: 11, write value: {result}')

    # Read the actual response
    def read_actual(self, depend):
        """
             : param nrow: List
             : param depend: Relying on data dictionary format, front use case number, followed by extracting JSONPATH expressions for the corresponding field
    {"case_001":["$.data.id",],}
    :return:
    """
        depend = json.loads(depend)
        # Dictionary used to rely on data
        depend_dict = {}
        for k, v in depend.items():
            # Get the line number
            norw = int(k.split('_')[1])
            table = self.book.sheet_by_index(0)
            # Get the response of the corresponding row, # 11 is the number of columns in the actual response result column in Excel-1
            actual = json.loads(table.cell_value(norw, 11))
            try:
                for i in v:
                    logger.info(f'i {i}, v {v}, actual {actual} \n {type(actual)}')
                    depend_dict[i.split('.')[-1]] = jsonpath.jsonpath(actual, i)[0]
            except TypeError as e:
                Logger.Error(f
                'actual response results cannot be used normally to extract any content, discovering abnormal {E}')
                return depend_dict
        # !/usr/bin/env/python3
        # -*- coding:utf-8 -*-
        """
@project: apiAutoTest
@author: zy7y
@file: test_api.py
@ide: PyCharm
@time: 2020/7/31
"""
        import json
        import shutil

        import jsonpath
        from loguru import logger
        import pytest
        import allure
        from api.base_requests import BaseRequest
        from tools.read_config import ReadConfig
        from tools.read_data import ReadData

        rc = ReadConfig()
        base_url = rc.read_serve_config('dev')
        token_reg, res_reg = rc.read_response_reg()
        case_data_path = rc.read_file_path('case_data')
        report_data = rc.read_file_path('report_data')
        report_generate = rc.read_file_path('report_generate')
        log_path = rc.read_file_path('log_path')
        report_zip = rc.read_file_path('report_zip')
        email_setting = rc.read_email_setting()

        data_list, title_ids = ReadData(case_data_path).get_data()

        br = BaseRequest()
        token_header = {}
        no_token_header = {}

        class TestApiAuto(object):

            def start_run_test(self):
                import os
                if os.path.exists('../report') and os.path.exists('../log'):
                    shutil.rmtree(path='../report')
                    shutil.rmtree(path='../log')
                logger.add(log_path)

                pytest.main(args=[f'--alluredir={report_data}'])
                # # Start a report of a web service
                # os.system('allure serve ./report/data')
                os.system(f'allure generate {report_data} -o {report_generate} --clean')
                Logger.debug('report has been generated ")

        def treating_data(self, is_token, dependent, data):
            if is_token == '':
                header = no_token_header
            else:
                header = token_header
                # Logger.info(F
                # 'Data Data: {DATA}')
                if dependent != '':
                    dependent_data = ReadData(case_data_path).read_actual(dependent)
                    # Logger.debug(f
                    # 'Dependent Data Resolution Dictionary {Dependent_data}')
                    if data != '':
                        #     a new DATA
                        dependent_data.update(json.loads(data))
                        data = dependent_data
                        Logger.debug(F'DATA has data, depending on data, {data} ')
                else:
                    #
                    data = dependent_data
                    Logger.debug(F'DATA has no data, depending on data {data} ')
            # else:
                if data == '':
                    data = None
                    # Logger.debug(FODATA has no data, depending
                    # on
                    # no
                    # data
                    # {data}
                    # ')
                else:
                    data = json.loads(data)
                    Logger.debug(F'DATA has data, depending on {data} ')
            return data, header

            @pytest.mark.parametrize('case_number,path,is_token,method,file_var,'
                                     'file_path,dependent,data,expect,actual', data_list, ids=title_ids)
        def test_main(self, case_number, path, is_token, method, file_var, file_path,
                          dependent, data, expect, actual):

                with allure.step("Processing related data dependencies, header"):
                    data, header = self.treating_data(is_token, dependent, data)
                with allure.step("Send Request, JSON String"):
                    res = br.base_requests(method=method, url=base_url + path, file_var=file_var, file_path=file_path,
                                       data=data, header=header)
                with allure.step("The actual result bar" in 'the content of the response results'):
                    ReadData(case_data_path).write_result(case_number, res)
                #   ten The interface must be correct to return to TOKEN
                if is_token == 'write':
                    with allure.step("Extract token to Header from the response after login"):
                        token_header['Authorization'] = jsonpath.jsonpath(res, token_reg)[0]
                logger.info(f'token_header: {token_header}, \n no_token_header: {no_token_header}')
                with allure.step("Actual Data is extracted according to the Profile Extract Rule"):
                    really = jsonpath.jsonpath(res, res_reg)[0]
                with allure.step("Expected Result Results for Processing"):
                    expect = eval(expect)
                with allure.step("Expected Results and actual response to assert operation"):
                    assert really == expect

                Logger.info(f'full JSON response: {res} \ n Requires data dictionary: {really} \ n expected data dictionary: {EXPECT} \ n test results: {really == Expect}')
if __name__ == '__main__':
    from tools.zip_file import zipDir
    from tools.send_email import send_email
    t1 = TestApiAuto()
    t1.start_run_test()
    zipDir(report_generate, report_zip)
    send_email(email_setting)