# coding=utf-8

import csv

RAW_RECORD = 'to_be_replaced.csv'  ## 填写你下载的文件名称，需要包括 .csv 后缀
CLEANED_RECORD = RAW_RECORD.split('.')[0] + '_cleaned.csv'

def clean_csv(input, output):
    with open(input, encoding='gbk') as f, open(output, 'w') as o:
        lines = f.readlines() ## 注意这行代码会一次性读取整个文件，若文件非常大时不推荐使用
        lines = lines[4:-7] ## 去掉开头结尾非 CSV 的内容
        lines = [line.replace(' ', '') for line in lines] ## 去掉空格
        o.writelines(lines)

def analyze_income_expense(record):
    """统计支出和收入的总和
    """
    pass

def analyze_max_expense_item(record):
    """统计花费最高的事项
    """
    pass


def analyze_max_expense_date(record):
    """统计花费最多的是哪一天
    """
    pass


if __name__ == "__main__":
    clean_csv(RAW_RECORD, CLEANED_RECORD)
    analyze_income_expense(CLEANED_RECORD)
    analyze_max_expense_item(CLEANED_RECORD)
    analyze_max_expense_date(CLEANED_RECORD)
