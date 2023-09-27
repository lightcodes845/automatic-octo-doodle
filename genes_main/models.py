from django.db import models

# Create your models here.
class Assembly(models.Model):
    accession_id = models.CharField(max_length=50)
    class Meta:
        db_table = 'assembly'

class Gene(models.Model):
    gene_id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=50)
    stable_id = models.CharField(max_length=50)
    class Meta:
        db_table = 'gene'

class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, related_name='regions')
    class Meta:
        db_table = 'region'

class Transcript(models.Model):
    transcript_id = models.IntegerField(primary_key=True)
    stable_id = models.CharField(max_length=50)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE, related_name='transcripts')
    class Meta:
        db_table = 'transcript'

class TranscriptLocation(models.Model):
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE, related_name='locations')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='locations')
    start = models.IntegerField()
    end = models.IntegerField()

    class Meta:
        db_table = 'transcript_location'
