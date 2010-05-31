#!/usr/bin/python

# This file generated by a program. do not edit.
import EUtils.POM

#  $Id: LinkOut.dtd,v 1.23 2007/09/20 21:21:56 timonin Exp $ 
#  LinkOut DTD version 1.1
#            
#      This document is still under revision and may change.
#      
#      Changes:
#      version 1.1:
#      - SubjectType and Attribute lists updated
#      - DTD is XML
#      version 1.6:
#      - <apad> tag added
#      
#      version sequence refreshed to 1.1 on 2001/09/20
#      
#      version 1.2:
#      - SubObjectSelector updated to 
#       
#      <!ELEMENT SubObjectSelector       (Database, SubProvider)>
#      
#      version 1.3:
#      - Entities added:  lo.name, lo.genus, lo.species, lo.subsp
# 
#      version 1.6:
#      - Entities added: lo.month, lo.authln 
#      
#      version 1.8:
#      - Entities added: lo.eyear, lo.eyr, lo.eyl, lo.emonth, lo.emon, lo.emo,
#                        lo.eday
#      version 1.11:
#      - added Attribute: preference
#      
#      version 1.12:
#      - dropped lo.muid
# 
#      version 1.16
# 	 - Entities added: lo.clusterid for UniGene
# 	 
# 	 version 1.22
# 	 - SubjectType added: locus-specific
#       
# 	 
#     
#  Typical usage:
# 
#         <!DOCTYPE LinkSet PUBLIC "-//NLM//DTD LinkOut//EN" "LinkOut.dtd">
#         <LinkSet>
#         ...
#          </LinkSet>
#             
#          or:
# 
#          <!DOCTYPE Provider PUBLIC "-//NLM//DTD LinkOut//EN" "LinkOut.dtd">
#          <Provider>
#          ...
#          </Provider>
# 
#     
# 
# 
#    Rule based URL generation. In general, to build the
#    URL both base and rule are required, where base is the
#    HTTP base address, for example:
# 
#        http://www.sciencemag.org/cgi/content/full/
# 
#    and rule is in the following format:
# 
#        &lo.vol;/&lo.iss;/&lo.page;
# 
#    LinkOut will replace the keywords in rule with the actual 
#    value for a retrieved citation. Therefore, rule will be 
#    translated into: 281/5384/1863
#    
#    The program will concatenate base with rule:
# 
#      http://www.sciencemag.org/cgi/content/full/281/5384/1863
# 
#    The following keywords are supported for any database:
# 
#      lo.id      - Unique identifier (PMID, GI, TaxID, etc.)
# 
#   For PubMed only: 
# 
#      lo.pii     - Publisher Item Identification. Must be submitted 
#      by the publisher. For example, 6847, in the PubMed DTD this 
#      ID is an attribute of the ArticleId element. 
# 
#      lo.doi     - Article DOI 
# 
#      lo.issn    - Journal ISSN code 
#      
#      lo.essn    - Journal Electronic ISSN code
# 
#      lo.issnl   - Journal ISSN code without the dash 
# 
#      lo.jtit    - Journal title (MEDLINE abbreviation) 
# 
#      lo.vol     - Volume 
# 
#      lo.iss     - Issue 
# 
#      lo.page    - First page 
# 
#      lo.year    - Four digit year.  For example, 1998 
# 
#      lo.yr      - Last two digit of year.  For example, 98; 00 
# 
#      lo.yl      - Last digit of year.  For example, for 1999 use 9;  
#      for 1990 use 0 
# 
#      lo.eyear    - Four digit year of electronic publication date.  For example, 1998 
# 
#      lo.eyr      - Last two digit of year of electronic publication date.  For example, 98; 00 
# 
#      lo.eyl      - Last digit of year of electronic publication date.  For example, for 1999 use 9;  
#      for 1990 use 0 
# 
#      lo.month  -  The month. For example, September
# 
#      lo.mon     - The 3 letter month abbreviation. For example, Sep 
# 
#      lo.mo      - Two digit month.  For example, 01; 12 
#      
#      lo.emonth  -  The month of electronic publication date. For example, September
# 
#      lo.emon     - The 3 letter month abbreviation of electronic publication date. For example, Sep 
# 
#      lo.emo      - Two digit month of electronic publication date.  For example, 01; 12 
#      
#      lo.day     - Two digit day. For example, 01; 31 
#      
#      lo.eday     - Two digit day of electronic publication date. For example, 01; 31 
# 
#      lo.otit    - Article title 
# 
#      lo.auth    - First author 
# 
#      lo.authln  - Last name of the first author
# 
# 
#   For Sequence databases (Nucleotide, Protein, Structure, Genome):
# 
#      lo.pacc    - Primary accession for sequences
#      
#   For Taxonomy only:
#   
#      lo.scientificname    - Full scientific name.  For example: "Homo sapiens neanderthalensis"
#      
#      lo.genus   - Genius name.  For example: "Homo"
#      
#      lo.species - Species epithet.  For example: "sapiens"
#      
#      lo.subsp   - Sub-species epithet.  For example: "neanderthalensis"
# 
#   For UniGene only:
# 
#   	lo.clusterid - Cluster Id
# 
# 
# 
#  Entities for special characters 
#  internal DTD entities 
class SubjectType(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  can be one of the following; see LinkOut SubjectTypes and Attributes 
#  at http://www.ncbi.nlm.nih.gov/books/bv.fcgi?rid=helplinkout.section.files.Special_Elements_Sub for a description 
#  of these elements: 
# 
# //CHEMICAL INFORMATION
#         Biological Properties
#         Chemical Libraries
#         Imaging Agents
#         Metabolism
#         Molecular Interactions
#         Physical Properties
#         Reactions
#         Theoretical Properties
#         Toxicology
#         Vendors
# 
# 
# //EDUCATION
#         conferences/meetings/workshops
#         glossaries/dictionaries
#         online tutorials/courses
# 
# //FUNDING SOURCES
#         funding sources
# 
# //LITERATURE
#         abstracts/indexes/summaries
#         aggregators
#         books
#         individual online article
#         images
#         libraries
#         patent databases
#         publishers/providers
# 
# //MEDICAL
#         clinical trials
#         consumer health
#         diagnostics
#         disease organizations
#         medical equipment and devices
#         pharmacology
#         treatment guidelines
# 
# //MOLECULAR BIOLOGY DATABASES
#         DNA/protein sequence
#         gene/protein/disease-specific
#         gene expression
# 		locus-specific
#         mapping
#         organism-specific
#         population/variation
#         protein interactions/pathways
#         structure
#         taxonomy/phylogenetic
# 
# //RESEARCH MATERIALS
#         clones/clone libraries
#         culture/stock collections
#         laboratory equipment
#         oligonucleotides
#         other reagents
# 
# //RESEARCHERS
#         colleges/universities
#         companies/research institutes
#         directories
#         individuals
#         societies/associations
# 
# //TOOLS
#         3D structure prediction/functional modeling
#         primer design
#         protein identification/characterization
#         restriction mapping
#         sequence screening/similarity/alignment
#         sequence viewer
#         translation
# 
# 
class Attribute(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  can be one of the following; see LinkOut SubjectTypes and Attributes 
#  at http://www.ncbi.nlm.nih.gov/books/bv.fcgi?rid=helplinkout.section.files.Special_Elements_Att for a description 
#  of these elements:
# //BARRIERS
#         registration required
#         subscription/membership/fee required
# 
# //OWNERSHIP
#         author of URL
#         publisher of information in URL
# 
# //Resource Form
#         author manuscript
#         electronic full-text
#         full-text online
#         full-text PDF
#         full-text PostScript
#         order form
#         print collection       
#         
# //Adminstrative
#         library-local
#         preference
#         
#         
# 
#  This is the top level element for Provider 
class Provider(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'ProviderId', ''), (u'Name', ''), (u'NameAbbr', ''), (u'SubjectType', u'*'), (u'Attribute', u'*'), (u'Url', u'*'), (u'IconUrl', u'*'), (u'Brief', u'?')], ''))


