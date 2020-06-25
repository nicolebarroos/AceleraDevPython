from django.shortcuts import render
from django.db.models import Q
from datetime import datetime, timedelta
from api.models import User, Agent, Event, Group

def get_active_users() -> User:
    #Entry.objects.filter(pub_date__year=2006)
    """Traga todos os uarios ativos, seu último login deve ser menor que 10 dias """
    today = datetime.today()
    ten = timedelta(10)
    q1 = User.objects.filter(last_login__gte=(today - ten))
    return q1
        

def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    q2 = User.objects.count()
    return q2


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    q3 = User.objects.filter(group__name='admin')
    return q3


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    q4 = Event.objects.filter(level='debug')
    return q4


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    q5 = Event.objects.filter(agent=agent, level="critical")
    return q5


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    q6 = Agent.objects.filter(user__name=username)
    return q6


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    q7 = Group.objects.filter(user__agent__event__level='information')
    return q7

