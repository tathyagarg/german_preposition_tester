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
    ['diskutieren', 'erzählen', 'nachdenken', 'reden', 'schimpfen', 'sich ärgern', 'sich aufregen', 'sich beschweren', 'sich freuen', 'sich informieren', 'sich unterhalten', 'sich wundern', 'sprechen', 'streiten', 'verfüngen', 'verhandeln'],
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
    ['ausgeben', 'danken', 'eignen', 'kämpfen', 'kaufen', 'protestieren', 'sich bedanken', 'sich engagieren', 'sich entschuldigen', 'sich interessieren', 'sorgen'],
    True
)
um = Preposition(
    'um',
    ['beneiden', 'bitten', 'es geht', 'sich bewerben', 'sich handeln', 'sich kümmern', 'sich streiten'],
    True
)
von = Preposition(
    'von',
    ['abhängen', 'erfahren', 'sich erholen', 'erzählen', 'hören', 'träumen', 'sich verabschieden'],
    False
)
zu = Preposition(
    'zu',
    ['einladen', 'führen', 'gehören', 'gratulieren', 'meinen', 'passen'],
    False
)

DUPLICATES = {'diskutieren': ('mit', 'über'), 'reden': ('mit', 'über'), 'sich freuen': ('auf', 'über'), 'sich unterhalten': ('mit', 'über'), 'sprechen': ('mit', 'über'), 'verhandeln': ('mit', 'über'), 'sich beschweren': ('über', 'bei'), 'sich bedanken': ('bei', 'für'), 'sich entschuldigen': ('bei', 'für'), 'sich streiten': ('mit', 'um'), 'erzählen': ('über', 'von')}
WORDS = ['aufpassen', 'beneiden', 'schimpfen', 'erfahren', 'bitten', 'sich informieren', 'sich entschuldigen', 'suchen', 'kaufen', 'eignen', 'führen', 'sich interessieren', 'streiten', 'verfüngen', 'sich aufregen', 'protestieren', 'rechnen', 'sich richten', 'kämpfen', 'sich verabreden', 'fragen', 'sich verabschieden', 'sorgen', 'fahren', 'meinen', 'es geht', 'sich freuen', 'sich unterhalten', 'telefonieren', 'riechen', 'sich konzenteiren', 'warten', 'verhandeln', 'leiden', 'aufhören', 'gehören', 'gratulieren', 'vergleichen', 'sich verstehen', 'sich streiten', 'sich handeln', 'hören', 'schreiben', 'arbeiten', 'ankommen', 'träumen', 'sich wenden', 'sprechen', 'helfen', 'antworten', 'sich erinnern', 'diskutieren', 'sich erholen', 'umgehen', 'sich gewöhnen', 'sich engagieren', 'hoffen', 'teilnehmen', 'sterben', 'sich bedanken', 'passen', 'sich beschweren', 'achten', 'sich ärgern', 'erzählen', 'sich wundern', 'schmecken', 'verzichten', 'sich vorbereiten', 'einladen', 'anfangen', 'beginnen', 'wohnen', 'sich bewerben', 'sich beschäftigen', 'danken', 'stören', 'glauben', 'sich kümmern', 'abhängen', 'ausgeben', 'nachdenken', 'denken', 'reden', 'sich treffen', 'sich beziehen']
