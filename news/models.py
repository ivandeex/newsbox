from django.db.models import (Model, CASCADE, SET_NULL, CharField, TextField,
                              AutoField, IntegerField, SmallIntegerField, URLField,
                              ForeignKey, ManyToManyField)
from unixtimestampfield.fields import UnixTimeStampField
from django.utils.translation import ugettext_lazy as _


class Category(Model):
    cid = AutoField(primary_key=True)
    title = CharField(max_length=255)
    description = TextField()
    block = SmallIntegerField()

    class Meta:
        db_table = 'aggregator_category'
        managed = False
        verbose_name_plural = _('News categories')


class Feed(Model):
    fid = AutoField(primary_key=True)
    title = CharField(max_length=255)
    url = URLField(_('URL'), max_length=255)
    refresh = IntegerField()  # interval in seconds
    checked = UnixTimeStampField()
    link = URLField(max_length=255)
    description = TextField()
    image = TextField()
    etag = CharField(max_length=255)
    modified = UnixTimeStampField()
    block = SmallIntegerField()
    categories = ManyToManyField(Category, related_name='feeds', through='FeedCategory')

    class Meta:
        db_table = 'aggregator_feed'
        managed = False

    def category_list(self):
        return ', '.join(sorted(self.categories.values_list('title', flat=True)))

    def item_count(self):
        return self.items.count()


class FeedCategory(Model):
    # Primary key is FAKE! It is simply to prevent attempts to access 'id'!
    # Silence check by: SILENCED_SYSTEM_CHECKS = ['fields.W342']
    feed = ForeignKey(Feed, CASCADE, db_column='fid', primary_key=True)
    category = ForeignKey(Category, CASCADE, db_column='cid')

    class Meta:
        db_table = 'aggregator_category_feed'
        managed = False


class Item(Model):
    iid = AutoField(primary_key=True)
    feed = ForeignKey(Feed, SET_NULL, db_column='fid', related_name='items',
                      null=True, blank=True)
    title = CharField(max_length=255)
    link = URLField(max_length=255)
    author = CharField(max_length=255)
    description = TextField()
    timestamp = UnixTimeStampField()
    guid = CharField(max_length=255)

    class Meta:
        db_table = 'aggregator_item'
        managed = False

    def category_list(self):
        return self.feed.category_list()