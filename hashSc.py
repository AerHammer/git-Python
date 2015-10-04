#coding : utf-8

'''
Это модуль который имеет функции для расчета хеш сумм
1.Md5 хэш - hasMd5()
2.sha1 хеш - hasSha1()
3.sha256 хеш - hasSha256()
4.sha512 хеш - hasSha512()
5.sha384 хеш - hasSha384()
6.sha224 хеш - hasSha224()

'''

__author__ = 'yorick'

import hashlib

# =========================================================================================
# Функции расчета хеш сумм
# =========================================================================================

def hasMd5(filename):

    '''
    расчитывает md5 хеш
    '''

    m = hashlib.md5()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha256(filename):

    '''
    расчитывает sha256 хеш
    '''

    m = hashlib.sha256()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha512(filename):

    '''
    расчитывает sha512 хеш
    '''

    m = hashlib.sha512()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha384(filename):

    '''
    расчитывает sha384 хеш
    '''
    m = hashlib.sha384()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha224(filename):

    '''
    расчитывает sha224 хеш
    '''

    m = hashlib.sha224()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()



def hasSha1(filename):

    '''
    расчитывает sha1 хеш
    '''

    m = hashlib.sha1()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()

