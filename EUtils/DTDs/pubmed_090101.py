#!/usr/bin/python

# This file generated by a program. do not edit.
import EUtils.POM

#     
# 	   This is the Current DTD which NLM has written for 
#         External  Use.  If you are a NCBI User, use the information
#         from the PubmedArticleSet.
# 
#         Comments and suggestions are welcome.
#         (May 9, 2000)
# 	
#         Corrections:
#         ~~~~~~~~~~~
#         Oct. 09 2002 
#         - "PubMedArticle" has been renamed to "PubmedArticle"
#         - All referencies to "PubMedArticle" has been removed
#         - "ProviderId" has been removed from PubmedData
#         - "URL" has been removed from PubmdeData
# 		
# 		$Id: pubmed_090101.dtd 145539 2008-11-13 16:08:35Z korobtch $
#         
#        
#  ================================================================= 
#  ================================================================= 
#  Reference to Where the MEDLINECITATION DTD is located  
#  NLMMedline DTD              
# 
#      Comments and suggestions are welcome.
#      January 1, 2009 v.3
# 
#      **THIS IS THE FORTHCOMING DTD FOR 2009 NOT CURRENTLY IN USE.  
#      SEE http://www.nlm.nih.gov/databases/dtd/nlmmedline_080101.dtd FOR THE 
#      NLMMEDLINE DTD DATED JANUARY 1, 2008 CURRENTLY IN USE.**  
#             
#      This is the DTD which the U.S. National Library of Medicine 
#      has written for External Use.        
#      If you are a data Licensee, the data are found in 
#      MedlineCitationSet.       
#  
#      NOTE:  The use of "Medline" in a DTD or element name does not mean the record 
#      represents a citation from a Medline-selected journal.  When the NLM DTDs and 
#      XML elements were first created, MEDLINE records were the only data exported. 
#      Now NLM exports citations other than MEDLINE records using these tools. To 
#      minimize unnecessary disruption to users of the data and tools, NLM has
#      retained the original DTD and element names (e.g., NLMMedline DTD, MedlineTA,
#      MedlineJournalInfo)).       
#        
#   * = 0 or more occurrences (optional element, repeatable)
#   ? = 0 or 1 occurrences (optional element, at most 1)
#   + = 1 or more occurrences (required element, repeatable)
#   | = choice, one or the other but not both 
#   no symbol = required element
# 
#  ================================================================= 
#    NLMMedline DTD   
#  Typical usage:   
# 
#   <!DOCTYPE MedlineCitationSet PUBLIC "-//NLM//DTD NLM Medline//EN">
# 
# 
#  ================================================================= 
#    Revision Notes Section 
# 
# The following changes were made in the nlmmedline_090101.dtd:
#   
#        a.  Changed entity reference from "nlmmedlinecitation_080101.dtd"
#            to: "nlmmedlinecitation_090101.dtd"
# 
#        b.  CHANGE WITHDRAWN FOR V.2: Delete entity NlmDcmsID.Ref and
#            NlmDcmsID element
# 
#        c.  FOR V.3: Added GrantCountry.Ref entity
#         
#      Historic Revision notes for previous versions of NLMMedline DTD 
#      See:
#      http://www.nlm.nih.gov/databases/dtd/history_dtd_nlmmedline.html
# 
#  ================================================================= 
#   external DTD entities                        
#  ================================================================= 
#  Reference to Where the NLM MedlineCitation DTD is located  
#  NLMMedlineCitation DTD   
#      
#      Comments and suggestions are welcome.
#      January 1, 2009 v.2
# 
#      **THIS IS THE FORTHCOMING DTD FOR 2009 NOT CURRENTLY IN USE.  
#      SEE http://www.nlm.nih.gov/databases/dtd/nlmmedlinecitation_080101.dtd FOR THE 
#      NLMMEDLINECITATION DTD DATED JANUARY 1, 2008 CURRENTLY IN USE.**  
#                
#    NOTE:  The use of "Medline" in a DTD or element name does not mean the record 
#     represents a citation from a Medline-selected journal.  When the NLM DTDs and 
#     XML elements were first created, MEDLINE records were the only data exported. 
#     Now NLM exports citations other than MEDLINE records using these tools. To 
#     minimize unnecessary disruption to users of the data and tools, NLM has
#     retained the original DTD and element names (e.g., NLMMedline DTD, MedlineTA,
#     MedlineJournalInfo)).       
#        
#   * = 0 or more occurrences (optional element, repeatable)
#   ? = 0 or 1 occurrences (optional element, at most 1)
#   + = 1 or more occurrences (required element, repeatable)
#   | = choice, one or the other but not both 
#   no symbol = required element
# 
#  ================================================================= 
#    Revision Notes Section 
# 
# The following changes were made in the nlmmedlinecitation_090101.dtd:
# 
#      a. Changed entity reference from "nlmsharedcatcit_080101.dtd" 
#              to: "nlmsharedcatcit_090101.dtd" 
#      
#      b. Moved entity Type to nlmcommon dtd
# 
#      c. Added NLM value to entity Source
#  
#      d. CHANGE WITHDRAWN FOR V.2: Delete entity NlmDcmsID.Ref
#    
#   
#      Historic Revision notes for previous versions of NLMMedlineCitation DTD
#      See:
#      http://www.nlm.nih.gov/databases/dtd/history_dtd_medlinecitation.html
# 
#  
#  ================================================================= 
#  external DTD entities 
#  ================================================================= 
#  internal DTD entities 
#  ================================================================= 
#  ================================================================= 
#  Reference to Where the NLM Common DTD via NLMSharedCatCit DTD is located  
#  NLMSharedCatCit DTD
# 
#      Comments and suggestions are welcome.
#      January 1, 2009
# 
#      **THIS IS THE FORTHCOMING DTD FOR 2009 NOT CURRENTLY IN USE.  
#      SEE http://www.nlm.nih.gov/databases/dtd/nlmsharedcatcit_080101.dtd FOR THE 
#      NLMSHAREDCATCIT DTD DATED JANUARY 1, 2008 CURRENTLY IN USE.**  
#   
#      This is the DTD for data elements that are shared between 
#      NLMCatalogRecord and NLMMedlineCitation DTDs at the 
#      U.S. National Library of Medicine. 
#      
#     NOTE:  The use of "Medline" in a DTD or element name does not mean the record 
#     represents a citation from a Medline-selected journal.  When the NLM DTDs and 
#     XML elements were first created, MEDLINE records were the only data exported. 
#     Now NLM exports citations other than MEDLINE records using these tools. To 
#     minimize unnecessary disruption to users of the data and tools, NLM has
#     retained the original DTD and element names (e.g., NLMMedline DTD, MedlineTA,
#     MedlineJournalInfo)).       
#   
#   * = 0 or more occurrences (optional element, repeatable)
#   ? = 0 or 1 occurrences (optional element, at most 1)
#   + = 1 or more occurrences (required element, repeatable)
#    | = choice, one or the other but not both 
#   no symbol = required element
# 
#  ================================================================= 
#    Revision Notes Section 
# 
# The following changes were made in the nlmsharedcatcit_090101.dtd:
#      
#      a.  Changed entity reference from "nlmcommon_080101.dtd"
#                       to "nlmcommon_090101.dtd"
# 
#      b.  Moved OtherAbstract element from nlmsharedcatcit dtd to
#          nlmcommon dtd
#     
#     Historic Revision notes for previous versions of NLMSharedcatcit DTD
#      See:
#      http://www.nlm.nih.gov/databases/dtd/history_dtd_nlmsharedcatcit.html
# 
# 
#  ====================================================================== 
#  internal DTD entities 
#  ====================================================================== 
#  ====================================================================== 
#  Reference to Where the NLMCommon DTD is located  
#  NLMCommon DTD
# 
#      Comments and suggestions are welcome.
#      January 1, 2009 v.2
# 
#      **THIS IS THE FORTHCOMING DTD FOR 2009 NOT CURRENTLY IN USE.  
#      SEE http://www.nlm.nih.gov/databases/dtd/nlmcommon_080101.dtd FOR THE 
#      NLMCOMMON DTD DATED JANUARY 1, 2008 CURRENTLY IN USE.**  
#              
#      This is the DTD for data elements that are shared 
#      among various applications at the U.S. National Library of Medicine. 
#  
#     NOTE:  The use of "Medline" in a DTD or element name does not mean the record 
#     represents a citation from a Medline-selected journal.  When the NLM DTDs and 
#     XML elements were first created, MEDLINE records were the only data exported. 
#     Now NLM exports citations other than MEDLINE records using these tools. To 
#     minimize unnecessary disruption to users of the data and tools, NLM has
#     retained the original DTD and element names (e.g., NLMMedline DTD, MedlineTA,
#     MedlineJournalInfo)).       
# 
#   * = 0 or more occurrences (optional element, repeatable)
#   ? = 0 or 1 occurrences (optional element, at most 1)
#   + = 1 or more occurrences (required element, repeatable)
#    | = choice, one or the other but not both 
#   no symbol = required element
# 
#     NLMCommon.dtd
# 
#         Document Type Definition for the PubMed Article DTD
#         $Id: nlmcommon_090101.dtd 145539 2008-11-13 16:08:35Z korobtch $
# 
#  ====================================================================== 
#    Revision Notes Section
#     
#     The following changes were made in the nlmcommon_090101.dtd:
#     
#      a. Added ValidYN attribute to Investigator element
#             
#      b. Moved OtherAbstract element from nlmsharedcatcit to nlmcommon dtd
# 
#      c. Added OtherAbstract element to NCBIArticle element
# 
#      d. Moved entity Type from nlmmedlinecitation to nlmcommon dtd
#  
#      e. Added Publisher value to entity Type 
#      
#      f. Deleted Consumer value from entity Type 
# 
#      g. Added Country element to Grant element
#   
#      h. FOR V.2: Changed Country value to GrantCountry.Ref in Grant element
#  
#                 
#      Historic Revision notes for previous versions of NLMCommon DTD
#      See:
#      http://www.nlm.nih.gov/databases/dtd/history_dtd_nlmcommon.html
# 
#  ================================================================= 
#      internal DTD entities             
#  ================================================================= 
#  ================================================================= 
#  This is the top level element for NCBIArticle 
class NCBIArticle(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'PMID', ''), (u'Article', ''), (u'MedlineJournalInfo', ''), (u'InvestigatorList', u'?'), (u'OtherAbstract', u'?')], ''))


