CREATE TABLE train (
	`PassengerId` INTEGER NOT NULL, 
	`Survived` INTEGER NOT NULL, 
	`Pclass` INTEGER NOT NULL, 
	`Name` VARCHAR(82) NOT NULL, 
	`Sex` VARCHAR(6) NOT NULL, 
	`Age` FLOAT, 
	`SibSp` INTEGER NOT NULL, 
	`Parch` INTEGER NOT NULL, 
	`Ticket` VARCHAR(18) NOT NULL, 
	`Fare` FLOAT NOT NULL, 
	`Cabin` VARCHAR(15), 
	`Embarked` VARCHAR(4)
);
