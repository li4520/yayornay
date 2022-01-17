from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Cointoss_Results(models.Model):
    game_name = models.CharField(max_length=200, default="cointoss")
    total_cointoss_initiated = models.BigIntegerField(default=0)
    total_heads_count = models.BigIntegerField(default=0)
    total_tails_count = models.BigIntegerField(default=0)
    total_round_count = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id)
        # return self.game_name

    # def total_rps_initiated2(self):
    #     # return self.total_rps_initiated
    #     return '{0} ({1})'.format(self.id, self.total_rps_initiated, self.total_round_count)

    # def total_game_count(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

# Create your models here.

    # Metadata
    # class Meta:
        # ordering = ["-my_field_name"]
    # Methods
