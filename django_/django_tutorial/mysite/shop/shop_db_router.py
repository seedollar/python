class ShopDBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'shop':
            return 'shop-db'
        elif model._meta.app_label == 'polls':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        # Make sure we write to the 'default' database when we write Properties models
        if model._meta.model_name == 'properties':
            return None;

        if model._meta.app_label == 'shop':
            return 'shop-db'
        elif model._meta.app_label == 'polls':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        print(">>>>>>>>>>>>>db=%s, app_label=%s, model_name=%s" % (db, app_label, model_name))

        # We make sure that the properties table is replicated on both databases.
        if app_label == 'shop' and model_name == 'properties':
            return None

        if app_label == 'shop':
            return db == 'shop-db'

        if app_label == 'polls':
            return db == 'default'

        if app_label == 'admin':
            return db == 'default'

        if app_label == 'auth':
            return db == 'default'

        if app_label == 'contenttypes':
            return db == 'default'

        if app_label == 'sessions':
            return db == 'default'
        return None