#  ================================================================= 
#  This is the top level element for Article 
class Article(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'|', [(u'Journal', ''), (u'Book', '')], ''), (u'ArticleTitle', ''), (u'|', [(u',', [(u'Pagination', ''), (u'ELocationID', u'*')], ''), (u'ELocationID', u'+')], ''), (u'Abstract', u'?'), (u'Affiliation', u'?'), (u'AuthorList', u'?'), (u'Language', u'+'), (u'DataBankList', u'?'), (u'GrantList', u'?'), (u'PublicationTypeList', ''), (u'VernacularTitle', u'?'), (u'ArticleDate', u'*')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('PubModel', ['Print', 'Print-Electronic', 'Electronic', 'Electronic-Print'], 11, None)])


#  ================================================================= 
#   Further Definitions of NLM Tags                                  
class Abstract(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'AbstractText', ''), (u'CopyrightInformation', u'?')], '')], ''))


class AbstractText(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class AccessionNumber(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class AccessionNumberList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'AccessionNumber', u'+')], ''))


class Acronym(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Affiliation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Agency(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ArticleDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'Year', ''), (u'Month', ''), (u'Day', ''), (u',', [(u'Hour', ''), (u',', [(u'Minute', ''), (u'Second', u'?')], u'?')], u'?')], '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('DateType', 1, 14, u'Electronic')])


