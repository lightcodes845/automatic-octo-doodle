from pprint import pprint
import pytest
from rest_framework import status
from model_bakery import baker
from genes_main.models import Gene, Transcript

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_gene_query_exists_returns_200_and_data(self, api_client):
        # Arrange
        transcript_quantity = 3
        gene = baker.make(Gene)
        baker.make(Transcript, gene=gene, _quantity=transcript_quantity)

        # Act
        response = api_client.get(f'/api/genequery/?gene_symbol={gene.symbol}')

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['gene_id'] == gene.gene_id
        assert response.data[0]['symbol'] == gene.symbol
        assert response.data[0]['stable_id'] == gene.stable_id
        assert len(response.data[0]['transcripts']) == transcript_quantity

    def test_if_gene_query_does_not_exist_returns_200_and_empty_list(self, api_client):
        # Arrange
        gene_symbol = 'FakeGene'

        # Act
        response = api_client.get(f'/api/genequery/?gene_symbol={gene_symbol}')

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    def test_if_no_gene_symbol_provided_returns_400(self, api_client):
        # Arrange
        gene_symbol = ""

        # Act
        response = api_client.get(f'/api/genequery/?gene_symbol={gene_symbol}')

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'error': 'No gene symbol provided'}
