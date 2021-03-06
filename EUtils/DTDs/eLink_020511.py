#!/usr/bin/python

# This file generated by a program. do not edit.
import EUtils.POM

#     
#                 This is the Current DTD for Entrez eLink
# $Id: eLink_020511.dtd 56256 2005-02-18 17:13:40Z olegh $
# 
#  ================================================================= 
class ERROR(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Info(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Id(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('HasLinkOut', ['Y', 'N'], 12, None), EUtils.POM.XMLAttribute('HasNeighbor', ['Y', 'N'], 12, None)])


#  \d+ 
class Score(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \d+ 
class DbFrom(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class DbTo(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class LinkName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class IdList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Id', u'*')], ''))


#  cmd=neighbor 
class Link(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Id', ''), (u'Score', u'?')], ''))


class LinkSetDb(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'DbTo', ''), (u'LinkName', ''), (u'|', [(u'Link', u'*'), (u'Info', '')], ''), (u'ERROR', u'?')], ''))


#  cmd=links 
class Url(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class IconUrl(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class SubjectType(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Attribute(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class Name(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  .+ 
class NameAbbr(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  \S+ 
class Provider(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Name', ''), (u'NameAbbr', ''), (u'Id', ''), (u'Url', ''), (u'IconUrl', u'?')], ''))


class ObjUrl(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Url', ''), (u'IconUrl', u'?'), (u'LinkName', u'?'), (u'SubjectType', u'*'), (u'Attribute', u'*'), (u'Provider', '')], ''))


class IdUrlSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Id', ''), (u'|', [(u'ObjUrl', u'+'), (u'Info', '')], '')], ''))


class IdUrlList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'IdUrlSet', u'*'), (u'ERROR', u'?')], ''))


#  cmd=ncheck & lcheck 
class IdCheckList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Id', u'*'), (u'ERROR', u'?')], ''))


#  Common 
class LinkSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'DbFrom', ''), (u'|', [(u',', [(u'IdList', u'?'), (u'LinkSetDb', u'*')], ''), (u'IdUrlList', ''), (u'IdCheckList', ''), (u'ERROR', '')], '')], ''))


class eLinkResult(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'LinkSet', u'*'), (u'ERROR', u'?')], ''))

