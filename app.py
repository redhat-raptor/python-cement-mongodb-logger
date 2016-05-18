#!/bin/env python

from cement.core.foundation import CementApp
from log4mongo.handlers import MongoHandler


class MyCementApp(CementApp):
    class Meta:
        label = 'cement_mongodb_logger'


def main():
    with MyCementApp() as app:
        '''
        Can be any of the followings:
            'DEBUG'
            'INFO'
            'WARN'
            'ERROR'
            'FATAL'
        '''
        app.log.set_level('DEBUG')

        # Ideally get the mongo configs from cement config file
        host = 'localhost'
        port = 27017
        database_name = 'cement_mongodb_logs'
        collection = 'logs'

        mongo_handler = MongoHandler(
            host=host,
            port=port,
            database_name=database_name,
            collection=collection
        )

        app.log.backend.addHandler(mongo_handler)
        app.run()

        # Log it!
        app.log.info('This logs a info!')
        app.log.warn('This logs a warning!')
        app.log.error('This logs an error!')
        app.log.fatal('This logs a fatal error!')
        app.log.debug('This logs a debug!')


if __name__ == '__main__':
    main()
