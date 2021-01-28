from flask import render_template, redirect, url_for, flash
from sqlalchemy import func
from werkzeug.utils import secure_filename
from xlrd import open_workbook
from app import app, db
from app.disciplineDef import Disciplinizer, dictionarizer
from app.form import UploadForm
from app.models import Sheets, Info, Attributes, Abilities, Traits, Disciplines
from app.reads import Character
from app.reads import UploadFile


# index page with list of characters to choose from
@app.route('/')
@app.route('/index')
def index():
    char_names = Sheets.query.all()
    return render_template('index.html', title='List', char_names=char_names)


# display full character sheet
@app.route('/sheet/<char_name>')
def sheet(char_name):
    Disciplinizer(char_name)
    character = Sheets.query.filter_by(charactername=char_name).first()
    char_info = Info.query.get(character.id)
    attributes_info = Attributes.query.get(character.id)
    abilities_info = Abilities.query.get(character.id)
    trait_info = Traits.query.get(character.id)
    discipline_info = Disciplines.query.filter(Disciplines.char_id == character.id).all()
    disciplines_lib = dictionarizer(char_name)
    return render_template('fullsheet.html', title='Character Sheet', character=character,
                           about=char_info, attribs=attributes_info, abilits=abilities_info,
                           traits=trait_info, disciplines=discipline_info, definition=disciplines_lib)


@app.route('/addfile', methods=['GET', 'POST'])
def addfile():
    nump = db.session.query(func.max(Sheets.id)).scalar()
    if nump is None:
        ctrl = 1
    else:
        ctrl = nump + 1
    upfile = UploadFile()

    if upfile.validate_on_submit():
        filename = secure_filename(upfile.file.data.filename)
        upfile.file.data.save('uploads/' + filename)

        pc_chart = open_workbook('uploads/' + filename)
        c_sheet = pc_chart.sheet_by_index(0)

        scan = Character(c_sheet)

        add_sheet = Sheets(playername=scan.seeker('Player Name'),
                           charactername=scan.seeker('Character Name'))

        add_info = Info(clan=scan.seeker('Clan'),
                        nature=scan.seeker('Nature'),
                        demeanor=scan.seeker('Demeanor'),
                        role=scan.seeker('Role'),
                        story=scan.seeker('Chronicle'),
                        generation=scan.seeker('Generation'),
                        age=scan.seeker('Age'),
                        sire=scan.seeker('Sire'),
                        char_id=ctrl)

        add_attribs = Attributes(strength=scan.seeker('Strength'), dexterity=scan.seeker('Dexterity'), stamina=scan.seeker('Stamina'),
                                 charisma=scan.seeker('Charisma'), manipulation=scan.seeker('Manipulation'),
                                 appearance=scan.seeker('Appearance'),
                                 perception=scan.seeker('Perception'), intelligence=scan.seeker('Intelligence'),
                                 wits=scan.seeker('Wits'),
                                 char_id=ctrl)

        add_abilits = Abilities(alertness=scan.seeker('Alertness'),
                                athletics=scan.seeker('Athletics'),
                                brawl=scan.seeker('Brawl'),
                                dodge=scan.seeker('Dodge'),
                                empathy=scan.seeker('Empathy'),
                                expression=scan.seeker('Expression'),
                                intimidation=scan.seeker('Intimidation'),
                                leadership=scan.seeker('Leadership'),
                                streetwise=scan.seeker('Streetwise'),
                                subterfuge=scan.seeker('Subterfuge'),
                                animalken=scan.seeker('Animal Ken'),
                                crafts=scan.seeker('Crafts'),
                                drive=scan.seeker('Drive'),
                                etiquette=scan.seeker('Etiquette'),
                                firearms=scan.seeker('Firearms'),
                                melee=scan.seeker('Melee'),
                                performance=scan.seeker('Performance'),
                                security=scan.seeker('Security'),
                                stealth=scan.seeker('Stealth'),
                                survival=scan.seeker('Survival'),
                                academics=scan.seeker('Academics'),
                                computer=scan.seeker('Computer'),
                                finance=scan.seeker('Finance'),
                                investigation=scan.seeker('Investigation'),
                                law=scan.seeker('Law'),
                                linguistics=scan.seeker('Linguistics'),
                                medicine=scan.seeker('Medicine'),
                                occult=scan.seeker('Occult'),
                                politics=scan.seeker('Politics'),
                                science=scan.seeker('Science'),
                                char_id=ctrl)

        add_traits = Traits(willpower=scan.seeker('Willpower'),
                            path_name=scan.seeker('Path Name'),
                            path_lvl=scan.seeker('Path lvl'),
                            bloodpool=scan.seeker('Bloodpool'),
                            ppt=scan.seeker('BPPT'),
                            conscience=scan.seeker('Conscience'),
                            selfcontrol=scan.seeker('SelfControl'),
                            courage=scan.seeker('Courage'),
                            char_id=ctrl)

        add_discs = Disciplines(disciplineid=scan.seeker('Potence'), dlevel=scan.seeker('Potence'), char_id=ctrl)

        db.session.add(add_sheet)
        db.session.add(add_info)
        db.session.add(add_attribs)
        db.session.add(add_abilits)
        db.session.add(add_traits)
        db.session.add(add_discs)
        db.session.commit()

        flash('Character ->> ' + scan.seeker('Character Name') + ' <<- added successfully!')
        return redirect(url_for('index'))
    return render_template('fileadd.html', title='Add from file', upfile=upfile)


