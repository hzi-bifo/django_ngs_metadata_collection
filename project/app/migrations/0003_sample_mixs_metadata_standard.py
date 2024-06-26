# Generated by Django 5.0.4 on 2024-04-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_sample_metadata_a_remove_sample_metadata_b_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='mixs_metadata_standard',
            field=models.CharField(blank=True, choices=[('Agriculture', 'Agriculture'), ('Air', 'Air'), ('BuiltEnvironment', 'Built Environment'), ('FoodAnimalAndAnimalFeed', 'Food Animal and Animal Feed'), ('FoodFarmEnvironment', 'Food Farm Environment'), ('FoodFoodProductionFacility', 'Food Production Facility'), ('FoodHumanFoods', 'Human Foods'), ('HostAssociated', 'Host Associated'), ('HumanAssociated', 'Human Associated'), ('HumanGut', 'Human Gut'), ('HumanOral', 'Human Oral'), ('HumanSkin', 'Human Skin'), ('HumanVaginal', 'Human Vaginal'), ('HydrocarbonResourcesCores', 'Hydrocarbon Resources Cores'), ('HydrocarbonResourcesFluidsSwabs', 'Hydrocarbon Resources Fluids Swabs'), ('MicrobialMatBiofilm', 'Microbial Mat Biofilm'), ('MiscellaneousNaturalOrArtificialEnvironment', 'Miscellaneous Natural or Artificial Environment'), ('PlantAssociated', 'Plant Associated'), ('Sediment', 'Sediment'), ('Soil', 'Soil'), ('SymbiontAssociated', 'Symbiont Associated'), ('WastewaterSludge', 'Wastewater Sludge'), ('Water', 'Water')], max_length=100, null=True),
        ),
    ]
