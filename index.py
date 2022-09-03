#!python
print("Content-Type: text/html")
print()
print("Hello world")
print('''<!doctype html>
<html>
<head>
	<title>WEB - html</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="index.html">WEB</a></h1>
	<ol>
		<li><a href="index.py?id=HTML">HTML</a></li>
		<li><a href="index.py?id=CSS">CSS</a></li>
		<li><a href="index.py?id=JAVA">JAVA</a></li>
	</ol>

	<h2>{title}</h2>

	<p>hihi monkey <br><strong>haha</strong> <u>dasf</u> asdfsaf<br>
	dsfklajflksajlfjlasjflsksajflksajlkfjaslkfjlkscjdklajsfkjqiejofqijdklz
	<a href="https://www.w3.org/TR/2011/WD-html5-20110405/">dskljflasdjflkasjflkasjflkasjfdlksajfkd</a>
	sahfoqwenmzcnzvmnz,zvn,zjfi</p> 
</body>
</html>'''.format(title='Hello'))