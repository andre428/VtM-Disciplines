from app.models import Sheets, Info, Attributes, Abilities, Traits


class Disciplinizer:

    def __init__(self, char_name, character=[], char_info=[], attributes_info=[], abilities_info=[],
                 trait_info=[]):
        self.char_name = char_name
        self.character = character
        self.char_info = char_info
        self.attributes_info = attributes_info
        self.abilities_info = abilities_info
        self.trait_info = trait_info

    def data(self):
        self.character = Sheets.query.filter_by(charactername=self.char_name).first()
        self.char_info = Info.query.get(self.character.id)
        self.attributes_info = Attributes.query.get(self.character.id)
        self.abilities_info = Abilities.query.get(self.character.id)
        self.trait_info = Traits.query.get(self.character.id)

    def animalism1(self):
        return 'Roll: Manipulation + Animal Ken => ' + str(
            self.attributes_info.manipulation + self.abilities_info.animalken)

    def animalism2(self):
        return 'Roll: Charisma + Survival => ' + str(self.attributes_info.charisma + self.abilities_info.survival)

    def animalism3(self):
        return 'Roll: Manipulation + Intimidation / Empathy => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation) + ' / ' + str(
            self.attributes_info.manipulation + self.abilities_info.empathy)

    def animalism4(self):
        return 'Roll: Manipulation + Animal Ken => ' + str(
            self.attributes_info.manipulation + self.abilities_info.animalken)

    def animalism5(self):
        return 'Roll: Manipulation + Self Control => ' + str(
            self.attributes_info.manipulation + self.trait_info.selfcontrol)

    def auspex2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def auspex3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def auspex4(self):
        return 'Roll: Intelligence + Subterfuge => ' + str(
            self.attributes_info.intelligence + self.abilities_info.subterfuge)

    def auspex5(self):
        return 'Roll: Perception + Occult => ' + str(
            self.attributes_info.perception + self.abilities_info.occult)

    def bardo1(self):
        return 'Roll: Conscience => ' + str(
            self.trait_info.conscience)

    def bardo2(self):
        return 'Roll: UnConscience => ' + str(
            self.trait_info.conscience)

    def bardo3(self):
        return 'Roll: UnConscience => ' + str(
            self.trait_info.conscience)

    def bardo4(self):
        return 'Roll: Conscience => ' + str(
            self.trait_info.conscience)

    def bardo5(self):
        return 'Roll: Conscience => ' + str(
            self.trait_info.conscience)

    def chimerstry5(self):
        return 'Spend 2 WP, Roll: Manipulation + Subterfuge => ' + str(
            self.attributes_info.manipulation + self.abilities_info.subterfuge)

    def daimonion1(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def daimonion2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def daimonion3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def daimonion4(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def daimonion5(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def dementation1(self):
        return 'Roll: Charisma + Empathy => ' + str(
            self.attributes_info.charisma + self.abilities_info.empathy)

    def dementation2(self):
        return 'Roll: Charisma + Empathy => ' + str(
            self.attributes_info.charisma + self.abilities_info.empathy)

    def dementation3(self):
        return 'Roll: Charisma + Empathy => ' + str(
            self.attributes_info.charisma + self.abilities_info.empathy)

    def dementation4(self):
        return 'Roll: Charisma + Empathy => ' + str(
            self.attributes_info.charisma + self.abilities_info.empathy)

    def dementation5(self):
        return 'Roll: Charisma + Empathy => ' + str(
            self.attributes_info.charisma + self.abilities_info.empathy)

    def dominate1(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def dominate2(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def dominate3(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def dominate4(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def dominate5(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def melpominee2(self):
        return '1 BP + Roll: Wits + Performance => ' + str(
            self.attributes_info.wits + self.abilities_info.performance)

    def melpominee3(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def melpominee4(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def melpominee5(self):
        return 'Roll: Manipulation + Intimidation => ' + str(
            self.attributes_info.manipulation + self.abilities_info.intimidation)

    def mytherceria3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def mytherceria4(self):
        return 'Roll: Intelligence + Crafts => ' + str(
            self.attributes_info.intelligence + self.abilities_info.crafts)

    def mytherceria5(self):
        return 'Roll: Manipulation + Occult => ' + str(
            self.attributes_info.manipulation + self.abilities_info.occult)

    def obeah2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def obeah3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def obeah4(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def obeah5(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def obfuscate2(self):
        return 'Roll: Wits + Stealth => ' + str(
            self.attributes_info.wits + self.abilities_info.stealth)

    def obfuscate3(self):
        return 'Roll: Manipulation + Performance => ' + str(
            self.attributes_info.manipulation + self.abilities_info.performance)

    def obfuscate4(self):
        return 'Roll: Charisma + Stealth => ' + str(
            self.attributes_info.charisma + self.abilities_info.stealth)

    def obtenebration2(self):
        return 'Roll: Manipulation + Occult => ' + str(
            self.attributes_info.manipulation + self.abilities_info.stealth)

    def obtenebration3(self):
        return 'Roll: Manipulation + Occult => ' + str(
            self.attributes_info.manipulation + self.abilities_info.occult)

    def obtenebration4(self):
        return 'Roll: Manipulation + Occult => ' + str(
            self.attributes_info.manipulation + self.abilities_info.occult)

    def presence1(self):
        return 'Roll: Charisma + Performance => ' + str(
            self.attributes_info.charisma + self.abilities_info.performance)

    def presence2(self):
        return 'Roll: Charisma + Intimidation => ' + str(
            self.attributes_info.charisma + self.abilities_info.intimidation)

    def presence3(self):
        return 'Roll: Appearance + Empathy => ' + str(
            self.attributes_info.appearance + self.abilities_info.empathy)

    def presence4(self):
        return 'Roll: Charisma + Subterfuge => ' + str(
            self.attributes_info.charisma + self.abilities_info.subterfuge)

    def quietus2(self):
        return '1+ BP + Roll: Willpower and Attack => ' + str(
            self.attributes_info.dexterity + self.abilities_info.melee)

    def quietus3(self):
        return 'Roll: Stamina => ' + str(self.attributes_info.stamina)

    def quietus5(self):
        return 'Roll: Stamina + Athletics => ' + str(
            self.attributes_info.stamina + self.abilities_info.athletics)

    def temporis1(self):
        return 'Roll: Perception + Alertness => ' + str(
            self.attributes_info.perception + self.abilities_info.alertness)

    def temporis2(self):
        return 'Roll: Manipulation + Occult => ' + str(
            self.attributes_info.manipulation + self.abilities_info.occult)

    def temporis3(self):
        return '1 BP + Roll: Intelligence + Occult => ' + str(
            self.attributes_info.intelligence + self.abilities_info.occult)

    def temporis4(self):
        return '2 BP + Roll: Intelligence + Occult => ' + str(
            self.attributes_info.intelligence + self.abilities_info.occult)

    def temporis5(self):
        return '3 BP + Roll: Intelligence + Occult => ' + str(
            self.attributes_info.intelligence + self.abilities_info.occult)

    def thanatosis1(self):
        return 'Optional Roll: Stamina + Subterfuge => ' + str(
            self.attributes_info.stamina + self.abilities_info.subterfuge)

    def thanatosis2(self):
        return 'Optional Roll: Stamina + Subterfuge => ' + str(
            self.attributes_info.stamina + self.abilities_info.subterfuge)

    def thanatosis3(self):
        return 'Optional Roll: Stamina + Subterfuge => ' + str(
            self.attributes_info.stamina + self.abilities_info.subterfuge)

    def thanatosis4(self):
        return 'Optional Roll: Stamina + Subterfuge => ' + str(
            self.attributes_info.stamina + self.abilities_info.subterfuge)

    def thanatosis5(self):
        return 'Optional Roll: Stamina + Subterfuge => ' + str(
            self.attributes_info.stamina + self.abilities_info.subterfuge)

    def valeren1(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def valeren2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def valeren3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def valeren4(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def valeren5(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def vicissitude1(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def vicissitude2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def vicissitude3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def vicissitude4(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def vicissitude5(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def visceratika1(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def visceratika2(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def visceratika3(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def visceratika4(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)

    def visceratika5(self):
        return 'Roll: Perception + Empathy => ' + str(
            self.attributes_info.perception + self.abilities_info.empathy)


def dictionarizer(cname):
    pooler = Disciplinizer(cname)
    pooler.data()
    discipline_definition = {
        'Animalism': {1: pooler.animalism1(),
                      2: pooler.animalism2(),
                      3: pooler.animalism3(),
                      4: pooler.animalism4(),
                      5: pooler.animalism5()},

        'Auspex': {1: 'No roll to activate.',
                   2: pooler.auspex2(),
                   3: pooler.auspex3(),
                   4: pooler.auspex4(),
                   5: pooler.auspex5()},

        'Bardo': {1: pooler.bardo1(),
                  2: pooler.bardo1(),
                  3: pooler.bardo1(),
                  4: pooler.bardo1(),
                  5: pooler.bardo1()},

        'Celerity': {1: '1 BP => +1 Turn',
                     2: '1 BP => +2 Turns',
                     3: '1 BP => +3 Turns',
                     4: '1 BP => +4 Turns',
                     5: '1 BP => +5 Turns'},

        'Chimerstry': {1: '1 WP - no roll',
                       2: '1 WP + 1 BP - no roll',
                       3: '1 BP - no roll',
                       4: '1 BP - no roll',
                       5: pooler.chimerstry5()},

        'Daimonion': {1: pooler.daimonion1(),
                      2: pooler.daimonion2(),
                      3: pooler.daimonion3(),
                      4: pooler.daimonion4(),
                      5: pooler.daimonion5()},

        'Dementation': {1: pooler.dementation1(),
                        2: pooler.dementation2(),
                        3: pooler.dementation3(),
                        4: pooler.dementation4(),
                        5: pooler.dementation5()},

        'Dominate': {1: pooler.dominate1(),
                     2: pooler.dominate2(),
                     3: pooler.dominate3(),
                     4: pooler.dominate4(),
                     5: pooler.dominate5()},

        'Flight': {1: 'Glide',
                   2: 'Fly 1',
                   3: 'Fly 2',
                   4: 'Fly 3',
                   5: 'Fly 4'},

        'Fortitude': {1: '+1 Soak',
                      2: '+2 Soak',
                      3: '+3 Soak',
                      4: '+4 Soak',
                      5: '+5 Soak'},

        'Melpominee': {1: 'The Missing Voice',
                       2: pooler.melpominee2(),
                       3: pooler.melpominee3(),
                       4: pooler.melpominee4(),
                       5: pooler.melpominee5()},

        'Mytherceria': {1: 'Activation',
                        2: 'Detect fae',
                        3: pooler.mytherceria3(),
                        4: pooler.mytherceria4(),
                        5: pooler.mytherceria5()},

        'Obeah': {1: 'Lick & Heal',
                  2: pooler.obeah2(),
                  3: pooler.obeah3(),
                  4: pooler.obeah4(),
                  5: pooler.obeah5()},

        'Obfuscate': {1: 'Hide & Seek',
                      2: pooler.obfuscate2(),
                      3: pooler.obfuscate3(),
                      4: pooler.obfuscate4(),
                      5: 'Cloak numbers of friends'},

        'Obtenebration': {1: '1 BP',
                          2: pooler.obtenebration2(),
                          3: pooler.obtenebration3(),
                          4: pooler.obtenebration4(),
                          5: '3 BP'},

        'Potence': {1: '+1 Strength',
                    2: '+2 Strength',
                    3: '+3 Strength',
                    4: '+4 Strength',
                    5: '+5 Strength'},

        'Presence': {1: pooler.presence1(),
                     2: pooler.presence2(),
                     3: pooler.presence3(),
                     4: pooler.presence4(),
                     5: '1 WP'},

        'Protean': {1: 'Eyes',
                    2: '1 BP',
                    3: '1 BP',
                    4: '1 BP',
                    5: '1 BP'},

        'Quietus': {1: '1 BP',
                    2: pooler.quietus2(),
                    3: pooler.quietus3(),
                    4: '1+ BP',
                    5: pooler.quietus5()},

        'Sanguinus': {1: '1 BP',
                      2: '1 BP',
                      3: '1 BP',
                      4: '1 BP',
                      5: '3 BP'},

        'Serpentis': {1: 'Stare',
                      2: 'Tongue',
                      3: '1 BP + 1 WP',
                      4: '1 BP',
                      5: 'nothing'},

        'Spiritus': {1: 'Spiritus1',
                     2: 'Spiritus2',
                     3: 'Spiritus3',
                     4: 'Spiritus4',
                     5: 'Spiritus5'},

        'Temporis': {1: pooler.temporis1(),
                     2: pooler.temporis2(),
                     3: pooler.temporis3(),
                     4: pooler.temporis4(),
                     5: pooler.temporis5()},

        'Thanatosis': {1: pooler.thanatosis1(),
                       2: pooler.thanatosis2(),
                       3: pooler.thanatosis3(),
                       4: pooler.thanatosis4(),
                       5: pooler.thanatosis5()},

        'Valeren': {1: pooler.valeren1(),
                    2: pooler.valeren2(),
                    3: pooler.valeren3(),
                    4: pooler.valeren4(),
                    5: pooler.valeren5()},

        'Vicissitude': {1: pooler.vicissitude1(),
                        2: pooler.vicissitude2(),
                        3: pooler.vicissitude3(),
                        4: pooler.vicissitude4(),
                        5: pooler.vicissitude5()},

        'Visceratika': {1: pooler.visceratika1(),
                        2: pooler.visceratika2(),
                        3: pooler.visceratika3(),
                        4: pooler.visceratika4(),
                        5: pooler.visceratika5()}

    }
    return discipline_definition
