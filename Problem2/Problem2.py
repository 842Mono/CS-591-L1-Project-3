import sqlalchemy
print(sqlalchemy.__version__ )
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    player_id = Column(Integer, ForeignKey('players.id'))
    players = relationship("Player", back_populates="teams")

    # players = relationship("Player", back_populates="teams")
    # players_id = Column(Integer, ForeignKey('players.id'))

    # games_id = Column(Integer, ForeignKey('games.id'))
    games = relationship("Game", back_populates="teams") #foreign_keys=games_id, back_populates="teams")
    # # games2 = relationship("Game", back_populates="teams")

    def __repr__(self):
        return "<Team(name='%s')>" % (self.name)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    # Teams_id = Column(Integer, ForeignKey('teams.id'))
    teams = relationship("Team", back_populates="players")
    teams2 = relationship("Team", back_populates="players")


    # teams = relationship("Team", order_by=Team.id, back_populates="players")

    def __repr__(self):
        return "<Player(name='%s', position='%s')>" % (self.name, self.position)

class PlayerTeamsAssociationTable(Base):
    __tablename__ = 'Player/Teams Association Table'

    id = Column(Integer, primary_key=True)
    playerName = Column(String)
    teamName = Column(String)
    season = Column(Integer)
    def __repr__(self):
        return "<PlayerTeamsAssociationTable(PlayerName='%s', TeamName='%s', Season='%s')>" % (self.playerName, self.teamName, self.season)


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    # teams = relationship(Team, back_populates="games")
    # homeTeamName_id = Column(Integer, ForeignKey('teams.id'))
    # teamsawayTeamName = relationship("Team", back_populates="games")
    # awayTeam_id = Column(Integer, ForeignKey('teams.id'))
    # teams = relationship("Team", back_populates="players")

    # home_team_id = Column(Integer, ForeignKey('teams.id'))
    # home_team = relationship('Team', foreign_keys=[home_team_id], back_populates="games")
    # away_team_id = Column(Integer, ForeignKey('teams.id'))
    # away_team = relationship('Team', foreign_keys=[away_team_id], back_populates="games")
    # teams = relationship("Team", foreign_keys=[home_team_id, away_team_id], back_populates="games")

    # away_team_id = Column(Integer, ForeignKey('teams.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    teams = relationship("Team", foreign_keys=[team_id], back_populates="games") #[home_team_id, away_team_id])

    # awayTeamName = relationship("Team", foreign_keys=awayTeamName_id, back_populates="games")

    season = Column(Integer)
    week = Column(Integer)
    homeScore = Column(Integer)
    awayScore = Column(Integer)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)



# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)



from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

import csv

with open('data/reg_games_2010.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} ... {row[1]} ... {row[2]}.')
            session.add(Game(id=row[1], teams=[Team(id=row[2]), Team(id=row[3])], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))
            # for i in len(row):

            # """type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score"""
            # if()



            line_count += 1
    print(f'Processed {line_count} lines.')