SELECT * FROM book
WHERE isbn IN ('9781974715466');

SELECT title FROM book
WHERE genre IN ('Technology');

SELECT title, num_pages FROM book
WHERE author IN ('Donald Knuth');

SELECT DISTINCT author FROM book;
