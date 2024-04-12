/* use block comments to isolate the queries you want   */


--Query 1
SELECT player_name, AVG(Shot.xg_score) AS avg_xg
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Shot
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name = '2020/2021' AND Competition.competition_name = 'La Liga'
GROUP BY player_name
ORDER BY avg_xg DESC;



--Query 2
SELECT player_name, COUNT(Shot.event_id) AS shotnum
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Shot
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name = '2020/2021' AND Competition.competition_name = 'La Liga'
GROUP BY player_name
ORDER BY shotnum DESC;



--Query 3
SELECT player_name, COUNT(Shot.event_id) AS first_time_shots
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Shot
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name IN ('2020/2021', '2019/2020', '2018/2019') 
AND Competition.competition_name = 'La Liga'
AND Shot.first_time = true
GROUP BY player_name
ORDER BY first_time_shots DESC;




--Query 4
SELECT team_name, COUNT(Pass.event_id) AS  pass_count
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Pass
JOIN Team on Event.event_team_id = Team.team_id
WHERE Season.season_name ='2020/2021'
AND Competition.competition_name = 'La Liga'
GROUP BY team_name
ORDER BY pass_count DESC;




--Query 5
SELECT player_name, COUNT(Pass.event_id) AS intended_recipient_count
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Pass
JOIN Player on Pass.recipiant_player_id = Player.player_id
WHERE Season.season_name = '2003/2004'
AND Competition.competition_name = 'Premier League'
GROUP BY player_name
ORDER BY intended_recipient_count DESC;




--Query 6
SELECT team_name, COUNT(Shot.event_id) AS num_shots
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Shot
JOIN Team on Event.event_team_id = Team.team_id
WHERE Season.season_name = '2003/2004'
AND Competition.competition_name = 'Premier League'
GROUP BY team_name
ORDER BY num_shots DESC;




--Query 7
SELECT player_name, COUNT(Pass.event_id) AS through_balls
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Pass
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name = '2020/2021'
AND Competition.competition_name = 'La Liga'
AND Pass.technique = 'Through Ball'
GROUP BY player_name
ORDER BY through_balls DESC;




--Query 8
SELECT team_name, COUNT(Pass.event_id) AS through_balls
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Pass
JOIN Team on Event.event_team_id = Team.team_id
WHERE Season.season_name = '2020/2021'
AND Competition.competition_name = 'La Liga'
AND Pass.technique = 'Through Ball'
GROUP BY team_name
ORDER BY through_balls DESC;




--Query 9
SELECT player_name, COUNT(Dribble.event_id) AS completed_dribbles
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Dribble
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name IN ('2020/2021', '2019/2020', '2018/2019') 
AND Competition.competition_name = 'La Liga'
AND Dribble.outcome = 'Complete'
GROUP BY player_name
ORDER BY completed_dribbles DESC;




--Query 10
SELECT player_name, COUNT(Dribbled_past.event_id) AS dribbled_past
FROM Competition NATURAL JOIN Season NATURAL JOIN Matches NATURAL JOIN Event NATURAL JOIN Dribbled_past
JOIN Player on Event.player_id = Player.player_id
WHERE Season.season_name = '2020/2021'
AND Competition.competition_name = 'La Liga'
GROUP BY player_name
ORDER BY dribbled_past ASC;




