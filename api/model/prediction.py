
from enum import Enum
import json


class Prediction:

    def __init__(self, predictions_json):
        p_dict = json.loads(predictions_json)

        self.character_fates = {
            Character[q_id]: CharacterStatus(q_val) for q_id, q_val in p_dict['character_fates'].items()
        }

        self.yes_no_questions = {
            YesNoQuestion[q_id]: bool(q_val) for q_id, q_val in p_dict['yes_no_questions'].items()
        }

        self.character_choices = {
            CharacterChoiceQuestion[q_id]: Character[q_val] for q_id, q_val in p_dict['character_choices'].items()
        }

    @property
    def json(self):
        return {
            'character_fates': {
                q.name: v.value for q, v in self.character_fates.items()
            },
            'yes_no_questions': {
                q.name: v.value for q, v in self.yes_no_questions.items()
            },
            'character_choices': {
                q.name: v.id for q, v in self.character_choices.items()
            }
        }


class Question(Enum):
    def __init__(self, text, img_src):
        super().__init__()
        self.text = text
        self.img_src = img_src

    @property
    def json(self):
        return {'text': self.text, 'src': self.img_src}

    @staticmethod
    def get_questions_json(question_class):
        return {q.name: q.json for q in question_class}

    @staticmethod
    def get_all_questions():
        return {
            'character_fates': Question.get_questions_json(Character),
            'yes_no_questions': Question.get_questions_json(YesNoQuestion),
            'character_choices': Question.get_questions_json(CharacterChoiceQuestion)
        }


class Character(Question):
    JON_SNOW = ('Jon Snow', 'jon_snow.png')
    ARYA_STARK = ('Arya Stark', 'arya_stark.png')
    SANSA_STARK = ('Sansa Stark', 'sansa_stark.png')
    BRAN_STARK = ('Bran Stark', 'bran_stark.png')
    DAENERYS_TARGARYEN = ('Daenerys Targaryen', 'daenerys_targaryen.png')
    CERSEI_LANNISTER = ('Cersei Lannister', 'cersei_lannister.png')
    JAIME_LANNISTER = ('Jaime Lannister', 'jaime_lannister.png')
    TYRION_LANNISTER = ('Tyrion Lannister', 'tyrion_lannister.png')
    BRIENNE_OF_TARTH = ('Brienne Of Tarth', 'brienne_of_tarth.png')
    MELISANDRE = ('Melisandre', 'melisandre.png')
    VARYS = ('Varys', 'varys.png')
    DAVOS_SEAWORTH = ('Davos Seaworth', 'davos_seaworth.png')
    GENDRY = ('Gendry', 'gendry.png')
    SAMWELL_TARLY = ('Samwell Tarly', 'samwell_tarly.png')
    GILLY = ('Gilly', 'gilly.png')
    BABY_SAM = ('Baby Sam', 'baby_sam.png')
    GHOST = ('Ghost', 'ghost.png')
    NYMERIA = ('Nymeria', 'nymeria.png')
    DROGON = ('Drogon', 'drogon.png')
    RHAEGAL = ('Rhaegal', 'rhaegal.png')
    LYANNA_MORMONT = ('Lyanna Mormont', 'lyanna_mormont.png')
    QYBURN = ('Qyburn', 'qyburn.png')
    THE_MOUNTAIN = ('The Mountain', 'the_mountain.png')
    THE_HOUND = ('The Hound', 'the_hound.png')
    THEON_GREYVJOY = ('Theon Greyvjoy', 'theon_greyvjoy.png')
    JORAH_MORMONT = ('Jorah Mormont', 'jorah_mormont.png')
    BRONN = ('Bronn', 'bronn.png')
    GREY_WORM = ('Grey Worm', 'grey_worm.png')
    MISSANDEI = ('Missandei', 'missandei.png')
    BERRIC_DONDARRION = ('Berric Dondarrion', 'berric_dondarrion.png')
    EURON_GREYJOY = ('Euron Greyjoy', 'euron_greyjoy.png')
    PODRICK_PAYNE = ('Podrick Payne', 'podrick_payne.png')
    TORMUND_GIANTSBANE = ('Tormund Giantsbane', 'tormund_giantsbane.png')
    YARA_GREYJOY = ('Yara Greyjoy', 'yara_greyjoy.png')
    HOT_PIE = ('Hot Pie', 'hot_pie.png')
    THE_NIGHT_KING = ('The Night King', 'the_night_king.png')


class CharacterStatus(Enum):
    ALIVE = 0
    DEAD = 1
    WHITE_WALKER = 2


class YesNoQuestion(Question):
    CERSEI_PREGNANT = ('Is Cersei pregnant ?', 'cersei_pregnant.png')
    DAENERYS_PREGNANT = ('Is Daenerys pregnant (or will be in the season) ?', 'daenerys_pregnant.png')
    BRAN_NIGHT_KING = ('Is Bran related to the Night King ?', 'bran_night_king.png')
    CANT_KILL_WW = ('Someone won\'t be able to kill his friend who turned into a white walker', 'cant_kill_ww.png')
    WINTERFELL_DESTROYED = ('Winterfell get destroyed', 'winterfell_destroyed.png')
    KING_LANDING_DESTROYED = ('King\'s Landing get destroyed', 'kings_landing_destroyed.png')
    WW_REACH_ESSOS = ('The White Walkers reach Essos', 'ww_essos.png')
    ARYA_KILL_LIST = ('Arya completes her kill list', 'arya_kill_list.png')


class CharacterChoiceQuestion(Question):
    IRON_THRONE = ('Who will be the last sitting on the Iron Throne ?', 'iron_throne.png')
    KILL_NIGHT_KING = ('Who will kill the Night King ?', 'kill_night_king.png')
    IS_NIGHT_KING = ('Who is the Night King ?', 'is_night_king.png')
    KILL_CERSEI = ('Who will kill Cersei ?', 'kill_cersei.png')
    AZOR_AHAI = ('Who is Azor Ahai ?', 'azor_ahai.png')
    CLEGANE_BOWL = ('Who will win the Cleganebowl !?', 'clegane_bowl.png')
