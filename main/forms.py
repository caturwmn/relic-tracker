from django.forms import ModelForm
from main.models import Relic

class RelicForm(ModelForm):
    class Meta:
        model = Relic
        fields = ["name", "amount", "description", "best_rarity", 
                  "ideal_main_stat", "ideal_variant_amount"]