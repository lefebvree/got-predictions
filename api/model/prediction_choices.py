
from enum import Enum


class Choices:

    def __init__(self, fates, yes_no, characters):
        self.fates = fates
        self.choices_yes_no = yes_no
        self.choices_characters = characters

    @property
    def json(self):
        return {
            'fates'
        }


class Choice(Enum):
    def __init__(self, index, text, src):
        super().__init__()
        self.index = index
        self.text = text
        self.src = src


class Character(Choice):
    JON_SNOW = (0, 'Jon Snow', 'jon_snow')
    ARYA_STARK = (1, 'Arya Stark', 'arya_stark')
    SANSA_STARK = (2, 'Sansa Stark', 'sansa_stark')
    BRAN_STARK = (3, 'Bran Stark', 'bran_stark')
    DAENERYS_TARGARYEN = (4, 'Daenerys Targaryen', 'daenerys_targaryen')
    CERSEI_LANNISTER = (5, 'Cersei Lannister', 'cersei_lannister')
    JAIME_LANNISTER = (6, 'Jaime Lannister', 'jaime_lannister')
    TYRION_LANNISTER = (7, 'Tyrion Lannister', 'tyrion_lannister')
    BRIENNE_OF_TARTH = (8, 'Brienne Of Tarth', 'brienne_of_tarth')
    MELISANDRE = (9, 'Melisandre', 'melisandre')
    VARYS = (10, 'Varys', 'varys')
    DAVOS_SEAWORTH = (11, 'Davos Seaworth', 'davos_seaworth')
    GENDRY = (12, 'Gendry', 'gendry')
    SAMWELL_TARLY = (13, 'Samwell Tarly', 'samwell_tarly')
    GILLY = (14, 'Gilly', 'gilly')
    BABY_SAM = (15, 'Baby Sam', 'baby_sam')
    GHOST = (16, 'Ghost', 'ghost')
    NYMERIA = (17, 'Nymeria', 'nymeria')
    DROGON = (18, 'Drogon', 'drogon')
    RHAEGAL = (19, 'Rhaegal', 'rhaegal')
    LYANNA_MORMONT = (20, 'Lyanna Mormont', 'lyanna_mormont')
    QYBURN = (21, 'Qyburn', 'qyburn')
    THE_MOUNTAIN = (22, 'The Mountain', 'the_mountain')
    THE_HOUND = (23, 'The Hound', 'the_hound')
    THEON_GREYVJOY = (24, 'Theon Greyvjoy', 'theon_greyvjoy')
    JORAH_MORMONT = (25, 'Jorah Mormont', 'jorah_mormont')
    BRONN = (26, 'Bronn', 'bronn')
    GREY_WORM = (27, 'Grey Worm', 'grey_worm')
    MISSANDEI = (28, 'Missandei', 'missandei')
    BERRIC_DONDARRION = (29, 'Berric Dondarrion', 'berric_dondarrion')
    EURON_GREYJOY = (30, 'Euron Greyjoy', 'euron_greyjoy')
    PODRICK_PAYNE = (31, 'Podrick Payne', 'podrick_payne')
    TORMUND_GIANTSBANE = (32, 'Tormund Giantsbane', 'tormund_giantsbane')
    YARA_GREYJOY = (33, 'Yara Greyjoy', 'yara_greyjoy')
    HOT_PIE = (34, 'Hot Pie', 'hot_pie')
    THE_NIGHT_KING = (35, 'The Night King', 'the_night_king')


class YesNoChoice(Choice):
    CERSEI_PREGNANT = (0, 'Is Cersei pregnant ?', 'cersei_pregnant')
    DAENERYS_PREGNANT = (1, 'Is Daenerys pregnant (or will be in the season) ?', 'daenerys_pregnant')
    BRAN_NIGHT_KING = (2, 'Is Bran related to the Night King ?', 'bran_night_king')
    CANT_KILL_WW = (3, 'Someone won\'t be able to kill his friend who turned into a white walker', 'cant_kill_ww')
    WINTERFELL_DESTROYED = (4, 'Winterfell get destroyed', 'winterfell_destroyed')
    KING_LANDING_DESTROYED = (5, 'King\'s Landing get destroyed', 'kings_landing_destroyed')
    WW_REACH_ESSOS = (6, 'The White Walkers reach Essos', 'ww_essos')
    ARYA_KILL_LIST = (7, 'Arya completes her kill list', 'arya_kill_list')


class CharacterChoice(Choice):
    IRON_THRONE = (0, 'Who will be the last sitting on the Iron Throne ?', 'iron_throne')
    KILL_NIGHT_KING = (1, 'Who will kill the Night King ?', 'kill_night_king')
    IS_NIGHT_KING = (2, 'Who is the Night King ?', 'is_night_king')
    KILL_CERSEI = (3, 'Who will kill Cersei ?', 'kill_cersei')
    AZOR_AHAI = (4, 'Who is Azor Ahai ?', 'azor_ahai')
    CLEGANE_BOWL = (5, 'Who will win the Cleganebowl !?', 'clegane_bowl')
