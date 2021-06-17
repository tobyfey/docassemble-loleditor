from docassemble.base.core import DAObject, DAList, DADict, DASet, DAOrderedDict
from docassemble.base.util import get_config
from docassemble.base.functions import word
from docassemble.base.legal import *
from .airtable import Airtable


def get_airtable_api(table_name):
	api_key=get_config('airtable api key')
	base_key=get_config('airtable base key')
	api_response = Airtable(base_key, table_name, api_key)
	return api_response


class Application(DAObject):
	def ___init___(self, *pargs, **kwargs):
		self.initializeAttribute('specific_factors', SFDict.using(object_type=SF))
		self.initializeAttribute('match_dict', MatchAll.using(object_type=MatchDict.using(object_type=Match)))
		self.initializeAttribute('issues', IssueObjectList.using(object_type=IssueObject))
		self.initializeAttribute('legal_objects', LegalObjectList.using(object_type=LegalObject))
		self.initializeAttribute('facts', Facts)
		return super(Application, self).init(*pargs, **kwargs)
		
	def __unicode__(self):
		return self.name

class SFDict(DADict):
	def ___init___(self, *pargs, **kwargs):
		return super(SFDict, self).init(*pargs, **kwargs)
		
class SF(DASet):
	def ___init___(self, *pargs, **kwargs):
		return super(SF, self).init(*pargs, **kwargs)

class IssueObject(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(IssueObject, self).init(*pargs, **kwargs)
		
	def __str__(self):
		return self.name

class IssueObjectList(DAList):
	def ___init___(self, *pargs, **kwargs):
		return super(IssueObjectList, self).init(*pargs, **kwargs)


class LegalObject(DAObject):
	def ___init___(self, *pargs, **kwargs):
		self.initializeAttribute('legal_elements', LegalObjectList.using(object_type=LegalObject,ask_number=True))
		self.initializeAttribute('fact_objects', FactObjectList.using(object_type=FactObject))
		return super(LegalObject, self).init(*pargs, **kwargs)
	
	def __unicode__(self):
		return self.name

class LegalObjectList(DAList):
	def ___init___(self, *pargs, **kwargs):
		return super(LegalObjectList, self).init(*pargs, **kwargs)
	
	def __unicode__(self):
		return self.name

class FactObject(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(FactObject, self).init(*pargs, **kwargs)

class FactObjectList(DAList):
	def ___init___(self, *pargs, **kwargs):
		return super(FactObjectList, self).init(*pargs, **kwargs)

class Step(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(Step, self).init(*pargs, **kwargs)

class Option(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(Option, self).init(*pargs, **kwargs)

class Law_Link(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(Law_Link, self).init(*pargs, **kwargs)

class ChangeObject(DAObject):
	def ___init___(self, *pargs, **kwargs):
		return super(ChangeObject, self).init(*pargs, **kwargs)
		
