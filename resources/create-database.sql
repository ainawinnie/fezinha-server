
-- -----------------------------------------------------
-- Table user
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS user (
  id VARCHAR(36) NOT NULL,
  name VARCHAR(100) NOT NULL,
  login VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);


-- -----------------------------------------------------
-- Table bet_group
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bet_group (
  id VARCHAR(36) NOT NULL,
  name VARCHAR(100) NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  PRIMARY KEY (id)
);


-- -----------------------------------------------------
-- Table bet_event
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bet_event (
  id VARCHAR(36) NOT NULL,
  event_date TIMESTAMP NOT NULL,
  name VARCHAR(100) NOT NULL,
  bet_group_id VARCHAR(36) NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (bet_group_id) REFERENCES bet_group(id),
  INDEX(bet_group_id)
 );


-- -----------------------------------------------------
-- Table competitor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS competitor (
  id VARCHAR(36) NOT NULL,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);


-- -----------------------------------------------------
-- Table bet_event_has_competitor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bet_event_has_competitor (
  competitor_id VARCHAR(36) NOT NULL,
  bet_event_id VARCHAR(36) NOT NULL,
  result FLOAT NULL,

  PRIMARY KEY (competitor_id, bet_event_id),
  FOREIGN KEY (competitor_id) REFERENCES competitor(id),
  FOREIGN KEY (bet_event_id) REFERENCES bet_event(id)
);


-- -----------------------------------------------------
-- Table bet
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bet (
  id VARCHAR(36) NOT NULL,
  bet_date TIMESTAMP NULL,
  user_id VARCHAR(36) NOT NULL,
  bet_event_id VARCHAR(36) NOT NULL,
  bet_value FLOAT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (bet_event_id) REFERENCES bet_event(id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  INDEX(user_id)
);


-- -----------------------------------------------------
-- Table bet_competitor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bet_competitor (
  bet_id VARCHAR(36) NOT NULL,
  competitor_id VARCHAR(36) NOT NULL,
  result FLOAT NULL,

  PRIMARY KEY (bet_id, competitor_id),
  FOREIGN KEY (bet_id) REFERENCES bet(id),
  FOREIGN KEY (competitor_id) REFERENCES competitor(id)
);


-- -----------------------------------------------------
-- Table transaction_point
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS transaction_point (
  id VARCHAR(36) NOT NULL,
  user_id VARCHAR(36) NOT NULL,
  transaction_date TIMESTAMP NOT NULL,
  value FLOAT NOT NULL,
  bet_id VARCHAR(36) NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (bet_id) REFERENCES bet(id),
  INDEX(user_id)
);
