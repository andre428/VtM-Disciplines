from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FieldList, FormField

from app.models import ClansDict, DisciplineDict, PathDict

clan_choices = [(c.id, c.clanname) for c in ClansDict.query.order_by('clanname')]

discipline_choices = [(d.id, d.discipline) for d in DisciplineDict.query.order_by('discipline')]

path_choices = [(p.id, p.pathname) for p in PathDict.query.order_by('pathname')]


class ListOfDiss(FlaskForm):
    list_disciplines = SelectField(choices=discipline_choices)
    form_dlevel = IntegerField()


class UploadForm(FlaskForm):
    form_player = StringField()
    form_char = StringField()

    form_clan = SelectField(choices=clan_choices)

    form_nature = StringField()
    form_demeanor = StringField()
    form_role = StringField()
    form_story = StringField()
    form_generation = IntegerField()
    form_age = IntegerField()
    form_sire = StringField()

    strength = IntegerField()
    dexterity = IntegerField()
    stamina = IntegerField()
    charisma = IntegerField()
    manipulation = IntegerField()
    appearance = IntegerField()
    perception = IntegerField()
    intelligence = IntegerField()
    wits = IntegerField()

    alertness = IntegerField()
    athletics = IntegerField()
    brawl = IntegerField()
    dodge = IntegerField()
    empathy = IntegerField()
    expression = IntegerField()
    intimidation = IntegerField()
    leadership = IntegerField()
    streetwise = IntegerField()
    subterfuge = IntegerField()

    animalken = IntegerField()
    crafts = IntegerField()
    drive = IntegerField()
    etiquette = IntegerField()
    firearms = IntegerField()
    melee = IntegerField()
    performance = IntegerField()
    security = IntegerField()
    stealth = IntegerField()
    survival = IntegerField()

    academics = IntegerField()
    computer = IntegerField()
    finance = IntegerField()
    investigation = IntegerField()
    law = IntegerField()
    linguistics = IntegerField()
    medicine = IntegerField()
    occult = IntegerField()
    politics = IntegerField()
    science = IntegerField()

    form_willpower = IntegerField()
    form_path_name = SelectField(choices=path_choices)
    form_path_lvl = IntegerField()
    form_bloodpool = IntegerField()
    form_ppt = IntegerField()
    form_conscience = IntegerField()
    form_selfcontrol = IntegerField()
    form_courage = IntegerField()

    form_disciplines = FieldList(FormField(ListOfDiss), min_entries=3, max_entries=10)

    submit = SubmitField('Submit Character')