@app.route('/addform', methods=['GET', 'POST'])
def addform():
    nump = db.session.query(func.max(Sheets.id)).scalar()
    if nump is None:
        ctrl = 1
    else:
        ctrl = nump + 1
    form = UploadForm()
    if form.validate_on_submit():
        form_sheet = Sheets(playername=form.form_player.data,
                            charactername=form.form_char.data)

        form_info = Info(clan=form.form_clan.data,
                         nature=form.form_nature.data,
                         demeanor=form.form_demeanor.data,
                         role=form.form_role.data,
                         story=form.form_story.data,
                         generation=form.form_generation.data,
                         age=form.form_age.data,
                         sire=form.form_sire.data,
                         char_id=ctrl)

        form_attribs = Attributes(strength=form.strength.data, dexterity=form.dexterity.data, stamina=form.stamina.data,
                                  charisma=form.charisma.data, manipulation=form.manipulation.data,
                                  appearance=form.appearance.data,
                                  perception=form.perception.data, intelligence=form.intelligence.data,
                                  wits=form.wits.data,
                                  char_id=ctrl)

        form_abilits = Abilities(alertness=form.alertness.data,
                                 athletics=form.athletics.data,
                                 brawl=form.brawl.data,
                                 dodge=form.dodge.data,
                                 empathy=form.empathy.data,
                                 expression=form.expression.data,
                                 intimidation=form.intimidation.data,
                                 leadership=form.leadership.data,
                                 streetwise=form.streetwise.data,
                                 subterfuge=form.subterfuge.data,
                                 animalken=form.animalken.data,
                                 crafts=form.crafts.data,
                                 drive=form.drive.data,
                                 etiquette=form.etiquette.data,
                                 firearms=form.firearms.data,
                                 melee=form.melee.data,
                                 performance=form.performance.data,
                                 security=form.security.data,
                                 stealth=form.stealth.data,
                                 survival=form.survival.data,
                                 academics=form.academics.data,
                                 computer=form.computer.data,
                                 finance=form.finance.data,
                                 investigation=form.investigation.data,
                                 law=form.law.data,
                                 linguistics=form.linguistics.data,
                                 medicine=form.medicine.data,
                                 occult=form.occult.data,
                                 politics=form.politics.data,
                                 science=form.science.data,
                                 char_id=ctrl)

        form_traits = Traits(willpower=form.form_willpower.data,
                             path_name=form.form_path_name.data,
                             path_lvl=form.form_path_lvl.data,
                             bloodpool=form.form_bloodpool.data,
                             ppt=form.form_ppt.data,
                             conscience=form.form_conscience.data,
                             selfcontrol=form.form_selfcontrol.data,
                             courage=form.form_courage.data,
                             char_id=ctrl)

        form_discc = Disciplines(disciplineid=form.form_disciplines.data, dlevel=form.form_dlevel.data, char_id=ctrl)

        db.session.add(form_sheet)
        db.session.add(form_info)
        db.session.add(form_attribs)
        db.session.add(form_abilits)
        db.session.add(form_traits)
        db.session.add(form_discc)
        db.session.commit()
        flash('Character ->> ' + form.form_char.data + ' <<- added successfully!')
        return redirect(url_for('index'))
    return render_template('form.html', title='Add from form', form=form)


@app.route('/remove')
def remove():
    sheets_delete = Sheets.query.all()
    for sheet in sheets_delete:
        db.session.delete(sheet)

    char_delete = Info.query.all()
    for info in char_delete:
        db.session.delete(info)

    attributes_delete = Attributes.query.all()
    for attribute in attributes_delete:
        db.session.delete(attribute)

    abilities_delete = Abilities.query.all()
    for ability in abilities_delete:
        db.session.delete(ability)

    trait_delete = Traits.query.all()
    for trait in trait_delete:
        db.session.delete(trait)

    disc_delete = Disciplines.query.all()
    for disc in disc_delete:
        db.session.delete(disc)

    db.session.commit()
    return render_template('info.html', title='Clean database')


@app.route('/info')
def info():
    # some info about what is this all about
    return render_template('info.html', title='Information')
