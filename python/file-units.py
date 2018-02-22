import csv, xml

file_unit = open('test2.csv', 'r')
output_xml = 'output.xml'

csvReader = csv.reader(file_unit)
header = next(csvReader)
dataControlGroup = header.index('dataControlGroup')
parentSeriesNaid = header.index('parentSeriesNaid')
title = header.index('title')
containerId = header.index('containerId')
scopeAndContentNote = header.index('scopeAndContentNote')
accessRestrictionStatus = header.index('accessRestrictionStatus')
specificAccessRestriction = header.index('specificAccessRestriction')
securityClassification = header.index('securityClassification')
accessRestrictionNote = header.index('accessRestrictionNote')
useRestrictionStatus = header.index('useRestrictionStatus')
specificUseRestriction = header.index('specificUseRestriction')
useRestrictionNote = header.index('useRestrictionNote')
generalRecordsType = header.index('generalRecordsType')
copyStatus = header.index('copyStatus')
specificMediaType = header.index('specificMediaType')
generalMediaType = header.index('generalMediaType')

sequence_order = 1

print 'Creating DAS XML...'

with open(output_xml, 'a') as outfile:
	outfile.write('<import xmlns="http://ui.das.nara.gov/"><fileUnitArray>')
	
for row in csvReader:
	data_control_group = row[dataControlGroup]
	if data_control_group == '':
		print 'Blank dataControlGroup found in line ' + str(csvReader.line_num)
		data_control_group = '[DATA CONTROL GROUP REQUIRED]'
		reference_unit = '[REFERENCE UNIT REQUIRED]'
		location = '[LOCATION REQUIRED]'
		ou_group = '[OU GROUP REQUIRED]'
	if data_control_group == 'LL':
		reference_unit = 'Center for Legislative Archives'
		location = 'National Archives Building - Archives I (Washington, DC)'
		ou_group = 'NWL'
	if data_control_group == 'LM':
		reference_unit = 'Presidential Materials Division'
		location = 'National Archives Building - Archives I (Washington, DC)'
		ou_group = 'NLMS'
	if data_control_group == 'LPBHO':
		reference_unit = 'Barack Obama Presidential Library'
		location = 'Barack Obama Presidential Library (Hoffman Estates, IL)'
		ou_group = 'LPBHO'
	if data_control_group == 'LPDDE':
		reference_unit = 'Dwight D. Eisenhower Library'
		location = 'Dwight D. Eisenhower Library (Abilene, KS)'
		ou_group = 'NLDDE'
	if data_control_group == 'LPFDR':
		reference_unit = 'Franklin D. Roosevelt Library'
		location = 'Franklin D. Roosevelt Library (Hyde Park, NY)'
		ou_group = 'NLFDR'
	if data_control_group == 'LPGB':
		reference_unit = 'George Bush Library'
		location = 'George Bush Library (College Station, TX)'
		ou_group = 'NLGB'
	if data_control_group == 'LPGWB':
		reference_unit = 'George W. Bush Library'
		location = 'George W. Bush Library (Lewisville, TX)'
		ou_group = 'NLGWB'
	if data_control_group == 'LPGRF':
		reference_unit = 'Gerald R. Ford Library'
		location = 'Gerald R. Ford Library (Ann Arbor, MI)'
		ou_group = 'NLGRF'
	if data_control_group == 'LPHH':
		reference_unit = 'Herbert Hoover Library'
		location = 'Herbert Hoover Library (West Branch, IA)'
		ou_group = 'NLHH'
	if data_control_group == 'LPHST':
		reference_unit = 'Harry S. Truman Library'
		location = 'Harry S. Truman Library (Independence, MO)'
		ou_group = 'NLHST'
	if data_control_group == 'LPJC':
		reference_unit = 'Jimmy Carter Library'
		location = 'Jimmy Carter Library (Atlanta, GA)'
		ou_group = 'NLJC'
	if data_control_group == 'LPJFK':
		reference_unit = 'John F. Kennedy Library'
		location = 'John F. Kennedy Library (Boston, MA)'
		ou_group = 'NLJFK'
	if data_control_group == 'LPLBJ':
		reference_unit = 'Lyndon B. Johnson Library'
		location = 'Lyndon Baines Johnson Library (Austin, TX)'
		ou_group = 'NLLBJ'
	if data_control_group == 'LPRN':
		reference_unit = 'Richard Nixon Library'
		location = 'Richard Nixon Library (Yorba Linda, CA)'
		ou_group = 'NLRN'
	if data_control_group == 'LPRR':
		reference_unit = 'Ronald Reagan Library'
		location = 'Ronald Reagan Library (Simi Valley, CA)'
		ou_group = 'NLRR'
	if data_control_group == 'LPWJC':
		reference_unit = 'William J. Clinton Library'
		location = 'William J. Clinton Library (Little Rock, AR)'
		ou_group = 'NLWJC'
	if data_control_group == 'RDF':
		reference_unit = 'National Archives at College Park - FOIA'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'RDF'
	if data_control_group == 'RDSC':
		reference_unit = 'National Archives at College Park - Cartographic'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'NWCS-C'
	if data_control_group == 'RDSM':
		reference_unit = 'National Archives at College Park - Motion Pictures'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'NWCS-M'
	if data_control_group == 'RDSS':
		reference_unit = 'National Archives at College Park - Still Pictures'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'NWCS-S'
	if data_control_group == 'RDTP1':
		reference_unit = 'National Archives at Washington, DC - Textual Reference'
		location = 'National Archives Building - Archives I (Washington, DC)'
		ou_group = 'RDTP1'
	if data_control_group == 'RDTP2':
		reference_unit = 'National Archives at College Park, MD - Textual Reference'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'RDTP2'
	if data_control_group == 'RDEP':
		reference_unit = 'National Archives at College Park - Electronic Records'
		location = 'National Archives at College Park - Archives II (College Park, MD)'
		ou_group = 'NWME'
	if data_control_group == 'REAT':
		reference_unit = 'National Archives at Atlanta'
		location = 'NARA\'s Southeast Region (Atlanta, GA)'
		ou_group = 'NRCA'
	if data_control_group == 'REBO':
		reference_unit = 'National Archives at Boston'
		location = 'NARA\'s Northeast Region (Boston, MA)'
		ou_group = 'NRAAB'
	if data_control_group == 'RENY':
		reference_unit = 'National Archives at New York'
		location = 'NARA\'s Northeast Region (New York City, NY)'
		ou_group = 'NRAAN'
	if data_control_group == 'REPA':
		reference_unit = 'National Archives at Philadelphia'
		location = 'NARA\'s Mid Atlantic Region (Philadelphia, PA)'
		ou_group = 'NRBA'
	if data_control_group == 'RLSL':
		reference_unit = 'National Personnel Records Center - Military Personnel Records'
		location = 'National Military Personnel Records Center (St. Louis, MO)'
		ou_group = 'NRPA'
	if data_control_group == 'RMCH':
		reference_unit = 'National Archives at Chicago'
		location = 'NARA\'s Great Lakes Region (Chicago, IL)'
		ou_group = 'NRDA'
	if data_control_group == 'RMDV':
		reference_unit = 'National Archives at Denver'
		location = 'NARA\'s Rocky Mountain Region (Denver, CO)'
		ou_group = 'NRGA'
	if data_control_group == 'RMFW':
		reference_unit = 'National Archives at Fort Worth'
		location = 'NARA\'s Southwest Region (Fort Worth, TX)'
		ou_group = 'NRFA'
	if data_control_group == 'RMKC':
		reference_unit = 'National Archives at Kansas City'
		location = 'NARA\'s Central Plains Region (Kansas City, MO)'
		ou_group = 'NREA'
	if data_control_group == 'RWRS':
		reference_unit = 'National Archives at Riverside'
		location = 'NARA\'s Pacific Region (Riverside, CA)'
		ou_group = 'NRHAR'
	if data_control_group == 'RWSB':
		reference_unit = 'National Archives at San Francisco'
		location = 'NARA\'s Pacific Region (San Bruno, CA)'
		ou_group = 'NRHAS'
	if data_control_group == 'RWSE':
		reference_unit = 'National Archives at Seattle'
		location = 'NARA\'s Pacific Alaska Region (Seattle, WA)'
		ou_group = 'NRIAS'
		
	parent_series_naid = row[parentSeriesNaid]
	title2 = row[title]
	container_id = row[containerId]
	scope_and_content_note = row[scopeAndContentNote]
	access_restriction_status = row[accessRestrictionStatus]
	specific_access_restriction = row[specificAccessRestriction]
	security_classification = row[securityClassification]
	access_restriction_note = row[accessRestrictionNote]
	use_restriction_status = row[useRestrictionStatus]
	specific_use_restriction = row[specificUseRestriction]
	use_restriction_note = row[useRestrictionNote]
	general_records_type = row[generalRecordsType]
	copy_status = row[copyStatus]
	specific_media_type = row[specificMediaType]
	general_media_type = row[generalMediaType]
	
	if parent_series_naid == '':
		parent_series_naid = '[PARENT SERIES NAID REQUIRED]'
		print 'Blank parentSeriesNaid found in line ' + str(csvReader.line_num)
	if title2 == '':
		title2 = '[TITLE REQUIRED]'
		print 'Blank title found in line ' + str(csvReader.line_num)
	if access_restriction_status == '':
		access_restriction_status = '[ACCESS RESTRICTION STATUS REQUIRED]'
		print 'Blank accessRestrictionStatus found in line ' + str(csvReader.line_num)
	if use_restriction_status == '':
		use_restriction_status = '[USE RESTRICTION STATUS REQUIRED]'
		print 'Blank useRestrictionStatus found in line ' + str(csvReader.line_num)
	if general_records_type == '':
		general_records_type = '[GENERAL RECORDS TYPE REQUIRED]'
		print 'Blank generalRecordsType found in line ' + str(csvReader.line_num)
	if copy_status == '':
		copy_status = '[COPY STATUS REQUIRED]'
		print 'Blank copyStatus found in line ' + str(csvReader.line_num)
	if specific_media_type == '':
		specific_media_type = '[SPECIFIC MEDIA TYPE REQUIRED]'
		print 'Blank specificMediaType found in line ' + str(csvReader.line_num)
	if general_media_type == '':
		general_media_type = '[GENERAL MEDIA TYPE REQUIRED]'
		print 'Blank generalMediaType found in line ' + str(csvReader.line_num)
		
	das_xml = """<fileUnit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<sequenceOrder>""" + str(sequence_order) + """</sequenceOrder>
<title>""" + title2 + """</title>
<parentSeries><naId>""" + parent_series_naid + """</naId></parentSeries>
<generalRecordsTypeArray><generalRecordsType><termName>""" + general_records_type + """</termName></generalRecordsType></generalRecordsTypeArray>
<dataControlGroup><groupCd>""" + data_control_group + """</groupCd><groupId>ou=""" + ou_group + """,ou=groups</groupId></dataControlGroup>
<accessRestriction><status><termName>""" + use_restriction_status + """</termName></status></accessRestriction>
<useRestriction><status><termName>""" + access_restriction_status + """</termName></status></useRestriction>
<physicalOccurrenceArray><fileUnitPhysicalOccurrence>
<copyStatus><termName>""" + copy_status + """</termName> </copyStatus><referenceUnitArray><referenceUnit><termName>""" + reference_unit + """</termName> </referenceUnit></referenceUnitArray>
<locationArray><location><facility><termName>""" + location + """</termName> </facility></location></locationArray>
<mediaOccurrenceArray><mediaOccurrence><specificMediaType><termName>""" + specific_media_type + """</termName></specificMediaType>
<generalMediaTypeArray><generalMediaType><termName>""" + general_media_type + """</termName></generalMediaType></generalMediaTypeArray>
</mediaOccurrence></mediaOccurrenceArray>
</fileUnitPhysicalOccurrence></physicalOccurrenceArray>
</fileUnit>
"""

	f = open(output_xml, 'a')
	f.write(das_xml) 
	f.close()
	sequence_order = sequence_order + 1

with open(output_xml, 'a') as outfile:
	outfile.write('</fileUnitArray></import>')
	
print 'DAS XML complete!'