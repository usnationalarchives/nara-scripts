import csv
import xml.etree.ElementTree as ET

tree = ET.parse('MD.xml')
root = tree.getroot()
state = root.get('state')

f = open('1940 Census - ' + state + '_DAS.xml', 'a')
sequence_order = 1
f.write("""<?xml version="1.0" encoding="utf-8"?>
<itemArray>""")
for county in root:
	if county.tag == 'county-summary':
		countyname = str(county.get('name'))
		parent_file_unit = '1940 Census - ' + state + ' - ' + countyname
		with open('1940Census_fileUnitNaIds.csv', 'r') as log :
			readfile = csv.reader(log, delimiter= ',')
			for row in readfile:
				if row[1] == parent_file_unit:
					parent_file_unit_naid = row[0]
		
		for subcounty in county:
			if subcounty.tag == 'ed-summary':
				ed = str(subcounty.get('ed'))
				
				digital_objects = ''
				for images in subcounty:
					if images.tag == 'T1224-description':
						scope_and_content = images.text
					if images.tag == 'T627-files':
						for file in images.iter('image'):
							filename = str(file.get('filename'))
							digital_objects = digital_objects + """			<digitalObject>
				<objectType>
					<termName>Image (JPG)</termName>
				</objectType>
				<labelFlag>""" + filename + """</labelFlag>
				<accessFilename></accessFilename>
				<accessFileSize></accessFileSize>
				<thumbnailFilename>http://media.nara.gov/dc-metro/jpg_t.jpg</thumbnailFilename>
				<thumbnailFileSize>1234</thumbnailFileSize>
			</digitalObject>
"""
	
				DASxml_Top = """
	<item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		<sequenceOrder>""" + str(sequence_order) + """</sequenceOrder>
		<title>""" + parent_file_unit + """ - ED """ + ed + """</title>
		<scopeAndContentNote>""" + scope_and_content + """</scopeAndContentNote>
		<parentFileUnit>
			<parentFileUnitTitle>""" + parent_file_unit + """</parentFileUnitTitle>
			<naId>""" + parent_file_unit_naid + """</naId>
		</parentFileUnit>
		<generalRecordsTypeArray>
			<generalRecordsType>
				<termName>Textual Records</termName>
			</generalRecordsType>
		</generalRecordsTypeArray>
		<dataControlGroup>
			<groupCd>RDTP1</groupCd>
			<groupId>ou=RDTP1,ou=groups</groupId>
		</dataControlGroup>
		<accessRestriction>
			<status>
				<termName>Unrestricted</termName>
			</status>
		</accessRestriction>
		<useRestriction>
			<status>
				<termName>Unrestricted</termName>
			</status>
		</useRestriction>
		<physicalOccurrenceArray>
			<itemPhysicalOccurrence>
				<copyStatus>
					<termName>Preservation-Reproduction-Reference</termName>
				</copyStatus>
				<referenceUnitArray>
					<referenceUnit>
						<termName>National Archives at Washington, DC - Textual Reference</termName>
					</referenceUnit>
				</referenceUnitArray>
				<locationArray>
					<location>
						<facility>
							<termName>National Archives Building - Archives I (Washington, DC)</termName>
						</facility>
					</location>
				</locationArray>
				<mediaOccurrencearray>
					<mediaOccurrence>
						<specificMediaType>
							<termName>Paper</termName>
						</specificMediaType>
						<generalMediaTypeArray>
							<generalMediaType>
								<termName>Loose Sheets</termName>
							</generalMediaType>
						</generalMediaTypeArray>
					</mediaOccurrence>
				</mediaOccurrencearray>
			</itemPhysicalOccurrence>
		</physicalOccurrenceArray>
		<digitalObjectArray>
"""
				
				DASxml_Bottom = """		</digitalObjectArray>
	</item>
"""

				f.write(DASxml_Top + digital_objects + DASxml_Bottom)
				sequence_order = sequence_order + 1
f.write('</itemArray>')
f.close()