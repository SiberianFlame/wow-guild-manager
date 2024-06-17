from django.contrib.auth.models import User
from django.db import models


def get_class_choices():
    return [
        ('DK', (('Death Knight'))),
        ('DH', (('Demon Hunter'))),
        ('DR', (('Druid'))),
        ('EV', (('Evoker'))),
        ('HR', (('Hunter'))),
        ('MG', (('Mage'))),
        ('MK', (('Monk'))),
        ('PL', (('Paladin'))),
        ('PT', (('Priest'))),
        ('RG', (('Rogue'))),
        ('SM', (('Shaman'))),
        ('WK', (('Warlock'))),
        ('WR', (('Warrior')))
    ]
    # return [
    #     ('DK', 'Death Knight'),
    #     ('DH', 'Demon Hunter'),
    #     ('DR', 'Druid'),
    #     ('EV', 'Evoker'),
    #     ('HR', 'Hunter'),
    #     ('MG', 'Mage'),
    #     ('MK', 'Monk'),
    #     ('PL', 'Paladin'),
    #     ('PT', 'Priest'),
    #     ('RG', 'Rogue'),
    #     ('SM', 'Shaman'),
    #     ('WK', 'Warlock'),
    #     ('WR', 'Warrior')
    # ]
    # return {
    #     'Demon Knight': {
    #         'BD': 'Blood',
    #         'FRT': 'Frost',
    #         'UH': 'Unholy'
    #     },
    #     'Demon Hunter': {
    #         'HC': 'Havoc',
    #         'VG': 'Vengeance'
    #     },
    #     'Druid': {
    #         'BC': 'Balance',
    #         'FER': 'Feral',
    #         'GD': 'Guardian',
    #         'RS': 'Restoration'
    #     },
    #     'Evoker': {
    #         'AG': 'Augmentation',
    #         'DST': 'Devastation',
    #         'PS': 'Preservation'
    #     },
    #     'Hunter': {
    #         'BM': 'Beast Mastery',
    #         'MS': 'Marksmanship',
    #         'SV': 'Survival'
    #     },
    #     'Mage': {
    #         'AC': 'Arcane',
    #         'FR': 'Fire',
    #         'FST': 'Frost'
    #     },
    #     'Monk': {
    #         'BW': 'Brewmaster',
    #         'MW': 'Mistweaver',
    #         'WW': 'Windwalker'
    #     },
    #     'Paladin': {
    #         'HL': 'Holy',
    #         'PT': 'Protection',
    #         'RT': 'Retribution'
    #     },
    #     'Priest': {
    #         'DS': 'Discipline',
    #         'HL': 'Holy',
    #         'SHD': 'Shadow'
    #     },
    #     'Rogue': {
    #         'AS': 'Assassination',
    #         'OW': 'Outlaw',
    #         'SB': 'Subtlety'
    #     },
    #     'Shaman': {
    #         'EL': 'Elemental',
    #         'EH': 'Enhancement',
    #         'RST': 'Restoration'
    #     },
    #     'Warlock': {
    #         'AF': 'Affliction',
    #         'DL': 'Demonology',
    #         'DSR': 'Destruction'
    #     },
    #     'Warrior': {
    #         'AM': 'Arms',
    #         'FRY': 'Fury',
    #         'PTN': 'Protection'
    #     },
    # }


class UserProfile(models.Model):
    """
    UserProfile class for extending standard Django user model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='profile')
    email = models.CharField(max_length=100, verbose_name='email')
    nickname = models.CharField(max_length=20, verbose_name='nickname', unique=True)
    char_class = models.CharField(max_length=20, choices=get_class_choices())
