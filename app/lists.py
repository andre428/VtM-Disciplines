"""
from app.models import Sheets, Info, Attributes, Abilities, Traits, Disciplines, Discdict, Clans
from sqlalchemy import func
from app import db
from app.form import UploadForm

form = UploadForm()

nump = db.session.query(func.max(Sheets.id)).scalar()
ctrl = nump + 1

add_sheet = Sheets(playername='playername',
                   charactername='ncfgdkjndf'
                   )

add_info = Info(clan=6,
                nature='nature',
                demeanor='demenor',
                role='role',
                story='story',
                generation=10,
                age=17,
                sire='sire',
                char_id=ctrl
                )

add_attribs = Attributes(strength=3, dexterity=4, stamina=3,
                         charisma=2, manipulation=2, appearance=3,
                         perception=4, intelligence=3, wits=4, char_id=ctrl)

add_abilits = Abilities(alertness=3,
                        athletics=4,
                        brawl=2,
                        dodge=2,
                        empathy=2,
                        expression=2,
                        intimidation=4,
                        leadership=4,
                        streetwise=4,
                        subterfuge=4,
                        animalken=4,
                        crafts=4,
                        drive=4,
                        etiquette=4,
                        firearms=4,
                        melee=4,
                        performance=4,
                        security=4,
                        stealth=4,
                        survival=4,
                        academics=4,
                        computer=4,
                        finance=4,
                        investigation=4,
                        law=4,
                        linguistics=4,
                        medicine=4,
                        occult=4,
                        politics=4,
                        science=4,
                        char_id=ctrl)

add_traits = Traits(willpower=6,
                    humanity=5,
                    path_Name='Humanity',
                    path_lvl=5,
                    bloodpool=12,
                    ppt=2,
                    conscience=3,
                    selfcontrol=3,
                    courage=4,
                    char_id=ctrl
                    )

add_discs = Disciplines(disciplineid=46,
                        dlevel=4,
                        char_id=ctrl
                        )

form_sheet = Sheets(playername=form.form_player.data,
                    charactername=form.form_char.data
                    )

form_info = Info(clan=form.form_clan.data,
                 nature=form.form_nature.data,
                 demeanor=form.form_demeanor.data,
                 role=form.form_role.data,
                 story=form.form_story.data,
                 generation=form.form_generation.data,
                 age=form.form_age.data,
                 sire=form.form_sire.data,
                 char_id=ctrl
                 )

form_attribs = Attributes(strength=form.strength.data, dexterity=form.dexterity.data, stamina=form.stamina.data,
                          charisma=form.charisma.data, manipulation=form.manipulation.data,
                          appearance=form.appearance.data,
                          perception=form.perception.data, intelligence=form.intelligence.data, wits=form.wits.data,
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

form_traits = Traits(willpower=form.form_form_willpower.data,
                     humanity=form.form_humanity.data,
                     path_Name=form.form_form_path_Name.data,
                     path_lvl=form.form_path_lvl.data,
                     bloodpool=form.form_bloodpool.data,
                     ppt=form.form_ppt.data,
                     conscience=form.form_conscience.data,
                     selfcontrol=form.form_selfcontrol.data,
                     courage=form.form_courage.data,
                     char_id=ctrl)
"""