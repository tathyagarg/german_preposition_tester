import random

class Preposition:
    PREPOSITIONS = []
    def __init__(self, prep: str, words: list[str], is_akkusativ: bool, exceptions: list[int] = None) -> None:
        self.prep = prep
        self.words = words
        self.exceptions = exceptions or []
        self.is_akkusativ = is_akkusativ
        Preposition.PREPOSITIONS.append(self)

    @classmethod
    def query(cls, word):
        for prep in cls.PREPOSITIONS:
            if word in prep.words: return prep.prep
        return -1
    
    @classmethod
    def simple_query(cls, word):
        word = Preposition.query(word)
        if word == 'über': return 'uber'
        if word == 'für': return 'fur'
        return word
    
    @classmethod
    def all_query(cls, word):
        a = Preposition.query(word)
        if a == -1: return a
        b = Preposition.simple_query(word)
        return list(set([a, b]))


an = Preposition(
    'an',
    ['denken', 'glauben', 'leiden', 'schreiben', 'sich erinnern', 'sich gewöhnen', 'sich richten', 'sich wenden', 'sterben', 'stören', 'teilnehmen'],
    True,
    [2, 8, 10]
)
auf = Preposition(
    'auf',
    ['achten', 'ankommen', 'antworten', 'aufpassen', 'hoffen', 'sich beziehen', 'sich freuen', 'sich konzenteiren', 'sich vorbereiten', 'verzichten', 'warten'],
    True
)
mit = Preposition(
    'mit',
    ['anfangen', 'aufhören', 'beginnen', 'diskutieren', 'fahren', 'reden', 'rechnen', 'sich beschäftigen', 'sich streiten', 'sich treffen', 'sich unterhalten', 'sich verabreden', 'sich verstehen', 'sprechen', 'telefonieren', 'umgehen', 'vergleichen', 'verhandeln'],
    False
)
uber = Preposition(
    'über',
    ['diskutieren', 'erzählen', 'nachdenken', 'reden', 'schimpfen', 'sich ärgern', 'sich aufregen', 'sich beschweren', 'sich freuen', 'sich informieren', 'sich unterhalten', 'sich wundern', 'sprechen', 'streiten', 'verfüngen', 'verhandeln', 'lachen'],
    True
)
bei = Preposition(
    'bei',
    ['arbeiten', 'sich bedanken', 'sich beschweren', 'sich entschuldigen', 'helfen', 'wohnen'],
    False
)
nach = Preposition(
    'nach',
    ['fragen', 'riechen', 'schmecken', 'suchen'],
    False
)
fur = Preposition(
    'für',
    ['ausgeben', 'danken', 'eignen', 'kämpfen', 'kaufen', 'protestieren', 'sich bedanken', 'sich engagieren', 'sich entschuldigen', 'sich interessieren', 'sorgen', 'sein'],
    True
)
um = Preposition(
    'um',
    ['beneiden', 'bitten', 'es geht', 'sich bewerben', 'sich handeln', 'sich kümmern', 'sich streiten', 'gehen'],
    True
)
von = Preposition(
    'von',
    ['abhängen', 'erfahren', 'sich erholen', 'erzählen', 'hören', 'träumen', 'sich verabschieden', 'wissen'],
    False
)
zu = Preposition(
    'zu',
    ['einladen', 'führen', 'gehören', 'gratulieren', 'meinen', 'passen'],
    False
)
aus = Preposition('aus', ['bestehen'], False)
als = Preposition('als', ['gelten'], False)
gegen = Preposition('gegen', ['protestieren', 'sein'], True)

DUPLICATES = {'diskutieren': ('mit', 'über'), 'reden': ('mit', 'über'), 'sich freuen': ('auf', 'über'), 'sich unterhalten': ('mit', 'über'), 'sprechen': ('mit', 'über'), 'verhandeln': ('mit', 'über'), 'sich beschweren': ('über', 'bei'), 'sich bedanken': ('bei', 'für'), 'sich entschuldigen': ('bei', 'für'), 'sich streiten': ('mit', 'um'), 'erzählen': ('über', 'von'), 'protestieren': ['für', 'gegen'], 'sein': ['für', 'gegen']}
SIMPLIFIED_DUPLICATES = {'diskutieren': ('mit', 'uber'), 'reden': ('mit', 'uber'), 'sich freuen': ('auf', 'uber'), 'sich unterhalten': ('mit', 'uber'), 'sprechen': ('mit', 'uber'), 'verhandeln': ('mit', 'uber'), 'sich beschweren': ('uber', 'bei'), 'sich bedanken': ('bei', 'fur'), 'sich entschuldigen': ('bei', 'fur'), 'sich streiten': ('mit', 'um'), 'erzählen': ('uber', 'von'), 'protestieren': ['fur', 'gegen'], 'sein': ['fur', 'gegen']}
WORDS = ['aufpassen', 'beneiden', 'schimpfen', 'erfahren', 'bitten', 'sich informieren', 'sich entschuldigen', 'suchen', 'kaufen', 'eignen', 'führen', 'sich interessieren', 'streiten', 'verfüngen', 'sich aufregen', 'protestieren', 'rechnen', 'sich richten', 'kämpfen', 'sich verabreden', 'fragen', 'sich verabschieden', 'sorgen', 'fahren', 'meinen', 'es geht', 'sich freuen', 'sich unterhalten', 'telefonieren', 'riechen', 'sich konzenteiren', 'warten', 'verhandeln', 'leiden', 'aufhören', 'gehören', 'gratulieren', 'vergleichen', 'sich verstehen', 'sich streiten', 'sich handeln', 'hören', 'schreiben', 'arbeiten', 'ankommen', 'träumen', 'sich wenden', 'sprechen', 'helfen', 'antworten', 'sich erinnern', 'diskutieren', 'sich erholen', 'umgehen', 'sich gewöhnen', 'sich engagieren', 'hoffen', 'teilnehmen', 'sterben', 'sich bedanken', 'passen', 'sich beschweren', 'achten', 'sich ärgern', 'erzählen', 'sich wundern', 'schmecken', 'verzichten', 'sich vorbereiten', 'einladen', 'anfangen', 'beginnen', 'wohnen', 'sich bewerben', 'sich beschäftigen', 'danken', 'stören', 'glauben', 'sich kümmern', 'abhängen', 'ausgeben', 'nachdenken', 'denken', 'reden', 'sich treffen', 'sich beziehen']
BESTE_FREUNDE = ['anfangen', 'antworten', 'sich ärgern', 'aufhören', 'aufpassen', 'sich aufregen', 'ausgeben', 'sich bedanken', 'beneiden', 'bitten', 'danken', 'denken', 'einladen', 'sich entschuldigen', 'erfahren', 'sich erholen', 'sich erinnern', 'fragen', 'sich freuen', 'gehören', 'glauben', 'helfen', 'sich interessiern', 'sich kümmern', 'reden', 'schreiben', 'sprechen', 'streiten', 'suchen', 'teilnehmen', 'verzichten', 'warten']
ALL_BESTE_FREUNDE = BESTE_FREUNDE + ['beschäftigen', 'bestehen', 'sich eignen', 'erzählen', 'gehen', 'gelten', 'gratulieren', 'hoffen', 'hören', 'sich informieren', 'lachen', 'passen', 'protestieren', 'schimpfen', 'schmecken', 'sein', 'sterben', 'streiten', 'telefonieren', 'sich treffen', 'sich unterhalten', 'sich verabreden', 'verstehen', 'wissen']

ALL_WORDS = list(set(WORDS + ALL_BESTE_FREUNDE))

