from django.db import models,transaction

# Create your models here.

from shares.models import Share

class ActionJobsShares(models.Model):
    share = models.ForeignKey(
        Share,
        db_index=True,
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        'ActionJob',
        db_index=True,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'jobs_shares'
        managed = False

class ActionJobManager(models.Manager):

    # @transaction.atomic
    # def create(self, shares, **validated_data):
    #     action_job = super().create(**validated_data)
    #     action_job.attach_shares(shares)
    #     return action_job

    def select_all_related(self):
        return self.prefetch_related(
            'shares',
        )
class ActionJob(models.Model):

    objects = ActionJobManager()
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
    comments = models.CharField(
        verbose_name=("comments"),
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    shares = models.ManyToManyField(
        Share,
        through=ActionJobsShares,
        verbose_name=("shares"),
        related_name="jobs",
        related_query_name="jobs",
    )

    def set_shares(self, *shares):
        share_ids = [share.id for share in shares]
        self.shares.clear()
        # Set new shares
        ActionJobsShares.objects.bulk_create(
            [ActionJobsShares(job=self, share=share) for share in shares])




