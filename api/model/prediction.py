
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
            CharacterChoiceQuestion[q_id]:
                Character[q_val] if q_val is not '0' else '0' for q_id, q_val in p_dict['character_choices'].items()
        }

    @property
    def json(self):
        return {
            'character_fates': {
                q.name: v.value for q, v in self.character_fates.items()
            },
            'yes_no_questions': {
                q.name: v for q, v in self.yes_no_questions.items()
            },
            'character_choices': {
                q.name: v.name if v is not '0' else '0' for q, v in self.character_choices.items()
            }
        }

    def remove_answered_questions(self):
        chars = list(self.character_fates.keys())
        for char in chars:
            if char.answer is not None:
                self.character_fates.pop(char)
        questions = list(self.yes_no_questions.keys())
        for question in questions:
            if question.answer is not None:
                self.yes_no_questions.pop(question)
        choices = list(self.character_choices.keys())
        for choice in choices:
            if choice.answer is not None:
                self.character_choices.pop(choice)


class Question(Enum):
    def __init__(self, text, img_src, answer):
        super().__init__()
        self.text = text
        self.img_src = img_src
        self.answer = answer

    @property
    def json(self):
        val = {'text': self.text}
        if self.img_src is not None:
            val['src'] = self.img_src
        if self.answer is not None:
            val['answer'] = self.answer
        return val

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


class CharacterStatus(Enum):
    ALIVE = 0
    DEAD = 1
    WHITE_WALKER = 2


class Character(Question):
    JON_SNOW = ('Jon Snow', 'jon_snow.jpeg', None)
    ARYA_STARK = ('Arya Stark', 'arya_stark.jpeg', None)
    SANSA_STARK = ('Sansa Stark', 'sansa_stark.jpeg', None)
    BRAN_STARK = ('Bran Stark', 'bran_stark.jpeg', None)
    DAENERYS_TARGARYEN = ('Daenerys Targaryen', 'daenerys_targaryen.jpeg', None)
    CERSEI_LANNISTER = ('Cersei Lannister', 'cersei_lannister.jpeg', None)
    JAIME_LANNISTER = ('Jaime Lannister', 'jaime_lannister.jpeg', None)
    TYRION_LANNISTER = ('Tyrion Lannister', 'tyrion_lannister.jpeg', None)
    BRIENNE_OF_TARTH = ('Brienne Of Tarth', 'brienne_of_tarth.jpeg', None)
    MELISANDRE = ('Melisandre', 'melisandre.jpeg', None)
    VARYS = ('Varys', 'varys.jpeg', None)
    DAVOS_SEAWORTH = ('Davos Seaworth', 'davos_seaworth.jpeg', None)
    GENDRY = ('Gendry', 'gendry.jpeg', None)
    SAMWELL_TARLY = ('Samwell Tarly', 'samwell_tarly.jpeg', None)
    GILLY = ('Gilly', 'gilly.jpeg', None)
    BABY_SAM = ('Baby Sam', 'baby_sam.jpeg', None)
    GHOST = ('Ghost', 'ghost.jpeg', None)
    NYMERIA = ('Nymeria', 'nymeria.jpeg', None)
    DROGON = ('Drogon', 'drogon.jpeg', None)
    RHAEGAL = ('Rhaegal', 'rhaegal.jpeg', None)
    LYANNA_MORMONT = ('Lyanna Mormont', 'lyanna_mormont.jpeg', None)
    QYBURN = ('Qyburn', 'qyburn.jpeg', None)
    GREGOR_CLEGANE = ('Gregor Clegane', 'the_mountain.jpeg', None)
    SANDOR_CLEGANE = ('Sandor Clegane', 'the_hound.jpeg', None)
    THEON_GREYJOY = ('Theon Greyjoy', 'theon_greyjoy.jpeg', None)
    JORAH_MORMONT = ('Jorah Mormont', 'jorah_mormont.jpeg', None)
    BRONN = ('Bronn', 'bronn.jpeg', None)
    GREY_WORM = ('Grey Worm', 'grey_worm.jpeg', None)
    MISSANDEI = ('Missandei', 'missandei.jpeg', None)
    BERIC_DONDARRION = ('Beric Dondarrion', 'beric_dondarrion.jpeg', None)
    EURON_GREYJOY = ('Euron Greyjoy', 'euron_greyjoy.jpeg', None)
    PODRICK_PAYNE = ('Podrick Payne', 'podrick_payne.jpeg', None)
    TORMUND_GIANTSBANE = ('Tormund Giantsbane', 'tormund_giantsbane.jpeg', None)
    YARA_GREYJOY = ('Yara Greyjoy', 'yara_greyjoy.jpeg', None)
    HOT_PIE = ('Hot Pie', 'hot_pie.jpeg', None)
    THE_NIGHT_KING = ('The Night King', 'the_night_king.jpeg', None)


class YesNoQuestion(Question):
    CERSEI_PREGNANT = ('Cersei is pregnant', None, None)
    DAENERYS_PREGNANT = ('Daenerys get pregnant', None, None)
    BRAN_NIGHT_KING = ('Bran is related to the Night King', None, None)
    CANT_KILL_WW = ('Someone won\'t be able to kill his friend who turned into a whight', None, None)
    WINTERFELL_DESTROYED = ('Winterfell get destroyed', None, None)
    KING_LANDING_DESTROYED = ('King\'s Landing get destroyed', None, None)
    WW_REACH_ESSOS = ('The White Walkers reach Essos', None, None)
    ARYA_KILL_LIST = ('Arya completes her kill list', None, None)
    NED_STARK_COMEBACK = ('Sean Bean as Ned Stark will reappear for a scene', None, None)
    JAQEN_COMEBACK = ('Jaqen H\'ghar makes a comeback', None, None)
    JON_DAENERYS = ('Despite their parentage, Jon and Daenerys remain in love', None, None)
    NO_DRAGON = ('None of the dragons survives', None, None)
    NO_DIREWOLF = ('No Stark direwolf survives', None, None)


class CharacterChoiceQuestion(Question):
    IRON_THRONE = ('will be the last sitting on the Iron Throne', None, None)
    KILL_NIGHT_KING = ('will kill the Night King', None, None)
    KILL_CERSEI = ('will kill Cersei', None, None)
    AZOR_AHAI = ('is Azor Ahai', None, None)
    CLEGANE_BOWL = ('will win the Cleganebowl', None, None)
    KILL_DRAGON = ('will kill a dragon (ice dragon or not)', None, None)
    LAST_DEATH = ('will be the last person to die', None, None)
