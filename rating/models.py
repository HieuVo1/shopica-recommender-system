from django.db import models


class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    like = models.IntegerField()
    dislike = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    accountId = models.TextField(blank=True, null=True, db_column="account_id")
    rating = models.IntegerField(blank=True, null=True)
    productId = models.TextField(blank=True, null=True, db_column="product_id")

    class Meta:
        managed = False
        db_table = 'comment'
