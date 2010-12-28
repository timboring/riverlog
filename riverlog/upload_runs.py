import csv
import datetime

import models


def process_file(file):
	"""Process an uploaded file.

	Args:
		file: an UploadFile object
		(see http://docs.djangoproject.com/en/dev/topics/http/file-uploads/?from=olddocs#handling-uploaded-files)

		expected format of the uploaded file:
		date,
		put-on time,
		take-out time, 
		river, 
		section, 
		usgs level, 
		bridge gauge, 
		24-hr rain, 
		12-hr rain, 
		air temp (f),
		air temp (c), 
		notes
	"""
	reader = csv.reader(file, delimiter=',')
	saved = 0
	errors = 0
	#import pdb;pdb.set_trace()
	for row in reader:
		if row[0] == 'date':
			continue
		else:
			run = models.Run(
					date=_convert_date(row[0]),
					river=row[3])

			try:
				run.put_on_time = _convert_time(row[1])
			except IndexError:
				run.put_on_time = None

			try:
				run.take_out_time = _convert_time(row[2])
			except IndexError:
				run.take_out_time = None
				
			try:
				run.section = row[4] 
			except IndexError:
				run.section = None

			try:
				run.usgs_level = _sanitize_decimals(row[5])
			except IndexError:
				run.usgs_level = None

			try:
				run.bridge_gauge = _sanitize_decimals(row[6])
			except IndexError:
				run.bridge_gauge = None

			try:
				run.notes = row[11]
			except IndexError:
				run.notes = None

			try:
				run.save()
				saved += 1
			except:
				errors += 1

	return {'saved': saved, 'errors': errors}


def _sanitize_decimals(s):
	"""Sanitize decimal inputs.

	Args:
		s: str, typically something like '2,000.00'
	Returns:
		str or None
	"""
	if s == '':
		return None
	return s.replace(',', '')


def _convert_date(strDate):
	"""Convert a string to a datetime.Date object.

	Args:
		strDate: str, a date string in formate YYYY-MM-DD
	Returns:
		datetime.date object
	"""
	(year, month, day) = strDate.split('-')
	return datetime.date(int(year), int(month), int(day))


def _convert_time(t):
	"""Convert a string to a datetime.Time object.

	Args:
		t: str, a time string in format HH:MM[:SS]
	Returns:
		datetime.time object
	"""
	if t == '':
		return None

	if len(t) == 3:
		hour = t[0]
		minute = t[1:]
	else:
		hour = t[0:2]
		minute = t[2:]
	new_time = datetime.time(int(hour), int(minute))
	return new_time