class ProviderId(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Name(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class NameAbbr(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class Url(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('LNG', ['DA', 'DE', 'EN', 'EL', 'ES', 'FR', 'IT', 'IW', 'JA', 'NL', 'NO', 'RU', 'SV', 'ZH'], 13, u'EN')])


class IconUrl(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('LNG', ['DA', 'DE', 'EN', 'EL', 'ES', 'FR', 'IT', 'IW', 'JA', 'NL', 'NO', 'RU', 'SV', 'ZH'], 13, u'EN')])


class Brief(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  End of Privider group 
class LinkSet(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [(u'Link', u'+')], ''))


class Link(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'LinkId', ''), (u'ProviderId', ''), (u'IconUrl', u'*'), (u'|', [(u'ObjectSelector', ''), (u'SubObjectSelector', '')], ''), (u'ObjectUrl', u'+')], ''))


class LinkId(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ObjectSelector(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Database', ''), (u'ObjectList', '')], ''))


class Database(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  All Entrez databases may be configured to include LinkOut.  Please write to
# linkout@ncbi.nlm.nih.gov for the current list of databases available for LinkOut 
class ObjectList(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u'|', [(u'FileName', ''), (u'Query', ''), (u'ObjId', '')], u'+'))


class FileName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('fieldname', 1, 11, None)])


