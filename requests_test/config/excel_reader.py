# coding = utf-8
import xlrd
from requests_test.model.request_model import RequestModel


class ExcelReader:
    def reader(self):
        models_list = []
        wb = xlrd.open_workbook('../data/case.xlsx')
        names = wb.sheet_names()
        for sheet_name in names:
            sheet = wb.sheet_by_name(sheet_name)
            for i in range(sheet.nrows):
                if i == 0:
                    continue
                smart_list = []
                for j in range(sheet.ncols):
                    smart_list.append(sheet.cell_value(i, j))
                model = RequestModel()
                model.url = smart_list[0]
                model.desc = smart_list[1]
                model.method = smart_list[2]
                model.headers = smart_list[3]
                model.data = smart_list[4]
                model.assert_data = smart_list[5]
                model.assert_options = smart_list[6]
                model.assert_value = smart_list[7]
                model.extract = smart_list[8]
                model.is_need = smart_list[9]
                model.last_value = smart_list[10]
                model.req_param_type = smart_list[11]
                models_list.append(model)
        return models_list


if __name__ == '__main__':
    reader = ExcelReader()
    reader.reader()