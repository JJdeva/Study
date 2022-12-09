SELECT
	i.name, i.id,
    r.item_id, r.star, r.comment, r.mem_id,
    m.id, m.email
FROM
	item AS i LEFT JOIN review AS r
		ON r.item_id = i.id
	LEFT JOIN member AS m
		ON r.mem_id = m.id;