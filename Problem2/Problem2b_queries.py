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


from sqlalchemy import func, desc


query1result = []
half1 = []
half2 = []

# qa = session.execute("""SELECT team.id, team.name, sum(game.homeScore) AS totalHS, sum(game.awayScore) AS totalAS,
# sum(game.homeScore) - sum(game.awayScore) AS diff
# FROM team LEFT OUTER JOIN game ON team.name = game.home_team GROUP BY team.id ORDER BY diff DESC""")

qa = session.query(Team.id, Team.name, func.sum(Game.homeScore), func.sum(Game.awayScore), func.sum(Game.homeScore) - func.sum(Game.awayScore)).outerjoin(Game, Team.name == Game.home_team).group_by(Team.id).order_by(desc(func.sum(Game.homeScore) - func.sum(Game.awayScore)))

for item in qa:
    # print(item)
    half1.append(item)


# qb = session.execute("""SELECT team.id, team.name, sum(game.homeScore) AS totalHS, sum(game.awayScore) AS totalAS,
# sum(game.awayScore) - sum(game.homeScore) AS diff
# FROM team LEFT OUTER JOIN game ON team.name = game.away_team GROUP BY team.id ORDER BY diff DESC""")

qb = session.query(Team.id, Team.name, func.sum(Game.homeScore), func.sum(Game.awayScore), func.sum(Game.awayScore) - func.sum(Game.homeScore)).outerjoin(Game, Team.name == Game.away_team).group_by(Team.id).order_by(desc(func.sum(Game.awayScore) - func.sum(Game.homeScore)))

for item in qb:
    # print(item)
    half2.append(item)

half1.sort(key=lambda x : x.id)

half2.sort(key=lambda x : x.id)


i = 0
while i < len(half1):
    obj = {}
    obj['id'] = half1[i][0]
    obj['name'] = half1[i][1]
    obj['diff'] = half1[i][4] + half2[i][4]
    query1result.append(obj)
    i = i + 1

query1result.sort(key=lambda x : x['diff'], reverse=True)

query1result = query1result[:3]

print("Result of query 1:")
for item in query1result:
    print(item)




###

ql3 = []
ql1 = []
ql2 = []

q1 = session.execute("""
SELECT player.id, player.name, count(DISTINCT(game.id)) AS ct FROM player
JOIN "Player/Teams Association Table" ON player.id = "Player/Teams Association Table".player
JOIN game ON "Player/Teams Association Table".team = game.home_team WHERE game.homeScore > game.awayScore
GROUP BY player.id

INTERSECT

SELECT player.id, player.name, count(DISTINCT(game.id)) AS ct FROM player
JOIN "Player/Teams Association Table" ON player.id = "Player/Teams Association Table".player
JOIN game ON "Player/Teams Association Table".team = game.away_team WHERE game.awayScore > game.homeScore
GROUP BY player.id

ORDER BY count(DISTINCT(game.id)) DESC LIMIT 10
""")

print(q1)
for item in q1:
    print(item)
    ql1.append(item)

#merge both



# q2 = session.execute("""SELECT player.id, player.name, count(DISTINCT(game.id)) AS ct FROM player
# JOIN "Player/Teams Association Table" ON player.id = "Player/Teams Association Table".player
# JOIN game ON "Player/Teams Association Table".team = game.away_team WHERE game.awayScore > game.homeScore
# GROUP BY player.id ORDER BY count(DISTINCT(game.id)) DESC LIMIT 10 """)

# print(q2)
# for item in q2:
#     print(item)
#     ql2.append(item)


# print("============================")


# i1 = 0
# i2 = 0
# while i1 < len(ql1):
#     while i2 < len(ql2):
#         if ql1[i1].id == ql2[i2].id:
#             if ql1[i1].ct > ql2[i2].ct:
#                 del ql2[i2]
#             else:
#                 del ql1[i1]
#                 i1 = i1 - 1
#             i2 = 0
#             break
#         i2 = i2 + 1
#     i2 = 0
#     i1 = i1 + 1

# ql3 = ql1 + ql2

# ql3.sort(key=lambda x : x.ct, reverse=True)

# ql3 = ql3[:10]

# print("Result of the second query:")
# for item in ql3:
#     print(item)




session.close()