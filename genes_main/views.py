from pprint import pprint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Gene
from .serializers import GeneSerializer

# Create your views here.
class GeneSymbolQuery(APIView):

    def get(self, request):

        # Get the gene symbol from the request
        gene_symbol = request.query_params.get("gene_symbol", None)

        # If no gene symbol was provided, return an error
        if gene_symbol is None or str(gene_symbol) == "":
            return Response({"error": "No gene symbol provided"}, status=status.HTTP_400_BAD_REQUEST)


        # Query the database for information about the genes with a matching symbol
        genes = Gene.objects.filter(symbol=gene_symbol).prefetch_related('transcripts')

        # Serialize the data
        gene_serializer = GeneSerializer(genes, many=True)

        # Return the results in a structured JSON format
        return Response(gene_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Get the gene symbol from the request
        gene_symbol = request.data.get("gene_symbol", None)

        if gene_symbol is None:
            return Response({"error": "No gene symbol provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Query the database for information about the genes with a matching symbol
        genes = Gene.objects.filter(symbol=gene_symbol).prefetch_related('transcripts')

        # Serialize the data
        gene_serializer = GeneSerializer(genes, many=True)

        # Return the results in a structured JSON format
        return Response(gene_serializer.data, status=status.HTTP_200_OK)