class ArticleTitle(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Author(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [('', [(u'|', [(u',', [(u'LastName', ''), (u'|', [(u'ForeName', ''), (u',', [(u'FirstName', ''), (u'MiddleName', u'?')], '')], u'?'), (u'Initials', u'?'), (u'Suffix', u'?')], ''), (u'CollectiveName', '')], '')], ''), (u'Affiliation', u'?'), (u'DatesAssociatedWithName', u'?'), (u'NameQualifier', u'?'), (u'OtherInformation', u'?'), (u'TitleAssociatedWithName', u'?')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('ValidYN', ['Y', 'N'], 13, u'Y')])


class AuthorList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Author', u'+')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('CompleteYN', ['Y', 'N'], 13, u'Y')])


class Book(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'PubDate', ''), (u'Publisher', ''), (u'Title', ''), (u'AuthorList', u'?'), (u'CollectionTitle', u'?'), (u'Volume', u'?')], ''))


class BroadJournalHeading(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class BroadJournalHeadingList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'BroadJournalHeading', u'+')], ''))


class Coden(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class CollectionTitle(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class CollectiveName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class CopyrightInformation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Country(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Coverage(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class DataBank(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'DataBankName', ''), (u'AccessionNumberList', u'?')], ''))


class DataBankList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'DataBank', u'+')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('CompleteYN', ['Y', 'N'], 13, u'Y')])


