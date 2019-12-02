
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
            # print("============================================")

            session.add(Game(id=row[1], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))

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
            # print("============================================")

            session.add(Game(id=row[1], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))

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
            # print("============================================")

            session.add(Game(id=row[1], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))

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
            # print("============================================")

            session.add(Game(id=row[1], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))

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
            # print("============================================")

            session.add(Game(id=row[1], week=row[4], season=row[5], homeScore=row[8], awayScore=row[9]))

            line_count += 1

    print(f'Processed {line_count} lines.')


######################

with open('data/reg_roster_2010.csv') as csv_file:
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
            # print("============================================")


            #season, season_type, full_player_name, abbr_player_name, team, position, gsis_id
            # __tablename__ = 'player'

            # id = Column(Integer, primary_key=True)
            # name = Column(String, unique=True)
            # position = Column(String)

            # player_id = Column(Integer, ForeignKey('team.id')) #question
            # teams = relationship("Team", back_populates="players")





            # __tablename__ = 'Player/Teams Association Table'

            # id = Column(Integer, primary_key=True)
            # teamName = Column(Integer, ForeignKey('team.name'))
            # playerName = Column(Integer, ForeignKey('player.name'))
            # season = Column(Integer)



            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')


with open('data/reg_roster_2011.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')

with open('data/reg_roster_2012.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')


with open('data/reg_roster_2012.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')


with open('data/reg_roster_2013.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')



with open('data/reg_roster_2014.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')


with open('data/reg_roster_2015.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            session.add(Player(id=row[6], name=row[2], position=row[5])) # team=row[4],
            session.add(PlayerTeamsAssociationTable(id=row[6], teamName=row[4], playerName=row[2], season=row[0]))



            line_count += 1

    print(f'Processed {line_count} lines.')




session.commit()


from sqlalchemy import func

q = session.query(Team).join(Game, Team.id==Game.home_team).all()
# q = session.query(Team).join(Game, Team.id==Game.home_team).all()


print(q)