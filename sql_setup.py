def setup_dependencies(app):
    '''Helper function that sets up all needed processes for the flask app to run.'''

    # add models folder to path
    import os
    import sys
    sys.path.insert(1, 'models')

    # import models
    from passing import Passing, db
    from rushing import Rushing

    # initialize database
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    try:
        DATABASE_URL = os.environ['DATABASE_URL']
    except KeyError:
        from config import password
        DATABASE_URL = f'postgresql://fred:{password}@localhost:5432/database'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app)

    # create engine from database irl
    engine = create_engine(DATABASE_URL)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # import data handlers
    sys.path.insert(1, 'data_insert')

    # create tables
    if not engine.dialect.has_table(engine, 'passing'):

        Passing.__table__.create(bind=engine)
        session.commit()

    if not engine.dialect.has_table(engine, 'rushing'):
        Rushing.__table__.create(bind=engine)
        session.commit()

    return engine, session, Passing, Rushing