class DataBankName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class DateIssued(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class DatesAssociatedWithName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class DatesOfSerialPublication(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Day(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class DescriptorName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('MajorTopicYN', ['Y', 'N'], 13, u'N')])


class Edition(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ELocationID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('EIdType', ['doi', 'pii'], 11, None), EUtils.POM.XMLAttribute('ValidYN', ['Y', 'N'], 13, u'Y')])


class EndPage(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class FirstName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ForeName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Frequency(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('FrequencyType', ['Current', 'Former'], 13, u'Current')])


class Grant(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'GrantID', u'?'), (u'Acronym', u'?'), (u'Agency', ''), (u'Country', u'?')], ''))


class GrantID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class GrantList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Grant', u'+')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('CompleteYN', ['Y', 'N'], 13, u'Y')])


class Hour(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Imprint(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Initials(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Investigator(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u',', [(u'LastName', ''), (u'|', [(u'ForeName', ''), (u',', [(u'FirstName', ''), (u'MiddleName', u'?')], '')], u'?'), (u'Initials', u'?'), (u'Suffix', u'?')], ''), (u'Affiliation', u'?')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('ValidYN', ['Y', 'N'], 13, u'Y')])


class InvestigatorList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Investigator', u'+')], ''))


class ISOAbbreviation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ISSN(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('IssnType', ['Electronic', 'Print', 'Undetermined'], 11, None)])


class ISSNLinking(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Issue(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Journal(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'ISSN', u'?'), (u'JournalIssue', ''), (u'Coden', u'?'), (u'Title', u'?'), (u'ISOAbbreviation', u'?')], ''))


class JournalIssue(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Volume', u'?'), (u'Issue', u'?'), (u'PubDate', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('CitedMedium', ['Internet', 'Print'], 11, None)])


class Language(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class LastName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class MedlineDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class MedlineJournalInfo(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Country', u'?'), (u'MedlineTA', ''), (u'NlmUniqueID', u'?'), (u'ISSNLinking', u'?')], ''))


class MedlinePgn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class MedlineTA(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class MeshHeading(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'DescriptorName', ''), (u'QualifierName', u'*')], ''))


class MeshHeadingList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'MeshHeading', u'+')], ''))


class MiddleName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Minute(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Month(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class NameQualifier(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class NlmUniqueID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class OtherAbstract(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'AbstractText', ''), (u'CopyrightInformation', u'?')], '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Type', ['AAMC', 'AIDS', 'KIE', 'PIP', 'NASA', 'Publisher'], 11, None)])


class OtherInformation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Pagination(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u'|', [(u',', [(u'StartPage', ''), (u'EndPage', u'?'), (u'MedlinePgn', u'?')], ''), (u'MedlinePgn', '')], ''))


class Place(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('ImprintType', ['Current', 'Original'], 13, u'Current')])


class PlaceCode(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class PMID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ProjectedPublicationDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class PubDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'|', [(u',', [(u'Year', ''), (u'|', [(u',', [(u'Month', ''), (u'Day', u'?')], ''), (u'Season', '')], u'?')], ''), (u'MedlineDate', '')], '')], ''))


