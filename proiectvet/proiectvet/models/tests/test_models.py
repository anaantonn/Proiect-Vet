"""
Tests for the models module.
"""
from django.test import TestCase

from proiectvet.models.rasa import Rasa
from proiectvet.models.specie import Specie


class ModelTests(TestCase):
    """
    Test case for the models.
    """
    def setUp(self):
        self.specie = Specie.objects.create(
            nume="Bovina",
            protected=False,
        )

    def test_create_specie(self):
        """Test create specie is successful."""
        self.assertEqual(str(self.specie), self.specie.nume)

    def test_create_rasa(self):
        """Test create rasa is successful."""
        rasa = Rasa.objects.create(
            nume="BNR",
            id_specie=Specie.objects.get(nume="Bovina"),
            protected=False,
        )
        self.assertEqual(str(rasa), rasa.nume)
        self.assertEqual(rasa.id_specie, Specie.objects.get(nume="Bovina"))
