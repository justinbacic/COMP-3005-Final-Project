
--Country; country_id, country_name
CREATE TABLE Country (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(255)
);

--Competition;  competition_id, competition_name,  competition_gender,  season_id, country_id
CREATE TABLE Competition(
    competition_id INT PRIMARY KEY,
    competition_name VARCHAR(255),
    competition_gender VARCHAR(255),
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id)
);


--Season;  season_id, season_name
CREATE TABLE Season (
	season_id INT PRIMARY KEY,
	season_name VARCHAR(255),
	competition_id INT,
	FOREIGN KEY (competition_id) REFERENCES Competition (competition_id)
);

--Stadium; stadium_id, stadium_name, country_id
CREATE TABLE Stadium (
    stadium_id INT PRIMARY KEY,
    stadium_name VARCHAR(255),
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id)
);
--Team;  team_id, team_name, team_gender, country_id
CREATE TABLE Team (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(255),
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id)
);
--Manager;  manager_id, manager_name, nickname, date_of_birth, country_id, 
CREATE TABLE Manager (
    manager_id INT PRIMARY KEY,
    manager_name VARCHAR(255),
    nickname VARCHAR(255),
    date_of_birth DATE,
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id)
);
--Referee;  referee_id, referee_name, country_id
CREATE TABLE Referee (
    referee_id INT PRIMARY KEY,
    referee_name VARCHAR(255),
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id)
);

--Match;  match_id, match_date, kick_off, home_score, away_score, match_week, stage_id, stadium_id, home_team_id, home_team_manager_id, home_team_lineup[player_id], away_team_id, away_team_manager_id, away_team_lineup[player_id], referee_id
CREATE TABLE Matches (
    match_id INT PRIMARY KEY,
    match_date DATE,
    kick_off VARCHAR (255),
    home_score INT,
    away_score INT,
    match_week INT,
	season_id INT,
    FOREIGN KEY (season_id) REFERENCES Season (season_id),
    stage_name VARCHAR(255),
	stadium_id INT,
    FOREIGN KEY (stadium_id) REFERENCES Stadium (stadium_id),
	home_team_id INT,
    FOREIGN KEY (home_team_id) REFERENCES Team (team_id),
	home_team_manager_id INT,
    FOREIGN KEY (home_team_manager_id) REFERENCES Manager (manager_id),
	away_team_id INT,
    FOREIGN KEY (away_team_id) REFERENCES Team (team_id),
	away_team_manager_id INT,
    FOREIGN KEY (away_team_manager_id) REFERENCES Manager (manager_id),
	referee_id INT,
    FOREIGN KEY (referee_id) REFERENCES Referee (referee_id)
);

--Player;  player_id, player_name, nickname, jersy_number, country_id
CREATE TABLE Player (
    player_id INT PRIMARY KEY,
    player_name VARCHAR (255),
    nickname VARCHAR (255),
    jersy_number INT,
	country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country (country_id) 
);
--Position: player_id, team_id, match_id, position, from_time, to_time, from_period, to_period, start_reason, end_reason
CREATE TABLE Position (
	player_id INT,
    FOREIGN KEY (player_id) REFERENCES Player (player_id),
	team_id INT,
    FOREIGN KEY (team_id) REFERENCES Team (team_id),
	match_id INT,
    FOREIGN KEY (match_id) REFERENCES Matches (match_id),
    position VARCHAR (255),
    from_time VARCHAR(255),
    to_time VARCHAR(255),
    from_period INT,
    to_period INT,
    start_reason VARCHAR(255),
    end_reason VARCHAR(255)
);

--Event;  event_id, match_id, index, period, timestamp, type_id, type_name, possession, posession_team_id, play_pattern_name, event_team_id, player_id, position,  location[x,y], duration, under_pressure, out
CREATE TABLE Event (
    event_id VARCHAR(255) PRIMARY KEY,
	match_id INT,
    FOREIGN KEY (match_id) REFERENCES Matches (match_id),
    event_index INT,
    event_period INT, 
    event_timestamp VARCHAR(255),
    type_id INT,
    type_name VARCHAR(255),
    possession INT,
	possession_team_id INT,
    FOREIGN KEY (possession_team_id) REFERENCES Team (team_id),
    play_pattern_name VARCHAR(255),
	event_team_id INT,
    FOREIGN KEY (event_team_id) REFERENCES Team (team_id),
	player_id INT,
    FOREIGN KEY (player_id) REFERENCES Player (player_id),
    location_x INT,
    location_y INT,
    duration FLOAT, 
    under_pressure BOOLEAN,
    ball_out BOOLEAN
);
--Block; event_id, counterpress, deflection, offensive, save_block
CREATE TABLE Block (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    counterpress BOOLEAN,
    deflection BOOLEAN,
    offensive BOOLEAN,
    save_block BOOLEAN
);
--Ball_Receipt; event_id,  outcome
CREATE TABLE Ball_Receipt (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    outcome VARCHAR(255)
);
--Dribble; event_id, outcome, nutmeg, overrun, no_touch
CREATE TABLE Dribble (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    outcome VARCHAR(255),
    nutmeg BOOLEAN,
    overrun BOOLEAN,
    no_touch BOOLEAN
);
--Dribbled_Past; event_id,  counterpress
CREATE TABLE Dribbled_Past (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    counterpress BOOLEAN
);
--Pass; event_id, recipiant_player_id, length, angle, height, end_location[x,y], body_part, type, outcome, technique, deflected, miscommunication
CREATE TABLE Pass (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
	recipiant_player_id INT,
    FOREIGN KEY (recipiant_player_id) REFERENCES Player (player_id),
    length FLOAT,
    angle FLOAT,
    height VARCHAR(255),
    end_location_x FLOAT,
    end_location_y FLOAT,
    body_part VARCHAR(255),
    type VARCHAR(255),
    outcome VARCHAR(255),
    technique VARCHAR(255),
    deflected BOOLEAN,
    miscommunication BOOLEAN
);
--Shot; event_id, end_location[x,y,z], first_time, xg_score, deflected, technique, body_part, type, outcome
CREATE TABLE Shot (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    end_location_x FLOAT,
    end_location_y FLOAT,
    end_location_z FLOAT,
    first_time BOOLEAN,
    xg_score FLOAT,
    deflected BOOLEAN,
    technique VARCHAR(255),
    body_part VARCHAR(255),
    type VARCHAR(255),
    outcome VARCHAR(255)
);
--Carry; event_id, end_location[x,y]
CREATE TABLE Carry (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    end_location_x INT,
    end_location_y INT
);
--Foul_Committed; event_id, advantage, counterpress, offensive, penalty, card, type
CREATE TABLE Foul_Committed (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    advantage BOOLEAN,
    counterpress BOOLEAN,
    offensive BOOLEAN,
    penalty BOOLEAN,
    card VARCHAR(255),
    type VARCHAR(255)
);
--Foul_Won; event_id, advantage, defensive, penalty
CREATE TABLE Foul_Won (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    advantage BOOLEAN,
    defensive BOOLEAN,
    penalty BOOLEAN
);
--Goal_Keeper; event_id, position, technique, body_part, type, outcome
CREATE TABLE Goal_Keeper (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    position VARCHAR(255),
    technique VARCHAR(255),
    body_part VARCHAR(255),
    type VARCHAR(255),
    outcome VARCHAR(255)
);
--Interception; event_id, outcome
CREATE TABLE Interception (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    outcome VARCHAR(255)
);
--Duel; event_id, counterpress, type, outcome
CREATE TABLE Duel (
	event_id VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    counterpress BOOLEAN,
    outcome VARCHAR(255)
);
