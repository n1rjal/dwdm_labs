# BEFORE YOU BEGIN


```bash
python3 -m venv .env
```

```bash
source ./venv/bin/activate
```

```bash
pip install -r requirements.txt
```

If you are in other os other than window use this to create mysql.

```bash
docker run --name mysql \
  -e MYSQL_USER=dbuser \
  -e MYSQL_PASSWORD=password \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_ROOT_HOST=% \
  -e MYSQL_DATABASE=dwdm \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  --restart unless-stopped \
  -m 500m \
  mysql:latest

```

## LAB 2

```sql
CREATE TABLE courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(250),
    name VARCHAR(250),
    credit INT,
    type VARCHAR(25),
    semester INT
);



INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC109', 'Introduction to Information Technology', 3, 'Theory', 1);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC110', 'Programming', 3, 'Theory', 1);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC111', 'Digital Logic', 3, 'Theory', 1);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('MTH112', 'Mathematics I', 3, 'Theory', 1);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('PHY113', 'Physics', 3, 'Theory', 1);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC160', 'Discrete Structure', 3, 'Theory', 2);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC161', 'Object Oriented Programming', 3, 'Theory', 2);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC162', 'Microprocessor', 3, 'Theory', 2);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('MTH163', 'Mathematics II', 3, 'Theory', 2);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('STA164', 'Statistics I', 3, 'Theory', 2);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC206', 'Data Structure and Algorithm', 3, 'Theory', 3);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC207', 'Numerical Method', 3, 'Theory', 3);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC208', 'Computer Architecture', 3, 'Theory', 3);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC209', 'Computer Graphics', 3, 'Theory', 3);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('STA210', 'Statistics II', 3, 'Theory', 3);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC257', 'Theory of Computation', 3, 'Theory', 4);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC258', 'Computer Networks', 3, 'Theory', 4);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC259', 'Operating Systems', 3, 'Theory', 4);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC260', 'Database Management System', 3, 'Theory', 4);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC261', 'Artificial Intelligence', 3, 'Theory', 4);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC314', 'Design and Analysis of Algorithms', 3, 'Theory', 5);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC315', 'System Analysis and Design', 3, 'Theory', 5);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC316', 'Cryptography', 3, 'Theory', 5);
INSERT INTO courses (code, name, credit, type, semester) VALUES ('CSC317', 'Simulation and Modeling', 3, 'Theory', 5);
```


## Lab4

```sql


```
