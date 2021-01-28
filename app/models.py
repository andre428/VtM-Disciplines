from app import db


class Sheets(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    playername = db.Column(db.String(64), index=True, unique=False)
    charactername = db.Column(db.String(64), index=True, unique=True)
    character_info = db.relationship('Info', backref='character', lazy=True)
    character_attributes = db.relationship('Attributes', backref='character', lazy=True)
    character_abilities = db.relationship('Abilities', backref='character', lazy=True)
    character_traits = db.relationship('Traits', backref='character', lazy=True)
    character_disciplines = db.relationship('Disciplines', backref='character', lazy=True)

    def __repr__(self):
        return '{}'.format(self.charactername)


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    clan = db.Column(db.Integer, db.ForeignKey('clans_dict.id'), index=True)
    nature = db.Column(db.String(20), unique=False, nullable=False)
    demeanor = db.Column(db.String(20), unique=False, nullable=False)
    role = db.Column(db.String(20), unique=False, nullable=False)
    story = db.Column(db.String(40), unique=False, nullable=False)
    generation = db.Column(db.Integer, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    sire = db.Column(db.String(20), unique=False, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey('sheets.id'), index=True)

    def __repr__(self):
        return 'Clan: {}, Generation: {}'.format(self.claninfo, self.generation)


class Attributes(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    strength = db.Column(db.Integer, unique=False, nullable=False)
    dexterity = db.Column(db.Integer, unique=False, nullable=False)
    stamina = db.Column(db.Integer, unique=False, nullable=False)
    charisma = db.Column(db.Integer, unique=False, nullable=False)
    manipulation = db.Column(db.Integer, unique=False, nullable=False)
    appearance = db.Column(db.Integer, unique=False, nullable=False)
    perception = db.Column(db.Integer, unique=False, nullable=False)
    intelligence = db.Column(db.Integer, unique=False, nullable=False)
    wits = db.Column(db.Integer, unique=False, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey('sheets.id'), index=True)


class Abilities(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    alertness = db.Column(db.Integer, unique=False, nullable=False)
    athletics = db.Column(db.Integer, unique=False, nullable=False)
    brawl = db.Column(db.Integer, unique=False, nullable=False)
    dodge = db.Column(db.Integer, unique=False, nullable=False)
    empathy = db.Column(db.Integer, unique=False, nullable=False)
    expression = db.Column(db.Integer, unique=False, nullable=False)
    intimidation = db.Column(db.Integer, unique=False, nullable=False)
    leadership = db.Column(db.Integer, unique=False, nullable=False)
    streetwise = db.Column(db.Integer, unique=False, nullable=False)
    subterfuge = db.Column(db.Integer, unique=False, nullable=False)
    animalken = db.Column(db.Integer, unique=False, nullable=False)
    crafts = db.Column(db.Integer, unique=False, nullable=False)
    drive = db.Column(db.Integer, unique=False, nullable=False)
    etiquette = db.Column(db.Integer, unique=False, nullable=False)
    firearms = db.Column(db.Integer, unique=False, nullable=False)
    melee = db.Column(db.Integer, unique=False, nullable=False)
    performance = db.Column(db.Integer, unique=False, nullable=False)
    security = db.Column(db.Integer, unique=False, nullable=False)
    stealth = db.Column(db.Integer, unique=False, nullable=False)
    survival = db.Column(db.Integer, unique=False, nullable=False)
    academics = db.Column(db.Integer, unique=False, nullable=False)
    computer = db.Column(db.Integer, unique=False, nullable=False)
    finance = db.Column(db.Integer, unique=False, nullable=False)
    investigation = db.Column(db.Integer, unique=False, nullable=False)
    law = db.Column(db.Integer, unique=False, nullable=False)
    linguistics = db.Column(db.Integer, unique=False, nullable=False)
    medicine = db.Column(db.Integer, unique=False, nullable=False)
    occult = db.Column(db.Integer, unique=False, nullable=False)
    politics = db.Column(db.Integer, unique=False, nullable=False)
    science = db.Column(db.Integer, unique=False, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey('sheets.id'), index=True)


class Traits(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    willpower = db.Column(db.Integer, unique=False, nullable=False)
    path_name = db.Column(db.Integer, db.ForeignKey('path_dict.id'), index=True)
    path_lvl = db.Column(db.Integer, unique=False, nullable=False)
    bloodpool = db.Column(db.Integer, unique=False, nullable=False)
    ppt = db.Column(db.Integer, unique=False, nullable=False)
    conscience = db.Column(db.Integer, unique=False, nullable=False)
    selfcontrol = db.Column(db.Integer, unique=False, nullable=False)
    courage = db.Column(db.Integer, unique=False, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey('sheets.id'), index=True)


class Disciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    disciplineid = db.Column(db.Integer, db.ForeignKey('discipline_dict.id'), index=True)
    dlevel = db.Column(db.Integer, unique=False)
    char_id = db.Column(db.Integer, db.ForeignKey('sheets.id'), index=True)

    def __repr__(self):
        return '{}'.format(self.disinfo)


class DisciplineDict(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    discipline = db.Column(db.String(24), index=True, unique=False)
    disciplines_id = db.relationship('Disciplines', backref='disinfo', lazy=True)

    def __repr__(self):
        return '{}'.format(self.discipline)


class ClansDict(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    clanname = db.Column(db.String(20), index=True, unique=True)
    clan_id = db.relationship('Info', backref='claninfo', lazy=True)

    def __repr__(self):
        return '{}'.format(self.clanname)


class PathDict(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    pathname = db.Column(db.String(36), index=True, unique=True)
    path_id = db.relationship('Traits', backref='pathinfo', lazy=True)

    def __repr__(self):
        return '{}'.format(self.pathname)
