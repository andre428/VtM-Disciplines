from app import app, db
from app.models import Sheets, Info, Attributes, Abilities, Traits, Disciplines, DisciplineDict, ClansDict, PathDict


# Defines stuff for easier testing. I guess.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Sheets': Sheets,  'Info': Info,
            'Disciplines': Disciplines, 'Clans': ClansDict, 'Attributes': Attributes,
            'Abilities': Abilities, 'Traits': Traits, 'Distionary': DisciplineDict, 'Path': PathDict}


# Spin this shit up and run. Still need to figure out why the names are given this way..
if __name__ == '__main__':
    app.run()