class PublicationEndYear(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class PublicationFirstYear(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class PublicationInfo(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Country', u'?'), (u'PlaceCode', u'?'), (u'Imprint', u'*'), (u'Place', u'*'), (u'Publisher', u'*'), (u'DateIssued', u'*'), (u'ProjectedPublicationDate', u'?'), (u'PublicationFirstYear', u'?'), (u'PublicationEndYear', u'?'), (u'Edition', u'?'), (u'DatesOfSerialPublication', u'*'), (u'Frequency', u'*')], ''))


class PublicationType(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class PublicationTypeList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'PublicationType', u'+')], ''))


class Publisher(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class QualifierName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('MajorTopicYN', ['Y', 'N'], 13, u'N')])


class Season(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Second(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class StartPage(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Suffix(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Title(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class TitleAssociatedWithName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class VernacularTitle(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Volume(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Year(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  ======================================================================= 
#   Further Definitions of NLM Tags                                        
class Chemical(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'RegistryNumber', ''), (u'NameOfSubstance', '')], ''))


class ChemicalList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Chemical', u'+')], ''))


class DateCompleted(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'Year', ''), (u'Month', ''), (u'Day', ''), (u',', [(u'Hour', ''), (u',', [(u'Minute', ''), (u'Second', u'?')], u'?')], u'?')], '')], ''))


class DateCreated(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'Year', ''), (u'Month', ''), (u'Day', ''), (u',', [(u'Hour', ''), (u',', [(u'Minute', ''), (u'Second', u'?')], u'?')], u'?')], '')], ''))


class DateRevised(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'Year', ''), (u'Month', ''), (u'Day', ''), (u',', [(u'Hour', ''), (u',', [(u'Minute', ''), (u'Second', u'?')], u'?')], u'?')], '')], ''))


class GeneralNote(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Owner', ['NLM', 'NASA', 'PIP', 'KIE', 'HSR', 'HMD', 'SIS', 'NOTNLM'], 13, u'NLM')])


class Keyword(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('MajorTopicYN', ['Y', 'N'], 13, u'N')])


class KeywordList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Keyword', u'+')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Owner', ['NLM', 'NASA', 'PIP', 'KIE', 'HSR', 'HMD', 'SIS', 'NOTNLM'], 13, u'NLM')])


class NameOfSubstance(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class OtherID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Prefix', 1, 12, None), EUtils.POM.XMLAttribute('Source', ['NASA', 'KIE', 'PIP', 'POP', 'ARPL', 'CPC', 'IND', 'CPFH', 'CLML', 'IM', 'SGC', 'NRCBL', 'QCICL', 'QCIM', 'NLM'], 11, None)])


class PersonalNameSubject(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u',', [(u'LastName', ''), (u'|', [(u'ForeName', ''), (u',', [(u'FirstName', ''), (u'MiddleName', u'?')], '')], u'?'), (u'Initials', u'?'), (u'Suffix', u'?')], ''), (u'DatesAssociatedWithName', u'?'), (u'NameQualifier', u'?'), (u'OtherInformation', u'?'), (u'TitleAssociatedWithName', u'?')], ''))


class PersonalNameSubjectList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'PersonalNameSubject', u'+')], ''))


class RegistryNumber(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class SpaceFlightMission(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  =================================================================  
#  This is the top level element for MedlineCitation 
class MedlineCitation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'NlmDcmsID', u'?'), (u'PMID', ''), (u'DateCreated', ''), (u'DateCompleted', u'?'), (u'DateRevised', u'?'), (u'Article', ''), (u'MedlineJournalInfo', ''), (u'ChemicalList', u'?'), (u'CitationSubset', u'*'), (u'CommentsCorrections', u'?'), (u'GeneSymbolList', u'?'), (u'MeshHeadingList', u'?'), (u'NumberOfReferences', u'?'), (u'PersonalNameSubjectList', u'?'), (u'OtherID', u'*'), (u'OtherAbstract', u'*'), (u'KeywordList', u'*'), (u'SpaceFlightMission', u'*'), (u'InvestigatorList', u'?'), (u'GeneralNote', u'*')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Owner', ['NLM', 'NASA', 'PIP', 'KIE', 'HSR', 'HMD', 'SIS', 'NOTNLM'], 13, u'NLM'), EUtils.POM.XMLAttribute('Status', ['Completed', 'In-Process', 'PubMed-not-MEDLINE', 'In-Data-Review', 'Publisher', 'MEDLINE', 'OLDMEDLINE'], 11, None)])


#  End of MedlineCitation group 
#  ================================================================= 
#              Further Definition of NLM Tags         
class CitationSubset(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class CommentIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class CommentOn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class CommentsCorrections(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'CommentOn', u'*'), (u'CommentIn', u'*'), (u'ErratumIn', u'*'), (u'ErratumFor', u'*'), (u'PartialRetractionIn', u'*'), (u'PartialRetractionOf', u'*'), (u'RepublishedFrom', u'*'), (u'RepublishedIn', u'*'), (u'RetractionOf', u'*'), (u'RetractionIn', u'*'), (u'UpdateIn', u'*'), (u'UpdateOf', u'*'), (u'SummaryForPatientsIn', u'*'), (u'OriginalReportIn', u'*'), (u'ReprintOf', u'*'), (u'ReprintIn', u'*')], ''))


