CREATE TABLE mlb_wins (
	Year INT,
	Team VARCHAR PRIMARY KEY,
	Number_of_Games INT,
	Wins INT
);

SELECT * FROM mlb_wins

CREATE TABLE mlb_beer_prices (
	Year INT, 
	Team VARCHAR,
	Nickname VARCHAR,
	City VARCHAR,
	Price NUMERIC,
	Size INT,
	Price_per_Ounce NUMERIC
);

SELECT * FROM mlb_beer_prices



