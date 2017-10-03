#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Linq(list):


    def Where(self, where = None):
        wheres = Linq()
        for e in self:
            if where(e):
                wheres.append(e)
        return wheres

    def Select(self, select  = None):
        selects = Linq()
        for e in self:
            selects.append(e)
        return selects

    def Skip(self, skip):
        skips = Linq()
        for e in self:
            if 0 < skip:
                skip = skip - 1
            else:
                skips.append(e)
        return skips

    def Take(self, take):
        takes = Linq()
        for e in self:
            if 0 < take:
                takes.append(e)
                take = take - 1
            else:
                break
        return takes

    def All(self, all = None):
        for e in self:
            if not all(e):
                return False
        return True

    def Any(self, any = None):
        for e in self:
            if any(e):
                return True
        return False

    


# func=Noneのとき集合すべてを返す それ以外の時はlambda(無名関数)の引数にitemを入れたものを返すぞ
def _act(func, item):
    return item if func is None else func(item)


# test
linq1 = Linq([1])
linq2 = Linq([1, 1, 2, 3, 5])
linq3 = Linq(['Hello', 'null', 'World'])
linq4 = Linq([1, 1, 1, 1])
print(linq1.Where(lambda x: x % 2 == 1))
print(linq2.Where(lambda x: x % 5 == 1))
print(linq3.Where(lambda x: x != 'null'))
print(linq2.Any(lambda x: x == 4 ))
print(linq2.Skip(2)
           .Where(lambda x: x % 3 == 0))




