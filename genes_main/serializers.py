from rest_framework import serializers
from genes_main.models import Gene, Transcript


class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = ['transcript_id', 'stable_id',]

class GeneSerializer(serializers.ModelSerializer):
    transcripts = TranscriptSerializer(many=True)
    class Meta:
        model = Gene
        fields = ['gene_id', 'symbol', 'stable_id', 'transcripts']