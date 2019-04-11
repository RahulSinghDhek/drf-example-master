from django.db import models

# Create your models here.

from django.db import models,transaction

class Share(models.Model):
    name = models.CharField(
        verbose_name=("name"),
        max_length=128,
        unique=True,
        null=False,
        blank=False,
        db_index=True,
    )
    created_at = models.DateTimeField(
        verbose_name=("created at"),
        auto_now_add=True,
    )
    hostname = models.CharField(
        verbose_name=("hostname"),
        max_length=128,
        null=True,
        blank=True,
    )
    export_path = models.TextField(
        verbose_name=("export path"),
        null=True,
        blank=True,
    )
    function_name = models.CharField(
            verbose_name=("function name"),
            max_length=128,
            null=True,
            blank=True,
    )

    # class Meta:
    #     db_table = 'share'
    #     managed = False
    #     verbose_name = ("share")
    #     verbose_name_plural = ("shares")
    #     ordering = ('name',)

    def get_lite_info(self):
        return {'id': self.id, 'name': self.name, 'share_path': self.export_path, 'function_name': self.function_name}