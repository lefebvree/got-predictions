
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
    JON_SNOW = ('Jon Snow', 'jon_snow.jpeg')
    ARYA_STARK = ('Arya Stark', 'arya_stark.jpeg')
    SANSA_STARK = ('Sansa Stark', 'sansa_stark.jpeg')
    BRAN_STARK = ('Bran Stark', 'bran_stark.jpeg')
    DAENERYS_TARGARYEN = ('Daenerys Targaryen', 'daenerys_targaryen.jpeg')
    CERSEI_LANNISTER = ('Cersei Lannister', 'cersei_lannister.jpeg')
    JAIME_LANNISTER = ('Jaime Lannister', 'jaime_lannister.jpeg')
    TYRION_LANNISTER = ('Tyrion Lannister', 'tyrion_lannister.jpeg')
    BRIENNE_OF_TARTH = ('Brienne Of Tarth', 'brienne_of_tarth.jpeg')
    MELISANDRE = ('Melisandre', 'melisandre.jpeg')
    VARYS = ('Varys', 'varys.jpeg')
    DAVOS_SEAWORTH = ('Davos Seaworth', 'davos_seaworth.jpeg')
    GENDRY = ('Gendry', 'gendry.jpeg')
    SAMWELL_TARLY = ('Samwell Tarly', 'samwell_tarly.jpeg')
    GILLY = ('Gilly', 'gilly.jpeg')
    BABY_SAM = ('Baby Sam', 'baby_sam.jpeg')
    GHOST = ('Ghost', 'ghost.jpeg')
    NYMERIA = ('Nymeria', 'nymeria.jpeg')
    DROGON = ('Drogon', 'drogon.jpeg')
    RHAEGAL = ('Rhaegal', 'rhaegal.jpeg')
    LYANNA_MORMONT = ('Lyanna Mormont', 'lyanna_mormont.jpeg')
    QYBURN = ('Qyburn', 'qyburn.jpeg')
    THE_MOUNTAIN = ('The Mountain', 'the_mountain.jpeg')
    THE_HOUND = ('The Hound', 'the_hound.jpeg')
    THEON_GREYJOY = ('Theon Greyjoy', 'theon_greyjoy.jpeg')
    JORAH_MORMONT = ('Jorah Mormont', 'jorah_mormont.jpeg')
    BRONN = ('Bronn', 'bronn.jpeg')
    GREY_WORM = ('Grey Worm', 'grey_worm.jpeg')
    MISSANDEI = ('Missandei', 'missandei.jpeg')
    BERIC_DONDARRION = ('Beric Dondarrion', 'beric_dondarrion.jpeg')
    EURON_GREYJOY = ('Euron Greyjoy', 'euron_greyjoy.jpeg')
    PODRICK_PAYNE = ('Podrick Payne', 'podrick_payne.jpeg')
    TORMUND_GIANTSBANE = ('Tormund Giantsbane', 'tormund_giantsbane.jpeg')
    YARA_GREYJOY = ('Yara Greyjoy', 'yara_greyjoy.jpeg')
    HOT_PIE = ('Hot Pie', 'hot_pie.jpeg')
    THE_NIGHT_KING = ('The Night King', 'the_night_king.jpeg')


class CharacterStatus(Enum):
    ALIVE = 0
    DEAD = 1
    WHITE_WALKER = 2


class YesNoQuestion(Question):
    CERSEI_PREGNANT = ('Cersei is pregnant', 'cersei_pregnant.jpeg')
    DAENERYS_PREGNANT = ('Daenerys get pregnant', 'daenerys_pregnant.jpeg')
    BRAN_NIGHT_KING = ('Bran is related to the Night King', 'bran_night_king.jpeg')
    CANT_KILL_WW = ('Someone won\'t be able to kill his friend who turned into a white walker', 'cant_kill_ww.jpeg')
    WINTERFELL_DESTROYED = ('Winterfell get destroyed', 'winterfell_destroyed.jpeg')
    KING_LANDING_DESTROYED = ('King\'s Landing get destroyed', 'kings_landing_destroyed.jpeg')
    WW_REACH_ESSOS = ('The White Walkers reach Essos', 'ww_essos.jpeg')
    ARYA_KILL_LIST = ('Arya completes her kill list', 'arya_kill_list.jpeg')
    NED_STARK_COMEBACK = ('Sean Bean as Ned Stark will reappear for a scene', 'ned_stark_comeback.jpeg')
    JAQEN_COMEBACK = ('Jaqen H\'ghar makes a comeback', 'jaqen_comeback.jpeg')
    EPISODE_2_END = ('Episode 2 ends with the White Walkers in front of Westeros', 'episode_2_end.jpeg')


class CharacterChoiceQuestion(Question):
    IRON_THRONE = ('will be the last sitting on the Iron Throne', 'iron_throne.jpeg')
    KILL_NIGHT_KING = ('kill the Night King', 'kill_night_king.jpeg')
    KILL_CERSEI = ('will kill Cersei', 'kill_cersei.jpeg')
    AZOR_AHAI = ('is Azor Ahai', 'azor_ahai.jpeg')
    CLEGANE_BOWL = ('win the Cleganebowl', 'clegane_bowl.jpeg')
