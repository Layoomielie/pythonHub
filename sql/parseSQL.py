#!/usr/bin/python3.7
# -*- coding : utf-8 -*-
# coding: utf-8
# author：  张鸿建
import os
import sqlparse
from elasticsearch import Elasticsearch, helpers


# 1.分割SQL


class parseSQL():
    # sql = '''
    # delete from t_subject_option
    # where c_subject_id
    # in (
    # select c_id from t_paper_subject
    # where C_PAPER_ID
    # in ('297ee5926d0acfaa016d1605b12a2f7b','297ee5926d0acfaa016d1605b2212fc1'))
    # '''
    sql = ''
    path = 'E:\sql'
    identifier = ''
    queryFlag = 0
    fieldValueList = []
    fieldValueLine = None
    hits = None
    queryField = ''
    paramField = ''
    queryTermsBody = {'query': {'terms': {}}}
    queryTermBody = {'query': {'term': {}}}
    isBool = False
    isTerm = True
    BoolBody = []
    termPattern = {"term": {

    }}
    termsPattern = {"terms": {
        "$field": {
            "value": []
        }
    }}
    es = Elasticsearch(['10.100.23.92:9200'])

    def readSql(self):
        fileList = os.listdir(self.path)
        for file in fileList:
            filePath = self.path + '/' + file
            print("当前正在读取 " + filePath + " 文件")
            with open(filePath, "r") as f:
                self.sql += f.read()

    def splitSql(self):
        stmts = sqlparse.split(self.sql.lower())
        print("当前一共解析到 " + str(len(stmts)) + " 条sql")
        for stmt in stmts:
            # 2.format格式化
            # print(sqlparse.format(stmt, reindent=True, keyword_case="upper"))
            # 3.解析SQL
            if (stmt.strip() == ''):
                continue
            # print(stmt)
            stmt_parsed = sqlparse.parse(stmt)
            tokens1 = stmt_parsed[0].tokens
            for token1 in reversed(tokens1):
                if (token1.value != ''):
                    self.parseMethod(token1)

    def parseWhere(self, tokenParam):
        tokens = tokenParam.tokens
        # print('where解析开始')
        for token in reversed(tokens):
            if (str(token.value).strip() != ''):
                # print(type(token))
                # print(token.value)
                self.parseMethod(token)
        # print('where解析完成')

    def formatField(self, field):
        fields = field[2:].split("_")
        flag = 0
        fieldValue = ''
        for f in fields:
            if (flag != 0):
                f = f.capitalize()
            fieldValue += f
            flag += 1
        return fieldValue

    def query_to_es(self):
        fieldValueList = self.fieldValueList
        if (self.fieldValueLine == None):
            # print("fieldValueList: "+str(fieldValueList))
            self.queryTermsBody = {'query': {'terms': {}}}
            # self.queryTermsBody['size']=100queryField
            self.queryTermsBody['query']['terms'][self.queryField] = fieldValueList
            count = self.es.count(index=self.table, body=self.queryTermsBody)
            # print("当前count为：" + str(count['count']))
            self.queryTermsBody['size'] = count['count']
            print(self.queryTermsBody)
            result = self.es.search(index=self.table, body=self.queryTermsBody)
            print("当前查询出index: " + self.table + " " + str(count['count']) + "条数据")
        else:
            self.queryTermBody = {'query': {'term': {}}}
            self.queryTermBody['query']['term'][self.queryField] = self.fieldValueLine
            count = self.es.count(index=self.table, body=self.queryTermBody)
            # print("当前count为：" + str(count['count']))
            self.queryTermBody['size'] = count['count']
            print(self.queryTermBody)
            result = self.es.search(index=self.table, body=self.queryTermBody)
            print("当前查询出index: " + self.table + " " + str(count['count']) + "条数据")
        # print("table: "+self.table)
        hits = result['hits']['hits']
        self.hits = hits

    def delete_to_es(self):
        fieldValueList = self.fieldValueList
        if (self.fieldValueLine == None):
            # print("fieldValueList: " + str(fieldValueList))
            self.queryTermsBody = {'query': {'terms': {}}}
            # self.queryTermsBody['size']=100
            self.queryTermsBody['query']['terms'][self.queryField] = fieldValueList
            print(self.queryTermsBody)
            result = self.es.delete_by_query(index=self.table, body=self.queryTermsBody)
            print("当前删除了Index: " + self.table + " " + str(result['deleted']) + "条数据")
        else:
            self.queryTermBody = {'query': {'term': {}}}
            self.queryTermBody['query']['term'][self.queryField] = self.fieldValueLine
            print(self.queryTermBody)
            result = self.es.delete_by_query(index=self.table, body=self.queryTermBody)
            print("当前删除了Index: " + self.table + " " + str(result['deleted']) + "条数据")
        # print("table: " + self.table)

    def parseMethod(self, token):
        if (isinstance(token, sqlparse.sql.Where)):
            # print(token.value)
            self.parseWhere(token)
            # tokens=self.fieldValueList.tokens
            # for token in tokens:
            # print(token.value)

        elif (isinstance(token, sqlparse.sql.Identifier)):
            field = token.value.lower()
            if (field.startswith('t_')):
                self.table = field[2:]
            elif (field.startswith('c_')):
                fieldValue = self.formatField(field)
                if (self.hits != None):
                    # print("当前hit解析出 " + str(len(self.hits)) + "个结果")
                    self.fieldValueList = []
                    self.fieldValueLine = None
                    for hit in self.hits:
                        # print(hit['_source'])
                        self.fieldValueList.append(hit['_source'][self.paramField])
                if (self.queryFlag == 0):
                    queryField = fieldValue
                    if (self.fieldValueList == None):
                        self.termPattern['term'] = {queryField: self.fieldValueLine}
                    else:
                        self.termsPattern['terms'] = {queryField: self.fieldValueList}
                elif (self.queryFlag == 1):
                    self.paramField = fieldValue
            else:
                print('pass')
                pass
        elif (isinstance(token, sqlparse.sql.IdentifierList)):
            for t in token.tokens:
                if (t.value != ','):
                    field = t.value.replace("'", "")
                    self.fieldValueList.append(field)
        elif (isinstance(token, sqlparse.sql.Parenthesis)):
            tokens = token.tokens[1:-1]
            for t in reversed(tokens):
                if (str(t.value).strip() != ''):
                    self.parseMethod(t)
                    # print(type(t))
                    # print(t.value)
        elif (isinstance(token, sqlparse.sql.Comparison)):
            # print(token.value)
            # print(token.left)
            # print(token.right)
            field = self.formatField(token.left.value)
            self.queryField = field
            fieldValueLine = token.right.value
            self.fieldValueLine = str(fieldValueLine).replace('"', '').replace('\'', '')

        elif (isinstance(token, sqlparse.sql.Token)):
            if (str(token.value).strip() != ''):
                if (str(token.value).find('select') != -1):
                    self.queryFlag = 0
                    # print(token.value)
                    # print('开始查询es')
                    # print(self.queryField)
                    # print(self.table)
                    self.query_to_es()
                elif (str(token.value).find('delete') != -1):
                    self.queryFlag = 0
                    # print('开始删除es')
                    # print(self.queryField)
                    # print(self.table)
                    self.delete_to_es()
                elif (str(token.value).find('where') != -1):
                    self.queryFlag = 1
                elif (str(token.value).find('and') != -1):
                    if (self.isTerm):
                        self.BoolBody.append(queryField)
                    self.isBool = True


if __name__ == '__main__':
    print("----------------------------start----------------------------")
    parseSQL = parseSQL()
    parseSQL.readSql()
    parseSQL.splitSql()
    print("-----------------------------end-----------------------------")
