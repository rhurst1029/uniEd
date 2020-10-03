BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "course" (
	"course_id"	INTEGER NOT NULL,
	"instructor"	VARCHAR(36),
	"course_name"	VARCHAR(36),
	PRIMARY KEY("course_id")
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(64),
	"email"	VARCHAR(120),
	"password_hash"	VARCHAR(128),
	"about_me"	VARCHAR(140),
	"last_seen"	DATETIME,
	"instructor"	BOOLEAN,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "lecture" (
	"lecture_id"	INTEGER NOT NULL,
	"lecture_topic"	VARCHAR(36),
	"course_num"	INTEGER,
	"lecture_date"	VARCHAR(3),
	"lecture_week"	INTEGER,
	FOREIGN KEY("course_num") REFERENCES "course"("course_id"),
	PRIMARY KEY("lecture_id")
);
CREATE TABLE IF NOT EXISTS "post" (
	"id"	INTEGER NOT NULL,
	"body"	VARCHAR(140),
	"timestamp"	DATETIME,
	"user_id"	INTEGER NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "user"("id"),
	PRIMARY KEY("id","user_id")
);
CREATE TABLE IF NOT EXISTS "sub" (
	"id"	INTEGER NOT NULL,
	"subtopic"	VARCHAR(42),
	"lecture_num"	INTEGER,
	FOREIGN KEY("lecture_num") REFERENCES "lecture"("lecture_id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "question" (
	"question_id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"subtopic_id"	VARCHAR(42),
	"question"	VARCHAR(180),
	"content"	VARCHAR(180),
	FOREIGN KEY("user_id") REFERENCES "user"("id"),
	FOREIGN KEY("subtopic_id") REFERENCES "sub"("id"),
	PRIMARY KEY("question_id")
);
INSERT INTO "course" VALUES (1,'Josh Hug','CS61B');
INSERT INTO "course" VALUES (2,'Paul Hilfinger','CS61A');
INSERT INTO "course" VALUES (3,'Yining Liu','CS70');
INSERT INTO "course" VALUES (4,'Ryan Hurst','DATA100');
INSERT INTO "user" VALUES (1,'ryan','rhurst1029@gmail.com','pbkdf2:sha256:150000$nhwdHdxC$9fb3cadd0d7678b8841d7b618ccadea524498ca46d5cfa9dcc4e44d4444315c8',NULL,'2020-06-16 22:17:58.734416',NULL);
INSERT INTO "user" VALUES (2,'testInstructor','ryanhurst@berkeley.edu','pbkdf2:sha256:150000$VfXzelso$6f19549230faaf93c5165a9c52a472ffc2668b6b6629c38d04475ba61f97ae5f',NULL,'2020-06-13 00:13:03.230833',1);
INSERT INTO "user" VALUES (3,'instructorTest','ryanbuddy@gmail.com','pbkdf2:sha256:150000$JX5fghhG$c3fb26086e06b5548fa2a8bcbfbe0e1bcffc24981703377526c594ac06755713',NULL,'2020-06-13 00:13:58.144852',1);
INSERT INTO "user" VALUES (4,'i','a@b.com','pbkdf2:sha256:150000$wf0xtszh$ad70007c96f039aa5a9e4a8c9e980e972871b055fce159678c39187da75a8224',NULL,'2020-06-13 18:43:47.299205',1);
INSERT INTO "user" VALUES (5,'joshhug','j@a.com','pbkdf2:sha256:150000$jh9vPkZ4$54742358fd780232d5c22a3b928c71dbf5a574de85b92a8012bca7d12719decb',NULL,'2020-06-16 17:52:18.333191',1);
INSERT INTO "user" VALUES (6,'rhurst','a@gmail.com','pbkdf2:sha256:150000$XMdcvKYP$037cc59ca97455483cee2e57ad391bac2ccdb8919cc00066fe4fd870fcee797f',NULL,'2020-06-14 02:27:14.781224',0);
INSERT INTO "lecture" VALUES (1,'Pre: An Outline of 61B',1,'2020-01-22 00:00:00',1);
INSERT INTO "lecture" VALUES (2,'Intro, Hello World Java',1,'2020-01-23 00:00:00',1);
INSERT INTO "lecture" VALUES (3,'Defining & Using Classes',1,'2020-01-25 00:00:00',1);
INSERT INTO "lecture" VALUES (4,'References, Recursion, and Lists',1,'2020-01-28 00:00:00',2);
INSERT INTO "lecture" VALUES (5,'SLLists, Nested Classes, Sential nodes',1,'2020-01-30 00:00:00',2);
INSERT INTO "lecture" VALUES (6,'DLLists, Arrays',1,'2020-02-01 00:00:00',2);
INSERT INTO "lecture" VALUES (7,'ALists, Resizing, vs. SLists',1,'2020-02-04 00:00:00',3);
INSERT INTO "lecture" VALUES (8,'Testing',1,'2020-02-06 00:00:00',3);
INSERT INTO "lecture" VALUES (9,'Inheritance, Implements',1,'2020-02-08 00:00:00',3);
INSERT INTO "sub" VALUES (1,'Compilation',3);
INSERT INTO "sub" VALUES (2,'Defining & Instantiating Classes',3);
INSERT INTO "sub" VALUES (3,'Terminology',3);
INSERT INTO "sub" VALUES (4,'Arrays Of Objects',3);
INSERT INTO "sub" VALUES (5,'Static vs Instance Methods',3);
INSERT INTO "sub" VALUES (6,'Public Static Void Main',3);
INSERT INTO "sub" VALUES (7,'Using Libraries',3);
INSERT INTO "sub" VALUES (8,'Primitive Types',4);
INSERT INTO "sub" VALUES (9,'Reference Types',4);
INSERT INTO "sub" VALUES (10,'Parameter Passing',4);
INSERT INTO "sub" VALUES (11,'Instantiating Arrays',4);
INSERT INTO "sub" VALUES (12,'IntLists',4);
INSERT INTO "sub" VALUES (13,'SLLists',5);
INSERT INTO "sub" VALUES (14,'Access Control & Nested Classes',5);
INSERT INTO "sub" VALUES (15,'addLast & Size',5);
INSERT INTO "sub" VALUES (16,'Caching',5);
INSERT INTO "sub" VALUES (17,'The Empty List',5);
INSERT INTO "sub" VALUES (18,'Sentinel Nodes',5);
INSERT INTO "sub" VALUES (19,'Invariants',5);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_user_email" ON "user" (
	"email"
);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_user_username" ON "user" (
	"username"
);
CREATE INDEX IF NOT EXISTS "ix_post_timestamp" ON "post" (
	"timestamp"
);
COMMIT;
