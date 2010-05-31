#!/usr/bin/python

# This file generated by a program. do not edit.
import EUtils.POM

#     
#                 This is the Current DTD for Entrez eInfo
# $Id: eInfo_020511.dtd 94706 2006-12-04 21:51:33Z olegh $
# 
#  ================================================================= 
class DbName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class Name(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class FullName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Description(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class TermCount(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class Menu(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class DbTo(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class MenuName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Count(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class LastUpdate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class ERROR(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class IsDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class IsNumerical(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class SingleToken(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class Hierarchy(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class IsHidden(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  (Y|N) 
class DbList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'DbName', u'+')], ''))


class Field(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Name', ''), (u'FullName', ''), (u'Description', ''), (u'TermCount', ''), (u'IsDate', ''), (u'IsNumerical', ''), (u'SingleToken', ''), (u'Hierarchy', ''), (u'IsHidden', '')], ''))


class Link(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Name', ''), (u'Menu', ''), (u'Description', ''), (u'DbTo', '')], ''))


class LinkList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Link', u'*')], ''))


class FieldList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Field', u'*')], ''))


class DbInfo(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'DbName', ''), (u'MenuName', ''), (u'Description', ''), (u'Count', ''), (u'LastUpdate', ''), (u'FieldList', ''), (u'LinkList', u'?')], ''))


class eInfoResult(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u'|', [(u'DbList', ''), (u'DbInfo', ''), (u'ERROR', '')], ''))