class ErratumFor(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class ErratumIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class GeneSymbol(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class GeneSymbolList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'GeneSymbol', u'+')], ''))


class NlmDcmsID(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Note(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class NumberOfReferences(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class OriginalReportIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class PartialRetractionIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class PartialRetractionOf(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class RefSource(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ReprintIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class ReprintOf(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class RepublishedFrom(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class RepublishedIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class RetractionIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class RetractionOf(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class SummaryForPatientsIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class UpdateIn(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


class UpdateOf(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'RefSource', ''), (u'PMID', u'?'), (u'Note', u'?')], '')], ''))


#  ================================================================= 
#  ================================================================= 
class DeleteCitation(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'PMID', u'+')], ''))


class MedlineCitationSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'MedlineCitation', u'*'), (u'DeleteCitation', u'?')], ''))


#  ================================================================= 
#  ================================================================= 
#  ================================================================= 
class PubmedArticleSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'PubmedArticle', '')], u'+'))


#  ================================================================= 
#  This is the top level element for PubMedArticle 
class PubmedArticle(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'|', [(u'NCBIArticle', ''), (u'MedlineCitation', '')], ''), (u'PubmedData', u'?')], ''))


#  ================================================================= 
class PubmedData(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'History', u'*'), (u'PublicationStatus', ''), (u'ArticleIdList', ''), (u'ObjectList', u'?')], ''))


class History(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'PubMedPubDate', u'+')], ''))


class PubMedPubDate(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u',', [(u'Year', ''), (u'Month', ''), (u'Day', ''), (u',', [(u'Hour', ''), (u',', [(u'Minute', ''), (u'Second', u'?')], u'?')], u'?')], '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('PubStatus', ['received', 'accepted', 'epublish', 'ppublish', 'revised', 'aheadofprint', 'retracted', 'pmc', 'pmcr', 'pubmed', 'pubmedr', 'premedline', 'medline', 'medliner', 'entrez', 'pmc-release'], 11, None)])


class PublicationStatus(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ArticleIdList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'ArticleId', u'+')], ''))


class ArticleId(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('IdType', ['doi', 'pii', 'pmcpid', 'pmpid', 'pmc', 'mid', 'sici', 'pubmed', 'medline', 'pmcid'], 13, u'pubmed')])


class URL(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('lang', ['AF', 'AR', 'AZ', 'BG', 'CS', 'DA', 'DE', 'EN', 'EL', 'ES', 'FA', 'FI', 'FR', 'HE', 'HU', 'HY', 'IN', 'IS', 'IT', 'IW', 'JA', 'KA', 'KO', 'LT', 'MK', 'ML', 'NL', 'NO', 'PL', 'PT', 'PS', 'RO', 'RU', 'SL', 'SK', 'SQ', 'SR', 'SV', 'SW', 'TH', 'TR', 'UK', 'VI', 'ZH'], 12, None), EUtils.POM.XMLAttribute('Type', ['FullText', 'Summary', 'fulltext', 'summary'], 12, None)])


class ObjectList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Object', '')], u'+'))


class Object(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Param', '')], u'*'))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Type', 1, 11, None)])


class Param(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('Name', 1, 11, None)])


#  ================================================================= 