import sqlalchemy
print(sqlalchemy.__version__ )
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship, sessionmaker

class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return "<Team(name='%s')>" % (self.name)



class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    position = Column(String)

class PlayerTeamsAssociationTable(Base):
    __tablename__ = 'Player/Teams Association Table'

    id = Column(Integer, primary_key=True)
    team = Column(Integer, ForeignKey('team.id'))
    player = Column(Integer, ForeignKey('player.id'))
    season = Column(Integer)
    
    def __repr__(self):
        return "<PlayerTeamsAssociationTable(id='%s', team='%s', player='%s', season='%s')>" % (self.id, self.team, self.player, self.season)




class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)

    home_team = Column(String, ForeignKey('team.id'))
    away_team = Column(String, ForeignKey('team.id'))

    season = Column(Integer)
    week = Column(Integer)
    homeScore = Column(Integer)
    awayScore = Column(Integer)


    def __repr__(self):
        return "<Game(id='%s', home_team='%s', away_team='%s', season='%s', week='%s', homeScore='%s', awayScore='%s')>" % (self.id, self.home_team, self.away_team, self.season, self.week, self.homeScore, self.awayScore)





engine = create_engine('sqlite:///testfile.db', echo=True)
Base.metadata.create_all(bind=engine)


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
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')


with open('data/reg_games_2011.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')



with open('data/reg_games_2012.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')



with open('data/reg_games_2013.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')



with open('data/reg_games_2014.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')


with open('data/reg_games_2015.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
                # print(r)
                # pass
            # print("============================================")
            session.add(Game(id=row[1], home_team=row[2], away_team=row[3], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))


            teamExists = session.query(Team).filter_by(name=row[2]).first()
            if not teamExists:
                session.add(Team(name=row[2]))

            teamExists = session.query(Team).filter_by(name=row[3]).first()
            if not teamExists:
                session.add(Team(name=row[3]))

            # type, game_id, home_team, away_team, week, season, state_of_game, game_url, home_score, away_score

            line_count += 1
    print(f'Processed {line_count} lines.')



session.commit()



with open('data/reg_roster_2010.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')


with open('data/reg_roster_2011.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')



with open('data/reg_roster_2012.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')




with open('data/reg_roster_2013.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')



with open('data/reg_roster_2014.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')



with open('data/reg_roster_2015.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print("********************************************")
            # for r in row:
            #     print(r)
            # print("============================================")

            playerExists = session.query(Player).filter_by(name=row[2]).first()

            if not playerExists:
                session.add(Player(id=int(row[6][5:]), name=row[2], position=row[5])) # team=row[4],
            
            session.add(PlayerTeamsAssociationTable(team=row[4], player=int(row[6][5:]), season=row[0]))
            
            # season, season_type, full_player_name, abbr_player_name, team, position, gsis_id

            session.commit()

            line_count += 1

    print(f'Processed {line_count} lines.')



session.commit()


from sqlalchemy import func
# from sqlalchemy.sql import select

q = session.query(Team).outerjoin(Game, Team.name==Game.home_team).all()

print("the query")
print(q)
for item in q:
    print(item)



session.close()