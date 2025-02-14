# Primii pasi

python3 manage.py runserver\
python3 manage.py makemigrations\
python3 manage.py migrate

## Verifica CRUD din terminal

    python3 manage.py shell:
        from specie_rasa.models import Specie, Rasa
        specii = Specie.objects.all()
        rase = Rasa.objects.all()
        print(specii)
        print(rasa)

    Creaza noi specii si noi rase:
        Specie.objects.create(nume="Porc")
        Rasa.objects.create(nume="Duroc", id_specie=Specie.objects.get(id=4))

    Stegre speciile/rasele deja existente => Eroare:
        specie = Specie.objects.get(nume="Caine")
        specie.delete()