#  FileName is reserved for processing by the LinkOut team 
class Query(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ObjId(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  End of ObjectList group 
#  End of ObjectSelector group 
#  Libraries must use SubObjectSelector to refer to the sub providers 
class SubObjectSelector(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Database', ''), (u'SubProvider', '')], ''))


class SubProvider(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'NameAbbr', ''), (u'|', [(u'InclQuery', ''), (u'ExclQuery', '')], u'*')], ''))


class InclQuery(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class ExclQuery(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  End of SubObjectSelector group 
class ObjectUrl(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'|', [(u',', [(u'Base', ''), (u'|', [(u'Rule', ''), (u'RuleToMany', '')], u'?')], ''), (u'|', [(u'Rule', ''), (u'RuleToMany', '')], '')], ''), (u'UrlName', u'?'), (u'SubjectType', u'*'), (u'Attribute', u'*')], ''))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('LNG', ['DA', 'DE', 'EN', 'EL', 'ES', 'FR', 'IT', 'IW', 'JA', 'NL', 'NO', 'RU', 'SV', 'ZH'], 13, u'EN')])


class Base(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class pad(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('with', 1, 11, None), EUtils.POM.XMLAttribute('width', 1, 11, None), EUtils.POM.XMLAttribute('align', ['left', 'right'], 13, u'right')])


#  used to mark up strings that require padding to create fixed-length string
#      attributes. 
#  with      a character to pad with (required)
#      width     result string size (required) (integer)
#      align     the text should align to (left|right) (default:right)
#      
class apad(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('with', 1, 11, None), EUtils.POM.XMLAttribute('width', 1, 11, None), EUtils.POM.XMLAttribute('align', ['left', 'right'], 13, u'right')])


#  used to mark up strings that require padding to create fixed-length string
#      attributes. It skips all preceding alpha characters before padding 
#  with      a character to pad with (required)
#      width     result string size (required) (integer)
#      align     the text should align to (left|right) (default:right)
#      Examples:
#      	<apad with = "0" width = "6">E32</apad>  => "E00032"
#      	<apad with = "0" width = "6">640</apad>  => "000640"
#      
class subs(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('for', 1, 11, None), EUtils.POM.XMLAttribute('with', 1, 11, None)])


#  substitute one string for another in the element's content
#      
#  for    the string to replace
#      with   the string to substitute
#      
class toupper(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))


#  convert element content into upper case 
class tolower(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))


#  convert element content into lower case 
class strip(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))
	ATTLIST = EUtils.POM.AttributeList([EUtils.POM.XMLAttribute('what', ['spaces', 'letters', 'nondigits', 'digits'], 11, None)])


#  strip off spaces/letters/digits in the element's content
# 	
class normalize(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))


#  are used for normalization of &lo.voll , &lo.iss; elements.
# 	Examples:
# 		"Pt 5" 			==> "5"
# 		"3 Suppl"		==> "3"
# 		"2A Pt 3"   		==> "2A"
# 		"10 Suppl 2 Pt 1"   	==> "10"
# 		"2/3"			==> "2"
# 	
class Rule(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('|', [('#PCDATA', ''), (u'pad', ''), (u'apad', ''), (u'subs', ''), (u'toupper', ''), (u'tolower', ''), (u'strip', ''), (u'normalize', '')], '*'))


class UrlName(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


class RuleToMany(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel((u',', [(u'Rule', ''), (u'Separator', '')], ''))


class Separator(EUtils.POM.ElementNode):
	CONTENTMODEL = EUtils.POM.ContentModel(('', [('#PCDATA', '')], ''))


#  End of ObjectUrl group 
#  End of Link group 
#  End of LinkSet group 