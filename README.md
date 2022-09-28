# Quiz

A simple quiz application using Tkinter

## Steps
<br>
<ul>
<li> Download the zip file and extract the contents
<li> Run the following commands to install packages using command-line

```sh
  pip install tk
  pip install Pillow
  pip install mysql-connector-python
```

<li> Create an empty table in mysql 

```sh
CREATE TABLE `questions` (
  `qno` int(11) DEFAULT NULL,
  `question` varchar(256) DEFAULT NULL,
  `option1` varchar(256) DEFAULT NULL,
  `option2` varchar(256) DEFAULT NULL,
  `option3` varchar(256) DEFAULT NULL,
  `option4` varchar(256) DEFAULT NULL
) 
```

<li> Import the records from question-csv.csv file into the table
<li> Run the python script
<ul>
