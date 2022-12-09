SELECT
	i.id, i.name, AVG(r.star) AS star
FROM
	item AS i LEFT JOIN review AS r
		ON r.item_id = i.id
	LEFT JOIN member AS m
		ON r.mem_id = m.id
WHERE m.gender = 'f'
GROUP BY i.id, i.name
ORDER BY star DESC;