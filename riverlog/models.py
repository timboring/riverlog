from django.db import models

# Create your models here.
class Run(models.Model):
	date = models.DateField()
	put_on_time = models.DateTimeField(blank=True, null=True)
	take_out_time = models.DateTimeField(blank=True, null=True)
	river = models.CharField(max_length=80)
	section = models.CharField(max_length=50, blank=True, null=True)
	usgs_level = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	bridge_gauge = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
	notes = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return '[%s] %s, %s (level: %s)' % (
			self.date, self.river, self.section, self.bridge_gauge)
