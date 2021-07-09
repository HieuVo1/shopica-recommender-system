from surprise import dump
from surprise import Reader, Dataset, SVD
from surprise.model_selection.validation import cross_validate
from .models import Comment
from django_pandas.io import read_frame
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'rating', 'productId', 'accountId']


def generate_model():

    comments = Comment.objects.filter(productId__isnull=False)
    commentsDf = read_frame(comments, fieldnames=[
                            'rating', 'productId', 'accountId'])

    reader = Reader()
    svd = SVD()
    ratingDf = Dataset.load_from_df(
        commentsDf[['accountId', 'productId', 'rating']], reader)

    cross_validate(svd, ratingDf, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    trainset = ratingDf.build_full_trainset()
    svd.fit(trainset)

    dump.dump('final_model.sav', predictions=None, algo=svd, verbose=0)
